import pymysql.cursors
# Connect to the database
def getConnection():
	connection = pymysql.connect(host='101.200.213.220',
                             port=3306,
                             user='superadmin',
                             password='AdminSuper',
                             db='employees',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
	return cursor = conn.cursor()


def execute(sql):
	cursor.execute(sql)
	return cursor.lastrowid

def read_xls_file():  
    xls_data = get_data(r"D:/read_test.xlsx")  
    print "Get data type:", type(xls_data)  

    print sheet_n, ":", xls_data

