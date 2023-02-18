from pprint import pprint
import random


# this won't work
try:
    from app import Game
except ModuleNotFoundError:
    print("Doesn't Work")


# Hacky solution!!
import sys
from pathlib import Path


def get_module_directory():
    # get the parent directory
    print(__file__)
    print(Path(__file__).parent.parent)
    package_dir = Path(__file__).parent.parent
    return str(package_dir)

module_dir = get_module_directory()
print("--------This is how sys.path is before we touch it---------------")
pprint(sys.path)
sys.path.append(module_dir)
print("--------We've now added our package_dir string to sys.path--------------")
pprint(sys.path)
# This now works!  But it's hacky
from app import Game
