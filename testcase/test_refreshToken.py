from config import Conf
import os
from utils.yamlUtil import YamlReader
import pytest
from config.Conf import ConfigYaml
from utils.RequestsUtil import Request
from utils.AssertUtil import AssertUtil
import allure

# 获取测试用例内容list
# 获取testlogin.yml文件路径
login_test_file = os.path.join(Conf.get_data_path(), "testlogin.yml")
refreshToken_test_file = os.path.join(Conf.get_data_path(), "refreshToken.yml")
# 使用工具类来读取多个文档内容
login_data = YamlReader(login_test_file).data_all()[0]
# print(login_data)
refreshToken_data = YamlReader(refreshToken_test_file).data_all()


@allure.feature("刷新token")
class Test_refreToken():

    def setup_class(self):
        """
        先登录获取refreshToken
        :return:
        """
        url = ConfigYaml().get_conf_url() + login_data["url"]
        data = login_data["data"]
        request = Request()
        res = request.get(url=url, params=data)
        self.gid = res["body"]["data"]["gid"]
        self.refreshToken = res["body"]["data"]["refreshToken"]

    @pytest.mark.parametrize("refreshtoken", refreshToken_data)
    def test_refreshtoken(self, refreshtoken):
        url = ConfigYaml().get_conf_url() + refreshtoken["url"]
        data = refreshtoken["data"]
        case_name = refreshtoken["case_name"]
        allure.dynamic.title(case_name)
        if data["gid"] == "" and data["refreshToken"] == "":
            data["gid"] = str(self.gid)
            data["refreshToken"] = self.refreshToken
        request = Request()
        res = request.get(url=url, params=data)
        print(res)
        assert_res = AssertUtil()
        assert_res.assert_code(res["code"], refreshtoken["except"]["code"])
        assert_res.assert_code(res["body"]["errCode"], refreshtoken["except"]["errCode"])
        assert_res.assert_body(res["body"]["errDesc"], refreshtoken["except"]["errDesc"])


if __name__ == '__main__':
    pytest.main(["-s", "test_refreshToken.py"])
