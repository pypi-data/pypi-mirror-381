# SPDX-FileCopyrightText: Copyright (c) 2025 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# Original Copyright 2025 LiveCodeBench
# For the original license and copyright information, see the LICENSE file in this repository.

import numpy as np
import json
from livecodebench.benchmarks import load_generation_dataset, CodeGenerationProblem
from livecodebench.evaluation import codegen_metrics


dataset = load_generation_dataset()

dataset = sorted(dataset, key=lambda x: x.question_id)


def check_model(model_key):
    path = f"/home/naman/Repos/LiveCodeBench/run_models_outputs/{model_key}/chat_0.2_checked.json"
    with open(path) as f:
        old_results = json.load(f)
    old_results = sorted(old_results, key=lambda x: x["question_id"])
    assert old_results[0]["question_id"] == dataset[0].question_id

    def debug(idx):
        codegen_metrics(
            [dataset[idx].get_evaluation_sample()],
            [old_results[idx]["code_list"][:1]],
            debug=True,
        )

    def run(idx):
        return codegen_metrics(
            [dataset[idx].get_evaluation_sample()],
            [old_results[idx]["code_list"]],
        )

    debug(380)
    exit()
    # debug(196)
    # debug(352)

    metrics = codegen_metrics(
        [d.get_evaluation_sample() for d in dataset],
        [r["code_list"] for r in old_results],
        num_process_evaluate=12,
    )
    old_pass1 = np.mean([np.mean(r["pass1_list"]) for r in old_results])

    print(old_pass1)
    print(metrics[0]["pass@1"])

    for idx in range(400):
        old_pass1 = np.mean(old_results[idx]["pass1_list"])
        new_pass1 = metrics[0]["detail"]["pass@1"][idx]
        if not abs(old_pass1 - new_pass1) < 1e-4:
            print(idx, old_pass1, new_pass1)


# model_key = "GPT-4-Turbo-1106"
# check_model(model_key)

model_key = "Claude-3-Opus"
check_model(model_key)

model_key = "GPT-4-0613"
check_model(model_key)

model_key = "Mistral-Large"
check_model(model_key)

model_key = "Claude-3-Sonnet"
check_model(model_key)

model_key = "GPT-3.5-Turbo-0301"
check_model(model_key)

model_key = "Gemini-Pro"
check_model(model_key)
