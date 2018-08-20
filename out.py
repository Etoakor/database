import pymysql
import csv
import codecs


def get_conn():
    conn = pymysql.connect(host='localhost', port=3306, user='root', passwd='etoakor123', db='csv', charset='gbk')
    return conn

def query_all(cur, sql, args):
    cur.execute(sql, args)
    return cur.fetchall()


def read_mysql_to_csv(filename):
    with codecs.open(filename=filename, mode='w', encoding='gbk') as f:
        write = csv.writer(f, dialect='excel')
        conn = get_conn()
        cur = conn.cursor()
        sql = 'select * from csv'
        results = query_all(cur=cur, sql=sql, args=None)
        for result in results:
            print(result)
            write.writerow(result)



if __name__ == '__main__':
    read_mysql_to_csv('2.csv')