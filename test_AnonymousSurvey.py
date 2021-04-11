import unittest
from survey import AnonymousSurvey

class TestAnonymousSurvey(unittest.TestCase):

    """创建一组调查对象和答案"""
    def setUp(self):
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ["English", "Mandarin", "Spanish"]

    """测试输入单个数据能被保存"""
    def test_single_data_stored(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0],self.my_survey.responses)

    """测试输入多个数据能被保存"""
    def test_multiple_data_stored(self):
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response,self.my_survey.responses)


if __name__ == "__main__":
    unittest.main()
