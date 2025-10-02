#
# Copyright (c) nexB Inc. and others. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
# See http://www.apache.org/licenses/LICENSE-2.0 for the license text.
# See https://github.com/nexB/debian-inspector for support or download.
# See https://aboutcode.org for more information about nexB OSS projects.
#


import json
import shutil
import os.path

from commoncode import testcase


class JsonTester(testcase.FileBasedTesting):
    test_data_dir = os.path.join(os.path.dirname(__file__), "data")

    def check_json(self, results, expected_loc, regen=False, sort=False):
        """
        Test Python native object results against an expected JSON
        file at expected_loc.
        """
        expected_loc = self.get_test_loc(expected_loc, must_exist=False)

        if regen:
            regened_exp_loc = self.get_temp_file()
            with open(regened_exp_loc, "w") as ex:
                json.dump(results, ex, indent=2, separators=(",", ": "))

            expected_dir = os.path.dirname(expected_loc)
            if not os.path.exists(expected_dir):
                os.makedirs(expected_dir)
            shutil.copy(regened_exp_loc, expected_loc)

        with open(expected_loc, "rb") as ex:
            expected = json.load(ex)
        if sort:
            assert sorted(results) == sorted(expected)
        else:
            assert json.dumps(results, indent=2) == json.dumps(expected, indent=2)

    def check_file(self, results, expected_loc, regen=False, sort=False):
        """
        Test results text string against an expected file at
        expected_loc.
        """
        expected_loc = self.get_test_loc(expected_loc)

        if regen:
            regened_exp_loc = self.get_temp_file()
            with open(regened_exp_loc, "w") as ex:
                ex.write(results)

            expected_dir = os.path.dirname(expected_loc)
            if not os.path.exists(expected_dir):
                os.makedirs(expected_dir)
            shutil.copy(regened_exp_loc, expected_loc)

        with open(expected_loc, "rb") as ex:
            expected = ex.read()
            expected = expected.decode("utf-8")
        if sort:
            assert sorted(results.splitlines()) == sorted(expected.splitlines())
        else:
            assert results == expected
