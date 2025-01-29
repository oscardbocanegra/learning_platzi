import unittest

class AllAssertsTests(unittest.TestCase):

    def test_assert_equal(self):
        self.assertEqual(1, 1)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(1 == 1)
        self.assertFalse(1 == 2)