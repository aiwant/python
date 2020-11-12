import pymysql

db = pymysql.connect(   #数据库连接
	host="localhost",
	user="root",
	password="08981742lt",
	port=3306,
	database="python",
	charset="utf8"
	)

cursor = db.cursor()  #创建游标

#如果数据表已存在使用execute()方法删除表
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

#创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
			FIRST_NAME CHAR(20) NOT NULL,
			LAST_NAME CHAR(20),
			AGE INT,
			SEX CHAR(1),
			INCOME FLOAT)"""

#执行sql语句
cursor.execute(sql)