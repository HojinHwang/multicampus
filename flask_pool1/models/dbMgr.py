# models/dbMgr.py
from models.db import POOL

def test1():
    try:
        conn = POOL.connection()
        cur = conn.cursor()
        cur.execute('select * from mem')
        rows = cur.fetchall()
        cur.close()
        print(rows)
    except Exception as e:
        print('오류===', e)
    finally:
        conn.close()

def test_err():
    conn = POOL.connection()
    cur = conn.cursor()
    cur.execute('select * from me')
    rows = cur.fetchall()
    cur.close()
    print(rows)
    conn.close()
