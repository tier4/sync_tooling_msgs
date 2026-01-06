# Copyright 2025 TIER IV, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from typing import TYPE_CHECKING

import pytest
from sync_tooling_msgs.clock_id import parse_clock_id, readable_clock_id

if TYPE_CHECKING:
    from sync_tooling_msgs.clock_id_pb2 import ClockId


@pytest.mark.parametrize(
    "clock_name",
    [
        "sensor_clock_id",
        "sensor_clock_id_namespaced",
        "system_clock_id",
        "linux_clock_id",
        "ptp_clock_id",
        "interface_clock_id",
    ],
)
def test_print_and_parse(clock_name, request):
    clock_id: ClockId = request.getfixturevalue(clock_name)
    assert clock_id == parse_clock_id(readable_clock_id(clock_id))
