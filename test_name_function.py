import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    #测试name.function

    def test_first_last_name(self):
        #能够正确处理想 Jack July 这样的名字嘛
        formatted_name = get_formatted_name("Jack","July")
        self.assertEqual(formatted_name,"Jack July")

    def test_first_middle_last_name(self):
        # 能够正确处理想 Jack D July 这样的名字嘛
        formatted_name = get_formatted_name("Jack", "July", "D")
        self.assertEqual(formatted_name, "Jack D July")

if __name__ == "__main__":  #两个_ 才是 __
    unittest.main()