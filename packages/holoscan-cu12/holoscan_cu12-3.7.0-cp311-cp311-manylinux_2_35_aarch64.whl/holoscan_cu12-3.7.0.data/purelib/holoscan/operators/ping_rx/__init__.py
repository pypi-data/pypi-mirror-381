"""
SPDX-FileCopyrightText: Copyright (c) 2022-2024 NVIDIA CORPORATION & AFFILIATES. All rights reserved.
SPDX-License-Identifier: Apache-2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""  # noqa: E501

from holoscan.core import Operator, OperatorSpec


class PingRxOp(Operator):
    """Simple receiver operator.

    This is an example of a native operator with one input port.
    On each tick, it receives an integer from the "in" port.

    **==Named Inputs==**

        in : any
            A received value.
    """

    def __init__(self, fragment, *args, **kwargs):
        # Need to call the base class constructor last
        super().__init__(fragment, *args, **kwargs)

    def setup(self, spec: OperatorSpec):
        spec.input("in")

    def compute(self, op_input, op_output, context):
        value = op_input.receive("in")
        print(f"Rx message value: {value}")


__all__ = ["PingRxOp"]
