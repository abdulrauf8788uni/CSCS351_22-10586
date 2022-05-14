import unittest
import project

class TestProject(unittest.TestCase):

	def test_area(self):
		self.assertEqual(project.area(4), 50.27)
		self.assertEqual(project.area(0), 0)
		self.assertEqual(project.area(10), 314.16)


	def test_circumference(self):
		self.assertEqual(project.circumference(7), 43.98)
		self.assertEqual(project.circumference(0), 0)
		self.assertEqual(project.circumference(12), 75.4)

	def test_is_even(self):
		self.assertEqual(project.is_even(4), True)
		self.assertEqual(project.is_even(0), True)
		self.assertEqual(project.is_even(7), False)

	def test_is_vowel(self):
		self.assertEqual(project.is_vowel("z"), False)
		self.assertEqual(project.is_vowel("o"), True)
		self.assertEqual(project.is_vowel("y"), False)

	def test_inches_to_cm(self):
		self.assertEqual(project.inches_to_cm(1), 2.54)
		self.assertEqual(project.inches_to_cm(12), 30.48)
		self.assertEqual(project.inches_to_cm(7.4), 18.8)



if __name__ == "__main__":
	unittest.main()