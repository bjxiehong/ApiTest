import os
import pytest
from config import Conf
from common.Base import allure_report
from common.Base import send_mail

if __name__ == '__main__':
    report_path = Conf.get_report_path()+os.sep+"result"
    report_html_path = Conf.get_report_path()+os.sep+"html"
    pytest.main(["-s","--alluredir",report_path])
    allure_report(report_path,report_html_path)
    # send_mail(report_html_path,"接口测试结果如下，如有附件请查看附件。","接口测试demo")
