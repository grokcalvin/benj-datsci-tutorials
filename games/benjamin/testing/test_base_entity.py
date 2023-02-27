import sys
from pathlib import Path
import unittest

# A Hacky way to add your "package" to the system python path
game_dir = Path(__file__).parent.parent / "genetics_txt"
sys.path.append(str(game_dir))
from base_entity import increase_muscle_group


class TestGeneticsTXTBaseEntity(unittest.TestCase):
    def test_increase_muscle_group(self):
        input_test_data = [
            (1.5, 10),
            (1.0, 5),
            (2.0, 10),
            (2.0, 1),
        ]
        expected_results = [
            (2, 3),
            (1, 2),
            (2, 3),
            (2, 3),
            (2, 2),
        ]

        for (muscle_group, level), (min_value, max_value) in zip(input_test_data, expected_results):
            actual_result = increase_muscle_group(
                muscle_group=muscle_group,
                level=level
            )
            self.assertGreaterEqual(actual_result, min_value)
            self.assertLessEqual(actual_result, max_value)


if __name__ == '__main__':
    unittest.main()
