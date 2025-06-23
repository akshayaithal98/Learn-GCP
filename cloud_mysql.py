import mysql.connector 

def mysql_conn():
    try:
        host=""
        user=""
        password=''
        database="mysql_db"
        port=''
        conn=mysql.connector.connect(user=user,password=password,host=host,database=database,port=port)
        return conn
    except mysql.connector.Error as error:
        raise error
    except Exception as er:
        raise er

def execute_query(query):
    conn=mysql_conn()
    print(conn)
    cur=conn.cursor(dictionary=True)
    print(cur)
    cur.execute(query)
    rows=cur.fetchall()
    return rows

result=execute_query("select * from mysql_db.students")
print(result)

