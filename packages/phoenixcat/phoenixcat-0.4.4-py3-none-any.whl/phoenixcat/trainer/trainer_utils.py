import abc
import functools
import logging
import os
import json
from dataclasses import dataclass
from typing import Dict, Iterable, Callable


import torch
import torch.utils.data
from diffusers.utils import is_accelerate_available
from diffusers.configuration_utils import ConfigMixin, register_to_config

if is_accelerate_available():
    import accelerate
else:
    accelerate = None

from .. import constant
from ..conversion import get_obj_from_str
from ..logger.logging import init_logger
from ..random._seeds import seed_every_thing
from ..decorators import Register
from ..auto import (
    # ConfigMixin,
    auto_cls_from_pretrained,
    config_dataclass_wrapper,
    get_version,
)

logger = logging.getLogger(__name__)


_trainer_register = Register('trainer')

register_trainer = _trainer_register.register()


def list_trainers():
    return list(_trainer_register.keys())


def get_trainer_builder(name: str):
    return _trainer_register[name]


@config_dataclass_wrapper(config_name='train_config.json')
@dataclass
class TrainingConfig:
    batch_size: int
    test_batch_size: int = None
    max_epochs: int = None
    max_steps: int = None
    checkpointing_epochs: int = None
    checkpointing_steps: int = None
    validation_epochs: int = None
    validation_steps: int = None
    saving_epochs: int = None
    saving_steps: int = None
    watching_epochs: int = None
    watching_steps: int = None

    def __post_init__(self) -> None:
        if self.test_batch_size is None:
            logger.warning(
                f"`test_batch_size` is None, auto set to `batch_size` ({self.batch_size})."
            )
            self.test_batch_size = self.batch_size
        if (self.max_epochs is None) and (self.max_steps is None):
            logger.warning(
                f"Both `max_epochs` and `max_steps` are None. "
                f"`max_epochs` is automatically set to 10000."
            )
            self.max_epochs = 10000
        elif (self.max_epochs is not None) and (self.max_steps is not None):
            logger.warning(
                f"Both `max_epochs` and `max_steps` are given. "
                f"Training will end when either limit is reached."
            )
        if (self.checkpointing_epochs is None) and (self.checkpointing_steps is None):
            logger.warning(
                f"Both `checkpointing_epochs` and `checkpointing_steps` are None. "
                f"No checkpoints will be saved during the training."
            )
        elif (self.checkpointing_epochs is not None) and (
            self.checkpointing_steps is not None
        ):
            logger.warning(
                f"Both `checkpointing_epochs` and `checkpointing_steps` are given. "
                f"All checkpoints meeting the criteria will be saved."
            )
        if (self.validation_epochs is None) and (self.validation_steps is None):
            logger.warning(
                f"Both `validation_epochs` and `validation_steps` are None. "
                f"No validation will be performed during the training."
            )
        elif (self.validation_epochs is not None) and (
            self.validation_steps is not None
        ):
            logger.warning(
                f"Both `validation_epochs` and `validation_steps` are given. "
                f"All validation meeting the criteria will be performed."
            )
        if (self.saving_epochs is None) and (self.saving_steps is None):
            logger.warning(
                f"Both `saving_epochs` and `saving_steps` are None. "
                f"No states will be saved during the training."
            )
        elif (self.saving_epochs is not None) and (self.saving_steps) is not None:
            logger.warning(
                f"Both `saving_epochs` and `saving_steps` are given. "
                f"All states meeting the criteria will be saved."
            )
        if (self.watching_epochs is None) and (self.watching_steps is None):
            logger.warning(
                f"Both `saving_epochs` and `saving_steps` are None. "
                f"No variables will be saved during the training."
            )
        elif (self.watching_epochs is not None) and (self.watching_steps is not None):
            logger.warning(
                f"Both `saving_epochs` and `saving_steps` are given. "
                f"all variables meeting the criteria will be saved."
            )


@config_dataclass_wrapper(config_name='train_outputfiles.json')
@dataclass
class TrainingOutputFilesManager:
    logging_file: str | os.PathLike = "debug.log"
    version_file: str | os.PathLike = "version.json"
    logging_dir: str | os.PathLike = "logs"
    tensorboard_dir: str | os.PathLike = "tensorboard"
    wandb_dir: str | os.PathLike = "wandb"
    checkpoints_dir: str | os.PathLike = "checkpoints"


@config_dataclass_wrapper(config_name='train_flag.json')
@dataclass
class TrainingFlag:
    step: int = 0
    epoch: int = 0


@dataclass
class TrainingDatasetManager:
    training_dataset: torch.utils.data.Dataset = None
    validation_dataset: torch.utils.data.Dataset = None
    training_dataloader: torch.utils.data.DataLoader = None
    validation_dataloader: torch.utils.data.DataLoader = None


class TrainerMixin(abc.ABC, ConfigMixin):

    config_name = "config.json"
    output_files_manager = TrainingOutputFilesManager()

    def __init__(
        self,
        output_dir: str | os.PathLike,
        project: str,
        name: str,
        seed: int = 0,
    ) -> None:
        super().__init__()
        self._set_seed(seed)
        self.project = project
        self.name = name
        self.output_dir = os.path.join(output_dir, project, name)
        self.writer_dir = os.path.join(output_dir, project)
        self.flag = TrainingFlag()
        self.store_to_log = dict()

    def _set_seed(self, seed: int) -> None:
        self.seed = seed
        seed_every_thing(seed)

    def __post_init__(self) -> None:
        if self.is_local_main_process:
            self.save_config(self.output_dir)
            self.save_version()
            config_dict = self._internal_dict if hasattr(self, "_internal_dict") else {}
            if self.accelerator is not None:
                self.accelerator.init_trackers(
                    project_name=self.project,
                    init_kwargs={
                        "wandb": {
                            "name": self.name,
                            "dir": self.writer_dir,
                            "config": config_dict,
                        }
                    },
                )
        logger.debug("Save config and version.")

    def save_version(self) -> dict:
        version = get_version()
        with open(
            os.path.join(self.output_dir, self.output_files_manager.version_file), "w"
        ) as file:
            json.dump(version, file, indent=2)

    def register_logger(self, logger_config: Dict = {}) -> None:
        os.makedirs(
            os.path.join(self.output_dir, self.output_files_manager.logging_dir),
            exist_ok=True,
        )
        if self.accelerator is not None:
            filename = f"rank{self.accelerator.state.process_index}.{self.output_files_manager.logging_file}"
        else:
            filename = self.output_files_manager.logging_file
        if not self.is_local_main_process:
            logger_config["console_level"] = "CRITICAL"
        init_logger(
            os.path.join(
                self.output_dir, self.output_files_manager.logging_dir, filename
            ),
            **logger_config,
        )

    def register_accelerator(self, accelerator_config: Dict = None) -> None:
        if accelerate is None or accelerator_config is None:
            self.accelerator = None
            self.use_ddp = False
        else:
            self.accelerator = accelerate.Accelerator(**accelerator_config)
            self.use_ddp = True

    def register_training_config(self, training_config: Dict) -> None:
        self.training_config = TrainingConfig(**training_config)

    def register_training_dataset_manager(
        self,
        training_dataset: torch.utils.data.Dataset = None,
        validation_dataset: torch.utils.data.Dataset = None,
        training_dataloader: torch.utils.data.DataLoader = None,
        validation_dataloader: torch.utils.data.DataLoader = None,
    ) -> None:
        self.dataset_manager = TrainingDatasetManager(
            training_dataset,
            validation_dataset,
            training_dataloader,
            validation_dataloader,
        )

    def register_optimizer(self, params: Iterable, optimizer_config: Dict) -> None:
        optimizer_name = optimizer_config.pop("name", "torch.optim.Adam")
        optimizer_cls = get_obj_from_str(optimizer_name)
        self.optimizer = optimizer_cls(params, **optimizer_config)
        logger.debug(f"Load {optimizer_name}.")

    def register_lr_scheduler(self, lr_scheduler_config: Dict) -> None:
        lr_scheduler_name = lr_scheduler_config.pop(
            "name", "torch.optim.lr_scheduler.LambdaLR"
        )
        set_to_max_epoch = lr_scheduler_config.pop("set_to_max_epoch", None)
        set_to_max_iter = lr_scheduler_config.pop("set_to_max_iter", None)
        if set_to_max_epoch is not None:
            lr_scheduler_config[set_to_max_epoch] = self.training_config.max_epochs
        if set_to_max_iter is not None:
            lr_scheduler_config[set_to_max_iter] = self.training_config.max_steps
        lr_scheduler_cls = get_obj_from_str(lr_scheduler_name)
        self.lr_scheduler = lr_scheduler_cls(self.optimizer, **lr_scheduler_config)
        logger.debug(f"Load {lr_scheduler_name}.")

    @property
    def is_local_main_process(self) -> bool:
        if not self.accelerator:
            return True
        return self.accelerator.state.process_index == 0

    def wait_for_everyone(self):
        if self.accelerator is not None:
            self.accelerator.wait_for_everyone()

    def no_ending(self):
        if self.training_config.max_epochs is not None:
            if self.flag.epoch < self.training_config.max_epochs:
                return True
        if self.training_config.max_steps is not None:
            if self.flag.step < self.training_config.max_steps:
                return True
        return False

    @abc.abstractmethod
    def auto_set_to_train_mode(self):
        raise NotImplementedError(
            "Please implement the `auto_set_to_train_mode` method."
        )

    @abc.abstractmethod
    def auto_set_to_eval_mode(self):
        raise NotImplementedError(
            "Please implement the `auto_set_to_eval_mode` method."
        )

    @abc.abstractmethod
    def auto_save_checkpoint(self):
        raise NotImplementedError("Please implement the `auto_save_checkpoint` method.")

    @abc.abstractmethod
    def auto_save_training_status(self):
        raise NotImplementedError(
            "Please implement the `auto_save_training_status` method."
        )

    @abc.abstractmethod
    def auto_validation(self):
        raise NotImplementedError("Please implement the `auto_validation` method.")

    @abc.abstractmethod
    def auto_watching(self):
        raise NotImplementedError("Please implement the `auto_watching` method.")

    @abc.abstractmethod
    def auto_load_status(self, checkpoint_path):
        raise NotImplementedError("Please implement the `auto_load_status` method.")

    @torch.no_grad()
    def _save_checkpoint(self):
        self.wait_for_everyone()
        if self.is_local_main_process:
            self.auto_set_to_eval_mode()
            self.auto_save_checkpoint()
            self.auto_set_to_train_mode()
        self.wait_for_everyone()

    @torch.no_grad()
    def _save_training_status(self):
        self.wait_for_everyone()
        if self.is_local_main_process:
            self.auto_set_to_eval_mode()
            self.auto_save_training_status()
            self.auto_set_to_train_mode()
        self.wait_for_everyone()

    @torch.no_grad()
    def _validation(self):
        self.wait_for_everyone()
        self.auto_set_to_eval_mode()
        self.auto_validation()
        self.auto_set_to_train_mode()
        self.wait_for_everyone()

    @torch.no_grad()
    def _watching(self):
        self.wait_for_everyone()
        if self.is_local_main_process:
            self.auto_set_to_eval_mode()
            self.auto_watching()
            self.auto_set_to_train_mode()
        self.wait_for_everyone()

    @classmethod
    def from_yaml_config(cls, config_path: os.PathLike):
        import yaml

        with open(config_path, "r") as config_file:
            config = yaml.safe_load(config_file)
        return cls.from_config(config)

    @classmethod
    def from_json_config(cls, config_path: os.PathLike):
        import json

        with open(config_path, "r") as config_file:
            config = json.load(config_file)
        return cls.from_config(config)

    @classmethod
    def from_ini_config(cls, config_path: os.PathLike):
        import configparser

        config = configparser.ConfigParser()
        config.read(config_path)
        config = {section: dict(config.items(section)) for section in config.sections()}
        return cls.from_config(config)

    @classmethod
    def from_config_file(cls, config_path: os.PathLike):
        from pathlib import Path

        extension = Path(config_path).suffix.lower()
        if extension in constant.ConfigSuffix.json:
            return cls.from_json_config(config_path)
        if extension in constant.ConfigSuffix.yaml:
            return cls.from_yaml_config(config_path)
        if extension in constant.ConfigSuffix.ini:
            return cls.from_ini_config(config_path)
        raise NotImplementedError(
            f"Unknown suffix '{extension}' in path '{config_path}'."
        )

    @classmethod
    def from_output_dir(cls, dir_path: os.PathLike):
        config_path = os.path.join(dir_path, cls.config_name)
        self = cls.from_config_file(config_path)
        self.auto_load_status()

        logger.info(f"Warm up for epoch={self.flag.epoch} and step={self.flag.step}.")
        if self.flag.step == 0 and self.flag.epoch == 0:
            return self

        expect_epoch = self.flag.step // len(self.dataset_manager.training_dataloader)
        if expect_epoch != self.flag.epoch:
            raise RuntimeError("`current_epoch` and `current_step` mismatch.")

        return self


def register_to_run_one_epoch(only_training: bool = False):

    def one_epoch_func_decorator(one_epoch_func: Callable):

        @functools.wraps(one_epoch_func)
        def run_one_epoch(self: TrainerMixin, *args, **kwargs):
            logger.debug(f"Start Epoch {self.flag.epoch}.")
            result = one_epoch_func(self, *args, **kwargs)
            logger.debug(f"End Epoch {self.flag.epoch}.")

            self.flag.epoch += 1

            if only_training:
                return result

            if self.training_config.checkpointing_epochs is not None:
                if self.flag.epoch % self.training_config.checkpointing_epochs == 0:
                    self._save_checkpoint()

            if self.training_config.saving_epochs is not None:
                if self.flag.epoch % self.training_config.saving_epochs == 0:
                    self._save_training_status()

            if self.training_config.validation_epochs is not None:
                if self.flag.epoch % self.training_config.validation_epochs == 0:
                    self._validation()

            if self.training_config.watching_epochs is not None:
                if self.flag.epoch % self.training_config.watching_epochs == 0:
                    self._watching()

            return result

        return run_one_epoch

    return one_epoch_func_decorator


def register_to_run_one_iteration(only_training: bool = False):

    def one_iteration_func_decorator(one_iteration_func: Callable):

        @functools.wraps(one_iteration_func)
        def run_one_iteration(self: TrainerMixin, *args, **kwargs):
            result = one_iteration_func(self, *args, **kwargs)

            self.flag.step += 1
            if hasattr(self, "iter_process_bar") and self.iter_process_bar is not None:
                self.iter_process_bar.update(1)

            if only_training:
                return result

            if self.training_config.checkpointing_steps is not None:
                if self.flag.step % self.training_config.checkpointing_steps == 0:
                    self._save_checkpoint()

            if self.training_config.saving_steps is not None:
                if self.flag.step % self.training_config.saving_steps == 0:
                    self._save_training_status()

            if self.training_config.validation_steps is not None:
                if self.flag.step % self.training_config.validation_steps == 0:
                    self._validation()

            if self.training_config.watching_steps is not None:
                if self.flag.step % self.training_config.watching_steps == 0:
                    self._watching()

            return result

        return run_one_iteration

    return one_iteration_func_decorator


def auto_trainer_from_pretrained(path: str, **kwargs):

    return auto_cls_from_pretrained(_trainer_register, TrainerMixin, path, **kwargs)
