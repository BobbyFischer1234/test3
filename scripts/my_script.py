import datetime
import sqlite3
import os

DB_PATH = "/opt/trailbase/traildepot/data/main.db"

def main():
    now = datetime.datetime.now()
    print(f"[{now}] Running betting script...")
    
    try:
        # For GitHub Actions, use a different path or skip DB
        if os.path.exists(DB_PATH):
            conn = sqlite3.connect(DB_PATH)
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO trailkey (executed_at) VALUES (?)",
                (now.strftime("%Y-%m-%d %H:%M:%S"),)
            )
            conn.commit()
            conn.close()
            print(f"✅ Data saved to TrailBase at {now}")
        else:
            print(f"⚠️ Database not found, running in demo mode")
            print(f"✅ Would have saved: {now}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
