# Copyright 2024 NetCracker Technology Corporation
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

import re

class UtilsString:

    @staticmethod
    def split_and_trim(input_str):
        # split by newline, comma, or semicolon
        parts = re.split(r'[\n,;]', input_str)
        # trim whitespace from each part
        return [part.strip() for part in parts if part.strip()]

    @staticmethod
    def convert_to_bool(input_str):
        return str(input_str).strip().lower() == "true"
