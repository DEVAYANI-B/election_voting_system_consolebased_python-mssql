import pyodbc

class DBConnection:
    conn=None

    @staticmethod
    def get_connection():
        if DBConnection.conn is None:
            DBConnection.conn=pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};'
                'SERVER=localhost,1433;'
                'DATABASE=appdb;'
                'UID=sa;'
                'PWD=examlyMssql@123'
            )
            print("Database connected successfully!")
        return DBConnection.conn
    @staticmethod
    def close_connection():
        if DBConnection.conn:
            DBConnection.conn.close()
            DBConnection.conn=None