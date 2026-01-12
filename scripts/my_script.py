import datetime
import pandas as pd
from pathlib import Path

def main():
    now = datetime.datetime.now()
    print(f"Python script executed at: {now}")

    file_path = Path("data/results.xlsx")

    # SAFETY: ensure data/ is a directory
    if file_path.parent.exists() and not file_path.parent.is_dir():
        raise RuntimeError("'data' exists but is not a directory")

    file_path.parent.mkdir(parents=True, exist_ok=True)

    df_new = pd.DataFrame([{
        "executed_at": now.strftime("%Y-%m-%d %H:%M:%S")
    }])

    if file_path.exists():
        df_old = pd.read_excel(file_path)
        df_all = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_all = df_new

    df_all.to_excel(file_path, index=False)

if __name__ == "__main__":
    main()
