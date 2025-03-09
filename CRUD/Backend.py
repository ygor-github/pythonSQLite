import sqlite3 as sql

class TransactionObject:
    database = "clients"
    conn = None
    cur = None
    connected = False
    sql_query = sql
    
    @staticmethod
    def connect():
        TransactionObject.conn = sql.connect(TransactionObject.database)
        TransactionObject.cur = TransactionObject.conn.cursor()
        TransactionObject.connected = True
    
    @staticmethod
    def disconnect():
        TransactionObject.conn.close()
        TransactionObject.connected = False
    
    @staticmethod
    def execute(sql_query, params=None):
        if TransactionObject.connected:
            if params is None:
                TransactionObject.cur.execute(sql_query)
            else:
                TransactionObject.cur.execute(sql_query, params)
            return True
        else:
            return False
        
    @staticmethod
    def fetchall():
        return TransactionObject.cur.fetchall()
    
    @staticmethod
    def persist():
        if TransactionObject.connected:
            TransactionObject.conn.commit()
            return True
        else:
            return False
     
    @staticmethod
    def initdb():
        trans = TransactionObject()
        trans.connect()
        trans.execute("CREATE TABLE IF NOT EXISTS clients (user_id INTEGER PRIMARY KEY, name TEXT, lastname TEXT, email TEXT, cpf TEXT)")
        trans.persist()
        trans.disconnect()
    
    @staticmethod
    def insert(name, lastname, email, cpf):
        if name and lastname and email and cpf:
            try:
                trans = TransactionObject()
                trans.connect()
                trans.execute("INSERT INTO clients VALUES(NULL, ?,?,?,?)", (name, lastname, email, cpf))
                trans.persist()
                trans.disconnect()
                return True
            except sql.Error as e:
                print(f"Error al insertar: {e}")
                return False
        else:
            print("Error: Todos los campos deben estar completos.")
            return False
    
    @staticmethod
    def view():
        trans = TransactionObject()
        trans.connect()
        trans.execute('SELECT * FROM clients')
        rows = trans.fetchall()
        trans.disconnect()
        return rows
    
    @staticmethod
    def search(name='', lastname='', email='', cpf=''):
        trans = TransactionObject()
        trans.connect()
        trans.execute('SELECT * FROM clients WHERE name=? or lastname=? or email=? or cpf=?', (name, lastname, email,cpf))
        rows = trans.fetchall()
        trans.disconnect()
        return rows
    
    @staticmethod
    def delete(user_id):
        trans = TransactionObject()
        trans.connect()
        trans.execute('DELETE FROM clients WHERE user_id =?', (user_id,))
        trans.persist()
        trans.disconnect()
    
    @staticmethod
    def update(user_id, name, lastname, email, cpf):
        trans = TransactionObject()
        trans.connect()
        trans.execute('UPDATE clients SET name=?, lastname=?, email=?, cpf=? WHERE user_id=?', (name, lastname, email, cpf, user_id))
        trans.persist()
        trans.disconnect()
        
TransactionObject.initdb()
