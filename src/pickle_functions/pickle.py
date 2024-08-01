import pickle
from loguru import logger

def load_pickle(file_path):
    try:
        with file_path.open(mode = 'rb') as file:
            data = pickle.load(file)
            return data
    except FileNotFoundError as e:
        logger.error(f"File not found at: {file_path}, Error: {e}")
    except Exception as e:
        logger.error(f"Exception occured: {e}")


def dump_pickle(data, file_path):
    try:
        with file_path.open(mode = 'wb') as file:
            pickle.dump(data, file)
    except Exception as e:
        logger.error(f"Exception occured: {e}")