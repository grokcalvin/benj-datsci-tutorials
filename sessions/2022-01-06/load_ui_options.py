import yaml
from pathlib import Path
from typing import Union
from pprint import pprint

print(__file__)

module_dir = Path(__file__).parent

ui_option_file = module_dir / "ui_options.yml"

with ui_option_file.open("r") as f:
    ui_options = yaml.safe_load(f)
    pprint(ui_options)


# get your combat options (system decides based on environment)
environment = 'dungeon'

combat_option = ui_options['combat'][environment]
print(combat_option)


# get your combat options (system decides based on environment)
environment = 'open'

combat_option = ui_options['combat'][environment]
print(combat_option)