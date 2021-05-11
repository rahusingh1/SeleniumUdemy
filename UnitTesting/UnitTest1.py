import unittest  # python has in-build library/module for unit test
from Pyunit1 import Example


# we can create class of any name but the value in bracket should be same as below.
# it means that we are inheriting from unit test module, TestCase class.
# and inside this class we can create any no of functions or methods.
class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("This will run once before all the methods")
    @classmethod
    def tearDownClass(cls):
        print("This will run once after all the methods")

    # methods in unit test
    def setUp(self):
        print("This will run before every method")

    # method to teardown after running the method
    def tearDown(self):
        print("This will run after every method")


    def test_add(self):
        self.assertEqual(Example.add(self, 10,20), 30)
        self.assertEqual(Example.add(self, 0, 0), 0)
        self.assertEqual(Example.add(self, -1, 1), 0)

    def test_sub(self):
        result = Example.sub(self, 20, 10)
        self.assertEqual(result, 10)

# function name should start from test_   then only compiler will recognize that it is a test else not.
#     def test_something(self):
#         self.assertEqual(True, False)

# we need the following command to run this from command line directly with the name
# else to run it in terminal we need to use flag "python3 -m unittest filename.py"
    if __name__ == '__main__':
        unittest.main()
