import requests
import zipfile
import zipfile
import zipfile
from io import BytesIO
import urllib
from pathlib import Path
from pickle_functions.pickle import load_pickle, dump_pickle
from loguru import logger
from datetime import datetime
import os
import config 

start_time = datetime.now()
response = requests.get(config.extraction_url)
zip_data = BytesIO(response.content)

raw_zone_directory = config.raw_zone_directory

if not os.path.exists(raw_zone_directory):
    os.makedirs(raw_zone_directory)

extracted_files = load_pickle(config.files_extracted)

count = 0
with zipfile.ZipFile(zip_data) as z:
    for filename in z.namelist():

        if not extracted_files[filename]:
            extracted_files[filename] = 1
            file_contents = z.open(filename).read()
            file_contents = file_contents.decode("utf-8")
               
            with open(Path(f"{raw_zone_directory}/{filename}"), 'w') as file:
                file.write(file_contents)     

            dump_pickle(extracted_files, config.files_extracted)
            count += 1
logger.info(f"{count} files have been extracted and written to the raw data")
end_time = datetime.now()
elapsed_time = end_time - start_time
logger.info(f"First extraction took {elapsed_time}")