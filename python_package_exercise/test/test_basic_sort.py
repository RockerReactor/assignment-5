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

from sort_lib import bubble_sort
from sort_lib import insertion_sort
from sort_lib import quick_sort



def is_sorted(self, int_list):
    """
    Testing oracle.
    """
    return True

@pytest.fixture
def int_lists():
    # fixture which creates testing data for all tests
    return [[3,2,1],
	        [1,1,1],
			np.random.randint(low=-10, high=200, size=5)] 
    
def test_bubble(int_lists):
    for list_key in range(int_lists):
        s_list = bubble_sort(int_lists[list_key])
        for i in range(len(s_list)-1):
            assert s_list[i]<s_list[i+1]


def test_quick(int_lists):
     for list_key in range(int_lists):
        s_list = quick_sort(int_lists[list_key])
        for i in range(len(s_list)-1):
            assert s_list[i]<s_list[i+1]

def test_insertion(int_lists):
    for list_key in range(int_lists):
        s_list = insertion_sort(int_lists[list_key])
        for i in range(len(s_list)-1):
            assert s_list[i]<s_list[i+1]
