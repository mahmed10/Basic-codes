import os
try:
    os.mkdir(output_path)
except OSError:
    logging.info(os.path.abspath(output_path) + ' folder already existed')
else:
    logging.info(os.path.abspath(output_path) + ' folder created')
