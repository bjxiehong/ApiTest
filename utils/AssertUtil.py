"""
断言封装
"""
from utils.LogUtil import my_log
import json


class AssertUtil:
    def __init__(self):
        self.log = my_log("AssertUtil")

    def assert_code(self, code, excepted_code):
        """
         断言code相等
        :param code:
        :param excepted_code:
        :return:
        """
        try:
            assert int(code) == int(excepted_code)
            return True
        except:
            self.log.error("code error,code is %s,except_code is %s" % (code, excepted_code))
            raise

    def assert_body(self, body, excepted_body):
        """
        验证返回结果内容相等
        :param body:
        :param except_body:
        :return:
        """
        try:
            assert body == excepted_body
            return True
        except:
            self.log.error("body error,body is %s,except_body is %s" % (body, excepted_body))
            raise

    def assert_in_body(self, body, excepted_body):
        """
        验证返回结果是否包含期望的结果
        :param body:
        :param except_body:
        :return:
        """
        try:
            body = json.dumps(body)
            assert excepted_body in body
            return True
        except:
            self.log.error("不包含或者body错误，body is %s,excepted_body is %s" % (body, excepted_body))
            raise
