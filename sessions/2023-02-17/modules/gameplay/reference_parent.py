from pprint import pprint
import random


"""
We added this line to our bash profile:
```
export PYTHONPATH=$PYTHONPATH:/home/calvinl/projects/benj-datsci-tutorials/sessions/2023-02-17/modules
```
and then ran this to re-source our bash profile
```
source ~/.bash_profile

"""
from app import Game

import sys

# it works because we've added this directory
pprint(sys.path)

