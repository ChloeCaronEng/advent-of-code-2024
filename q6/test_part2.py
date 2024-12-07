import unittest
from part2 import main

class TestMain(unittest.TestCase):
    
    def test_main_small(self):
        input_string = "....#.....\n.........#\n..........\n..#.......\n.......#..\n..........\n.#..^.....\n........#.\n#.........\n......#..."
        expected_result = 6
        
        result = main(input_string)
        
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()