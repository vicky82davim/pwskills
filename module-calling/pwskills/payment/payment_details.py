import os, sys
from os.path import dirname, join, abspath

sys.path.insert(0,abspath(join(dirname(__file__), '..')))

from courses import courses_details
def payment():
    print("This is my payment details")

courses_details.course()