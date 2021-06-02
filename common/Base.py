from config.Conf import ConfigYaml
from utils.MysqlUtil import Mysql
from utils.LogUtil import my_log
import subprocess
from config.Conf import ConfigYaml
from utils.EmailUtil import SendEmail

log = my_log()


def init_db(db_alias):
    db_info = ConfigYaml().get_db_config_info(db_alias)
    host = db_info["db_host"]
    user = db_info["db_user"]
    password = db_info["db_password"]
    db_name = db_info["db_name"]
    # charset = db_info["db_charset"]
    port = int(db_info["db_port"])

    conn = Mysql(host, user, password, db_name, port)
    print(conn)
    return conn


def allure_report(report_path, report_html):
    """
    生成allure报告
    :param report_path:
    :param report_html:
    :return:
    """
    # 执行命令 allure generate
    allure_cmd = "allure generate %s -o %s --clean" % (report_path, report_html)
    log.info("报告地址")
    try:
        subprocess.call(allure_cmd, shell=True)
    except:
        log.error("执行用例失败，请检查测试环境相关配置")
        raise


def send_mail(report_html_path="", content="", title="测试"):
    """
    发送邮件
    :param report_html_path:
    :param content:
    :param title:
    :return:
    """

    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(smtp_addr=smtp_addr,
                      username=username,
                      password=password,
                      recv=recv,
                      title=title,
                      content=content,
                      file=report_html_path)
    email.send_mail()


if __name__ == '__main__':
    init_db("db_1")
