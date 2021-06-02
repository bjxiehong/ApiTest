import pymysql
from utils.LogUtil import my_log


class Mysql:
    def __init__(self, host, user, password, database, port=3306):
        self.log = my_log()
        try:
            self.conn = pymysql.connect(
                host=host,
                user=user,
                password=password,
                database=database,
                # charset=charset,
                port=port
            )
            self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)  # 返回结果一字典方式展示
        except Exception as e:
            self.log.error(e)

    def fetchone(self, sql):
        """
        查询单个
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchone()

    def fetchall(self, sql):
        """
        查询单个
        :param sql:
        :return:
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def exec(self, sql):
        """
        执行
        :return:
        """
        try:
            if self.conn and self.cursor:
                self.cursor.execute(sql)
                self.conn.commit()
        except Exception as e:
            self.conn.rollback()
            self.log.error("Mysql 执行失败")
            self.log.error(e)
            return False
        return True

    def __del__(self):
        """
        关闭对象
        :return:
        """
        if self.cursor is not None:
            self.cursor.close()
        if self.conn is not None:
            self.conn.close()


if __name__ == '__main__':
    sql = Mysql("127.0.0.1", "root", "xiehong@123", "lianbiao")
