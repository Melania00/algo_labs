import unittest
from src.beers import Beer

class TestBeerClass(unittest.TestCase):
    def setUp(self):
        self.employees = {
            1: [1],
            2: [1, 4],
            3: [1],
            4: [1, 2, 4],
            5: [1, 2],
            6: [2],
            7: [1, 2, 3],
            8: [2, 3, 4],
            9: [3, 4],
            10: [3, 4]
        }
        self.beer_manager = Beer(self.employees)

    def test_find_most_popular_beer(self):
        popular = self.beer_manager.find_popular_beer()
        self.assertEqual(popular, 1)

    def test_remove_satisfied_employees(self):
        self.beer_manager.find_popular_beer()
        remaining_employees = self.beer_manager.remove_satisfied_employees()


if __name__ == '__main__':
    unittest.main()
