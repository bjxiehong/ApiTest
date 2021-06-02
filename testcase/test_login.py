from config import Conf
import os
from utils.yamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from utils.AssertUtil import AssertUtil
import allure
from common.Base import allure_report

# 获取测试用例内容list
# 获取testlogin.yml文件路径
test_file = os.path.join(Conf.get_data_path(), "testlogin.yml")
# 使用工具类来读取多个文档内容
data_list = YamlReader(test_file).data_all()


# 参数化执行测试用例
@allure.feature("游客登录")
class TestLogin:
    @pytest.mark.parametrize("login", data_list)
    def test_yml(self, login):
        # 初始化URL,data
        url = ConfigYaml().get_conf_url() + login["url"]
        data = login["data"]
        # header = login["header"]
        print(data)
        case_name = login["case_name"]
        allure.dynamic.title(case_name)
        allure.dynamic.description("请求body==>> %s" % str(data))
        request = Request()
        res = request.get(url=url, params=data)
        # print(res)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], login["except"]["code"])
        assert_res.assert_code(res["body"]["errCode"], login["except"]["errCode"])
        assert_res.assert_body(res["body"]["errDesc"], login["except"]["errDesc"])


if __name__ == '__main__':
    # report_path = Conf.get_report_path()+os.sep+"result"
    # report_html_path = Conf.get_report_path()+os.sep+"html"
    pytest.main(["-s", "test_login.py", "--alluredir", "./report/result"])
    # allure_report(report_path,report_html_path)
