#
#  Copyright 2024 The InfiniFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
from abc import ABC
from agent.component.base import ComponentBase, ComponentParamBase


class TestCpnParam(ComponentParamBase):
    def __init__(self):
        super().__init__()
        self.test_in = "test_input"


class TestCpn(ComponentBase, ABC):
    component_name = "TestCpn"

    def _run(self, history, **kwargs):
        ans = self.get_input()
        ans = ",".join(ans["content"]) if "content" in ans else ""
        return TestCpn.be_output(self._param.test_in)

