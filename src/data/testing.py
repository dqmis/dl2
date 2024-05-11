"""
This file is only used for testing purposes
"""

from AlgoPuzzleVQA import AlgoPuzzleVQA
from MathVision import MathVision
from rebus import Rebus

a = AlgoPuzzleVQA()
b = MathVision()
c = Rebus()

for value in a.evaluate():
    print(value)
