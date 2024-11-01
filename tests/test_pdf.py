import unittest
from pathlib import Path
from parameterized import parameterized


TEST_DATA_DIR = Path(__file__).parent / 'data'


def load_pdf():
    ...


class TestPdfToBraille(unittest.TestCase):

    @parameterized.expand(load_pdf)
    def test_encoder(self, content: list[str], expected: list[int]):
        # test something
        unittest.skip()
