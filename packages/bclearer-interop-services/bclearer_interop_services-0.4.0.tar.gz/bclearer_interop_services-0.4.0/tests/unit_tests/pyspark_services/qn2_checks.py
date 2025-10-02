import inspect
import io
import os
import sys

currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe()
        )
    )
)
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import re
import subprocess
import unittest


def run_main():
    subprocess.run(
        ["python3", "main.py"]
    )


class TestingSuite(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        run_main()

    def test_correct_format(self):
        with open(
            "data/output.txt", "r"
        ) as outf:
            partA = outf.readline()
            partB = outf.readline()
            partC = outf.readline()
            partD = outf.readline()

        self.assertIsNotNone(
            re.match(
                r"records=(\d+)", partA
            ),
            "partA should be in the format of records=<number>",
        )

        self.assertIsNotNone(
            re.match(
                r"county=(\w+),\s+avgVisitors=(\d+(?:\.\d+)?)",
                partB,
            ),
            "partB should be in the format of county=<number>, avgVisitors=<number>",
        )

        self.assertIsNotNone(
            re.match(
                r"avgVisitorAge=(\d+(?:\.\d+)?)",
                partC,
            ),
            "partA should be in the format of avgVisitorAge=<number>",
        )

        self.assertIsNotNone(
            re.match(
                r"mostCommonBirthAge=(\d+),\s+count=(\d+)",
                partD,
            ),
            "partD should be in the format of mostCommonBirthAge=<number>, count=<number>",
        )
