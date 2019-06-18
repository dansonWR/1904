import pymysql
import time
import re

time_start = time.time()
db = pymysql.connect(host='localhost', port=3306, user='root', passwd='123456', database='dict', charset='utf8')
cur = db.cursor()
f = open('dict.txt', 'r')
for line in f:
    # result = line.split(' ', 1)
    tup = re.findall(r"(\S+)\s+(.*)", line)[0]
    # word = str(result[0])
    # mean = str(result[1])
    try:
        sql = "insert into words (word,mean) values (%s,%s);"
        cur.execute(sql, tup)
        db.commit()
    except Exception as e:
        db.rollback()
        print(e)
f.close()
cur.close()
db.close()
time_dur = time.time() - time_start
print(time_dur)
