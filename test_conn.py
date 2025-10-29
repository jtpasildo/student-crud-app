# test_db.py
from db import get_conn

try:
    conn = get_conn()
    print("✅ Connected successfully using db.py!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:")
    print(e)
