from package_sorter import PackageSorter
import unittest

class TestPackageSorter(unittest.TestCase):
    def setUp(self):
        self.sut = PackageSorter()
    def test_standard_weight(self):
        result = self.sut.sort_package(20, 20, 20, 10)
        self.assertEqual(result, PackageSorter.STANDARD, "Should be STANDARD")

    def test_special_heavy(self):
        result = self.sut.sort_package(10, 10, 10, 20)
        self.assertEqual(result, PackageSorter.SPECIAL, "Should be SPECIAL")

    def test_special_volume(self):
        result = self.sut.sort_package(100, 100, 100, 10)
        self.assertEqual(result, PackageSorter.SPECIAL, "Should be SPECIAL")

    def test_special_dimension(self):
        result = self.sut.sort_package(150, 10, 10, 10)
        self.assertEqual(result, PackageSorter.SPECIAL, "Should be SPECIAL") 

    def test_rejected(self):
        result = self.sut.sort_package(150, 10, 10, 3000)
        self.assertEqual(result, PackageSorter.REJECTED, "Should be REJECTED")  
    
    def test_negative_dimension(self):
        with self.assertRaises(ValueError):
            self.sut.sort_package(-10, 10, 10, 3000)

    def test_zero_dimension(self):
        with self.assertRaises(ValueError):
            self.sut.sort_package(10, 10, 0, 3000)

    def test_negative_mass(self):
        with self.assertRaises(ValueError):
            self.sut.sort_package(10, 10, 10, -1)

    def test_zero_mass(self):
        with self.assertRaises(ValueError):
            self.sut.sort_package(10, 10, 10, 0)

if __name__ == "__main__":
    unittest.main()