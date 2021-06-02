import logging
from config import Conf
from config.Conf import ConfigYaml
import datetime, os

# 定义日志级别
log_l = {
    "info": logging.INFO,
    "debug": logging.DEBUG,
    "warning": logging.WARNING,
    "error": logging.ERROR
}


# 封装Log工具类
# 1.创建类
class Logger:
    # 2.定义参数
    def __init__(self, log_file, log_name, log_level):
        self.log_file = log_file  # 扩展名 配置文件
        self.log_name = log_name
        self.log_level = log_level

        # 3.编写输出控制台或文件
        # 1.设置logger名称
        self.logger = logging.getLogger(self.log_name)
        # 2.设置log级别
        self.logger.setLevel(log_l[self.log_level])
        # 判断handler是否存在
        if not self.logger.handlers:
            # 3.输出控制台
            fh_stream = logging.StreamHandler()
            fh_stream.setLevel(log_l[self.log_level])
            formatter = logging.Formatter('%(asctime)s %(name)s %(lineno)s %(levelname)s %(message)s')
            fh_stream.setFormatter(formatter)
            # 写入文件
            fh_file = logging.FileHandler(self.log_file)
            fh_file.setLevel(log_l[self.log_level])
            fh_file.setFormatter(formatter)
            # 6.添加handler
            self.logger.addHandler(fh_stream)
            self.logger.addHandler(fh_file)


# 1.初始化参数数据
# 日志文件名称，日志文件级别
# 日志文件名称 = logs目录 + 当前时间 + 扩展名
# log目录
log_path = Conf.get_log_path()
# 当前时间
current_time = datetime.datetime.now().strftime("%Y-%m-%d")
log_extension = ConfigYaml().get_conf_log_extension()
logfile = os.path.join(log_path, current_time + log_extension)
# print(logfile)
# 日志文件级别
loglevel = ConfigYaml().get_conf_log()


# print(loglevel)
# 2.对外方法，初始logg工具类，提供其他类使用
def my_log(log_name=__file__):
    return Logger(log_file=logfile, log_name=log_name, log_level=loglevel).logger


if __name__ == '__main__':
    my_log().debug("this is debug")
