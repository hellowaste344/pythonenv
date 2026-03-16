import logging
import signal
import sys
import time

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def signal_handler(signum: int, _frame) -> None:  # noqa: ANN001
    sig_name = signal.Signals(signum).name
    logger.info("Received signal %s", sig_name)


signal.signal(signal.SIGINT, signal_handler)
signal.signal(signal.SIGTERM, signal_handler)

while True:
    time.sleep(1)
