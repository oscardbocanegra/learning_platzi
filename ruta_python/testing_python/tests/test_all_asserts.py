import unittest

SERVER="server_b"

class AllAssertsTests(unittest.TestCase):
    """
    Unit tests demonstrating various assert methods in unittest.
    
    Methods
    -------
    test_assert_equal():
        Tests that two values are equal.
    
    test_assert_true_or_false():
        Tests that a value is True and another value is False.
    
    test_assert_raises():
        Tests that a ValueError is raised when converting a non-numeric string to an integer.
    
    test_assert_in():
        Tests that a value is in a list and another value is not in a list.
    
    test_assert_dicts():
        Tests that two dictionaries are equal.
    """
    
    def test_assert_equal(self):
        self.assertEqual(10, 10)
        self.assertEqual("Hola", "Hola")

    def test_assert_true_or_false(self):
        self.assertTrue(True)
        self.assertFalse(False)

    def test_assert_raises(self):
        with self.assertRaises(ValueError):
            int("no_soy_un_numero")

    def test_assert_in(self):
        self.assertIn(10, [2, 4, 5, 10])
        self.assertNotIn(5, [2, 4, 10])

    def test_assert_dicts(self):
        user = {"first_name": "Luis", "last_name": "Martinez"}
        self.assertDictEqual(
            {"first_name": "Luis", "last_name": "Martinez"},
            user
        )
        self.assertSetEqual(
            {1, 2, 3},
            {1, 2, 3}
        )

    @unittest.skip("Trabjo en progreso, será habilitada nuevamente")
    def test_skip(self):
        self.assertEqual("hola", "chao")

    @unittest.skipIf(SERVER == "server_b", "Saltado porque no estamos en el servidor")
    def test_skip_if(self):
        self.assertEqual(100, 100)

    @unittest.expectedFailure
    def test_expected_failure(self):
        self.assertEqual(100, 150)