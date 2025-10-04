# Copyright (c) IBM Corporation
# SPDX-License-Identifier: MIT

import os
import typing

import tuning.sft_trainer
from tuning.config.tracker_configs import (
    TrackerConfigFactory,
)

if typing.TYPE_CHECKING:
    import transformers.trainer_callback


def parse_arguments_and_execute_wrapper(
    callbacks: list["transformers.trainer_callback.TrainerCallback"] | None,
    job_config: dict[str, typing.Any],
):

    parser = tuning.sft_trainer.get_parser()

    (
        model_args,
        data_args,
        training_args,
        trainer_controller_args,
        tune_config,
        file_logger_config,
        _aim_config,
        quantized_lora_config,
        fusedops_kernels_config,
        attention_and_distributed_packing_config,
        _exp_metadata,
    ) = tuning.sft_trainer.parse_arguments(parser, job_config)

    if not os.path.isdir(training_args.output_dir):
        os.makedirs(training_args.output_dir, exist_ok=True)

    combined_tracker_configs = TrackerConfigFactory()

    combined_tracker_configs.file_logger_config = file_logger_config
    combined_tracker_configs.aim_config = None

    return tuning.sft_trainer.train(
        model_args=model_args,
        data_args=data_args,
        train_args=training_args,
        peft_config=tune_config,
        trainer_controller_args=trainer_controller_args,
        tracker_configs=combined_tracker_configs,
        exp_metadata={},
        quantized_lora_config=quantized_lora_config,
        fusedops_kernels_config=fusedops_kernels_config,
        attention_and_distributed_packing_config=attention_and_distributed_packing_config,
        additional_callbacks=callbacks,
    )
