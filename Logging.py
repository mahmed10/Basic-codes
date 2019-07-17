import logging

#setup logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
 
# create console handler and set level to info
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)
formatter = logging.Formatter("%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)

# create error file handler and set level to error
handler = logging.FileHandler('logfile.log',"w", encoding=None, delay="true")
handler.setLevel(logging.INFO)
formatter = logging.Formatter("[%(message)s")
handler.setFormatter(formatter)
logger.addHandler(handler)


''''''''''########''''''''''
Log level
CRITICAL-50
ERROR-40
WARNING-30
INFO-20
DEBUG-10
NOTSET-0
''''''''''########''''''''''
For formatting

%(asctime)s "Human-readable time when the LogRecord was created"
%(filename)s "Filename portion of pathname"
%(levelname)s "Text logging level for the message"
%(levelno)s "Numeric logging level for the message (DEBUG, INFO, WARNING, ERROR, CRITICAL)"
%(lineno)d "Source line number where the logging call was issued (if available)"
%(msecs)d "Millisecond portion of the time when the LogRecord was created"
%(message)s "The logged message"
%(name)s "Name of the logger used to log the call"
%(pathname)s "Full pathname of the source file where the logging call was issued (if available)"
%(thread)d "Thread ID (if available)"
%(threadName)s "Thread name (if available)"
