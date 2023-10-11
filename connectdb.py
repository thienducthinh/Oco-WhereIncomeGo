import pymysql

class DBconnect(object):
    def __init__(self):
        self.dbconnection = pymysql.connect(
        host= "localhost",
        port=int(3306),
        user="admin",
        passwd="Thinhnguyen2491",
        db="Oco-WhereIncomeGo")
        
        self.dbcursor = self.dbconnection.cursor()

    def commit_db(self):
        self.dbconnection.commit()
    
    def close_db(self):
        self.dbcursor.close()
        self.dbconnection.close()


# db_test = DBconnect()
# db_test.dbcursor.execute("SELECT * FROM %s LIMIT 5" % ("us_zip_codes"))
# for row in db_test.dbcursor.fetchall():
#     print(row)