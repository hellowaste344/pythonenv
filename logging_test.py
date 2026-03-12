import logging

logging.error("program raised an error!")

logger = logging.getLogger("SimpleLogger")
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("app.log")
logger.addHandler(file_handler)

logger.info("Info message ")
logger.error("Error message ")


logging.basicConfig(
    filename="newfile.log",
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    filemode="w",
)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("Debug action")
logger.info("Info text")
logger.warning("Something's off")
logger.error("System is about to crush!!")
logger.critical("Kernel is shutdown")
