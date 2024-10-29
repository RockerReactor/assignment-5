# =========================================================================
#
#  Copyright Ziv Yaniv
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0.txt
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# =========================================================================

import pytest
import numpy as np

from bubble_sort import bubble_sort
from insertion_sort import insertion_sort
from quick_sort import quick_sort


def is_sorted(int_list):
    for i in range(len(int_list) - 1):
        if not int_list[i] <= int_list[i + 1]:
            return False
    return True


@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3, 2, 1], [1, 1, 1]] + [
        np.random.randint(low=-10, high=200, size=20) for i in range(1000)
    ]


def test_bubble(int_lists):
    for list_key in int_lists:
        s_list = bubble_sort(list_key)
        assert is_sorted(s_list)


def test_quick(int_lists):
    for list_key in int_lists:
        s_list = quick_sort(list_key)
        assert is_sorted(s_list)


def test_insertion(int_lists):
    for list_key in int_lists:
        s_list = insertion_sort(list_key)
        assert is_sorted(s_list)
