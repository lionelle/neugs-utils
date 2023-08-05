
import unittest
from gradescope_utils.autograder_utils.decorators import number
from neugs_utils.context_managers import Capturing
from neugs_utils import tier, COMMON_ONE, COMMON_TWO, COMMON_THREE, common_msg, strip_prompts
from neugs_utils.common_tests import check_style


student_files = [] # setup incase there are more than one import section

try:
    import IslandGrid
    student_files += ['IslandGrid.py']
except ImportError:
    try:
        import src.IslandGrid as IslandGrid
        student_files += ['src/IslandGrid.py']
    except ImportError:
        pass


# Double check class name, remember unit tests likes it to start with Test
class TestIslandGrid(unittest.TestCase):
    @tier(COMMON_ONE) ## mastery grading first tier
    @number("1.0")
    def test_can_move_north(self):
        """Test add function with multiple inputs""" 
        self.assertEqual(IslandGrid.can_move_north([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 1), True)
        self.assertEqual(IslandGrid.can_move_north([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 1, 2), False)
        self.assertEqual(IslandGrid.can_move_north([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 1), True)

    @tier(COMMON_ONE) ## mastery grading first tier
    @number("1.1")
    def test_can_move_south(self):
        """Test subtract function with multiple inputs""" 
        self.assertEqual(IslandGrid.can_move_south([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 1), False)
        self.assertEqual(IslandGrid.can_move_south([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 1, 2), True)
        self.assertEqual(IslandGrid.can_move_south([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 2), False)

    @tier(COMMON_TWO) ## mastery grading second tier
    @number("2.0")
    def test_can_move_west(self):
        """Test multiply function with multiple inputs""" 
        self.assertEqual(IslandGrid.can_move_west([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 1), False)
        self.assertEqual(IslandGrid.can_move_west([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 1, 2), True)
        self.assertEqual(IslandGrid.can_move_west([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 2), True)

    @tier(COMMON_TWO)
    @number("2.1")
    def test_can_move_east(self):
        """Test divide function with multiple inputs""" 
        self.assertEqual(IslandGrid.can_move_east([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 1), True)
        self.assertEqual(IslandGrid.can_move_east([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 1), False)
        self.assertEqual(IslandGrid.can_move_east([[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]], 2, 2), False)

    @tier(COMMON_THREE)
    @number("3.0")
    def test_select_function(self)-> None:
        """Tests to make sure the right function is returned based on the string entered. Multiple strings entered"""
        self.assertEqual(IslandGrid.select_function("N"), IslandGrid.can_move_north)
        self.assertEqual(IslandGrid.select_function("S"), IslandGrid.can_move_south)
        self.assertEqual(IslandGrid.select_function("W"), IslandGrid.can_move_west)
        self.assertEqual(IslandGrid.select_function("E"), IslandGrid.can_move_east)


if __name__ == '__main__':
    unittest.main()
