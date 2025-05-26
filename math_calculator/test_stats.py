import unittest
from utils.stats import compute_statistics

class TestStats(unittest.TestCase):

    def test_typical_case(self):
        nums = [1, 2, 2, 3, 4]
        result = compute_statistics(nums)
        self.assertEqual(result["середнє"], 2.4)
        self.assertEqual(result["медіана"], 2)
        self.assertEqual(result["мода"], 2)

    def test_no_mode(self):
        nums = [1, 2, 3, 4, 5]
        result = compute_statistics(nums)
        self.assertEqual(result["середнє"], 3)
        self.assertEqual(result["медіана"], 3)
        self.assertEqual(result["мода"], "немає моди")

    def test_even_number(self):
        nums = [10, 20, 30, 40]
        result = compute_statistics(nums)
        self.assertEqual(result["середнє"], 25)
        self.assertEqual(result["медіана"], 25)
        self.assertEqual(result["мода"], "немає моди")

    def test_single_element(self):
        nums = [42]
        result = compute_statistics(nums)
        self.assertEqual(result["середнє"], 42)
        self.assertEqual(result["медіана"], 42)
        self.assertEqual(result["мода"], 42)

if __name__ == '__main__':
    unittest.main()
