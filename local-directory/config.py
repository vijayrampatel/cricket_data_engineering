from pathlib import Path
from datetime import datetime

extraction_url = "https://cricsheet.org/downloads/all_csv2.zip"

files_extracted = Path('files_extracted.pkl')

raw_zone_directory = Path(f"raw_data/{datetime.now().strftime('%Y-%m-%d')}")


