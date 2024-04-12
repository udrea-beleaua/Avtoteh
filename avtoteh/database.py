import sqlite3


def create_table():
    conn =sqlite3.connect('piese.db')
    cursor= conn.cursor()
        
    cursor.execute('''
                    CREATE TABLE IF NOT EXISTS piese (
                        id TEXT PRIMARY KEY,
                        name TEXT,
                        marca TEXT,
                        model TEXT,
                        status TEXT)''')
    conn.commit()
    conn.close()
        
def fetch_piese():
    conn =sqlite3.connect('piese.db')
    cursor=conn.cursor()
    cursor.execute('SELECT * FROM piese')
    piese=cursor.fetchall()
    conn.close()
    return piese

def insert_piese(id,name,marca,model,status):
    connn = sqlite3.connect('piese.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO piese(id,name,year,car,status VALUES (?,?,?,?,?)',
                   (id,name,marca,model,status))
    conn.commit()
    conn.close()
        
def delete_piese(id):
    conn = sqlite3.connect('piese.db')
    cursor=conn.cursor()
    cursor.execute('DELETE FROM piese WHERE id = ?',(id,))
    conn.commit()
    conn.close()
        
def update_piese(new_name,new_marca,new_model,new_status,id):
    con=sqlite3.connect('piese.db')
    cursor=conn.cursor()
    cursor.execute("UPDATE piese SET name=?,marca=?,model=?,status=? WHERE id =?",
                   (new_name,new_marca,new_model,new_status,id))   
    conn.commit()
    conn.close()
        
def id_exists(id):
    conn=sqlite3.connect('piese.db')
    cursor=conn.cursor()
    cursor.execute('SELECT COUNT(*) FROM piese WHERE id=?',(id,))
    result=cursor.fetchone()
    conn.close()
    return result[0]>0
    
create_table()