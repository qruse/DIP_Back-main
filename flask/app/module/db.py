import psycopg2 as pg2

class Database():
    def __init__(self):
        user = 'postgres'
        password = 'postgres'
        host_product = '172.20.18.02' # 배포 server HOST ip 명시
        dbname = 'dip_library'
        port='5432' # 포트 포워딩된 포트 명시
        product_connection_string = "dbname={dbname} user={user} host={host} password={password} port={port}".format(dbname=dbname,
                                    user=user,
                                    host=host_product,
                                    password=password,
                                    port=port)  
        self.db = pg2.connect(product_connection_string)
        # DB corsor Object
        self.cursor = self.db.cursor()
    # it's Database execute Func. in sql, Do not have return value like INSERT, DELETE, ALTER etc.
    def execute(self, query, args={}):
        self.cursor.execute(query, args)
        self.db.commit()
    # it's exeuteAll. in sql, this func have return value like SELECT etc.
    def executeAll(self,query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchall()
        return row
    # if you want the return value one by one, using this func
    def executeOne(self, query, args={}):
        self.cursor.execute(query, args)
        row = self.cursor.fetchone()
        return row