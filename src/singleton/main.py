from singleton_logger import LoggerSingleton

logger1 = LoggerSingleton("1log")
logger1.critical("critical")
print(logger1.file_name)
logger2 = LoggerSingleton("2log")
logger2.critical("critical")
print(logger2.file_name)
logger1.info("info? to 2nd")

print(logger1.file_name)
