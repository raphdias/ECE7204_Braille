"""
String -> bits
 """

from dataclasses import dataclass


# Intake char information and output bytes using the lookup table
@dataclass
class Decoder:
    input: list[str]
    output: list[int] | None

    def generate_output():
        ...
