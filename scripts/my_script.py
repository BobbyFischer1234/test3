cat > /opt/test3/scripts/my_script.py << 'EOF'
import datetime
import sqlite3

DB_PATH = "/opt/trailbase/traildepot/data/main.db"

def main():
    now = datetime.datetime.now()
    print(f"[{now}] Running betting script...")
    
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # Insert timestamp into trailkey table
        cursor.execute(
            "INSERT INTO trailkey (executed_at) VALUES (?)",
            (now.strftime("%Y-%m-%d %H:%M:%S"),)
        )
        
        conn.commit()
        conn.close()
        
        print(f"✅ Data saved to TrailBase at {now}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
EOF
