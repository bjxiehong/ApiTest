import os
from utils.yamlUtil import YamlReader

# 1、获取项目基本目录
# 获取当前项目的绝对路径
current = os.path.abspath(__file__)
# print(current)
BASE_DIR = os.path.dirname(os.path.dirname(current))
# print(BASE_DIR)
# 定义config目录路径
_config_path = BASE_DIR + os.sep + "config"
# 定义data目录路径
_data_path = BASE_DIR + os.sep + "data"
# 定义conf.yml文件路径
_config_file = _config_path + os.sep + "conf.yml"
# 定义db_config.yml文件路径
_db_config_file = _config_path + os.sep + "db_conf.yml"
# 定义log文件路径
_log_path = BASE_DIR + os.sep + "logs"
# 定义report目录路径
_report_path = BASE_DIR + os.sep + "report"


# print(_report_path)


def get_db_config_file():
    return _db_config_file


def get_config_path():
    return _config_path


def get_config_file():
    return _config_file


def get_log_path():
    return _log_path


def get_data_path():
    return _data_path


def get_report_path():
    return _report_path


# 2、读取配置文件
class ConfigYaml:
    # 初始yaml读取配置文件
    def __init__(self):
        self.config = YamlReader(get_config_file()).data()
        self.db_config = YamlReader(get_db_config_file()).data()

    def get_conf_url(self):
        """
        获取测试的服务的配置信息
        :return:
        """
        return self.config["BASE"]["test"]["url"]

    def get_conf_log(self):
        return self.config["BASE"]["log_level"]

    def get_conf_log_extension(self):
        return self.config["BASE"]["log_extension"]

    def get_db_config_info(self, db_alias):
        """
        根据db_alias获取该名称下的数据库信息
        :param db_alias:
        :return:
        """
        return self.db_config[db_alias]

    def get_email_info(self):
        """
        获取email配置信息
        :return:
        """
        return self.config["email"]


if __name__ == '__main__':
    conf_read = ConfigYaml()
    # print(conf_read.get_conf_url())
    # print(conf_read.get_conf_log())
    # print(conf_read.get_conf_log_extension())
    # print(conf_read.get_db_config_info("db_1"))
    print(conf_read.get_email_info())
