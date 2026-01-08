import psycopg2

def get_pg_connection():
    return psycopg2.connect(
        host="localhost",
        database="iotdb",
        user="postgres",
        password="12345678",
        port=5432
    )
    
    
def get_all_energy():
    conn = get_pg_connection()
    cur = conn.cursor()