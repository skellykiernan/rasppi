import unittest
from mock import MagicMock

#~### Very simple method

# Replace function going to mock
func_to_mock = MagicMock(return_value=3)
func_to_mock(3, 4, 5, key='value')
func_to_mock.assert_called_with(3, 4, 5, key='value')

#~### A bit more with plus mocking an internal function call
def test_func(value):
    """ test_func to demo that a mocking an internal function call """
    incremented_value = inner_increment(value)
    return incremented_value

class MockExampleTest(unittest.TestCase):
    """docstring for MockExampleTest"""

    def test_mock_func_example(self):
        """docstring for test_Simple"""
        input_value    = 3
        expected_value = 4
        # Mock a function that shall be called during the test function
        # need to be careful of scoping rules here
        global inner_increment
        inner_increment = MagicMock(return_value=4)
        # call under test
        ret_value  = test_func(input_value)

        # check that the mock was called as expected
        inner_increment.assert_called_with(3)
        self.assertEqual(ret_value, expected_value)

#~### Start of Execution
if __name__ == '__main__':
        unittest.main()
