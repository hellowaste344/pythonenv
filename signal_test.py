import logging
import signal
import sys
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def signal_handler(sig, frame):  # noqa: ANN001
    logger.info("Received signal %s", sig)
    sys.exit()


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

while True:
    time.sleep(1)
