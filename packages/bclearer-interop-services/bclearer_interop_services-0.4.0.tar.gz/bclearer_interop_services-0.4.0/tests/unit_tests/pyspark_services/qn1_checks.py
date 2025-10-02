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

import unittest

import pandas as pd


class SampleTests(unittest.TestCase):

    def test_qn1_count(self):
        pdf = pd.read_csv(
            "data/baby_names.csv"
        )
        self.assertEqual(
            len(pdf),
            87899,
            "The output should have 87899 rows in total",
        )

    def test_qn1_format(self):
        with open(
            "data/baby_names.csv"
        ) as f:
            self.assertEqual(
                f.readline().strip(),
                "sid,id,position,created_at,created_meta,updated_at,updated_meta,meta,year,first_name,county,sex,count",
            )
            self.assertEqual(
                f.readline().strip(),
                "row-brkm-7izk-trjm,00000000-0000-0000-4F52-2DEB83640FD1,0,1611674742,,1611674742,,{ },2018,OLIVIA,Albany,F,17",
            )

    def test_qn1_function_declarations(
        self,
    ):
        try:
            from qn1 import (
                read_json_and_flatten_data,
            )
        except ImportError:
            self.fail(
                "The function read_json_and_flatten_data does not exist. Do not modify the function declarations."
            )
        try:
            from qn1 import (
                parse_dataframe_with_schema,
            )
        except ImportError:
            self.fail(
                "The function parse_dataframe_with_schema does not exist. Do not modify the function declarations."
            )
