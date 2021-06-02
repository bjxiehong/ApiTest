import yagmail


class SendEmail:
    def __init__(self, smtp_addr, username, password, recv, title, content=None, file=None):
        self.smtp_addr = smtp_addr
        self.username = username
        self.password = password
        self.recv = recv
        self.title = title
        self.content = content
        self.file = file

    def send_mail(self):
        yag = yagmail.SMTP(user=self.username, password=self.password, host=self.smtp_addr)
        yag.send(self.recv, self.title, self.content, self.file)


if __name__ == '__main__':
    from config.Conf import ConfigYaml

    email_info = ConfigYaml().get_email_info()
    smtp_addr = email_info["smtpserver"]
    username = email_info["username"]
    password = email_info["password"]
    recv = email_info["receiver"]
    email = SendEmail(smtp_addr=smtp_addr, username=username,
                      password=password, recv=recv,
                      title="测试", content="这是一个测试内容！！！！",
                      file="./report/html/index.html")
    email.send_mail()
