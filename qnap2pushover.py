import os
import logging
from smtp.smtp_server import SmtpServer
from smtp.smtp_pushover_handler import SmtpPushoverHandler
from pushover.pushover_client import PushoverClient
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()
    logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.getLevelName(os.environ['LOG_LEVEL'].upper()))
    pushover_client = PushoverClient(os.environ['API_TOKEN'], os.environ['USER_KEY'])
    handler = SmtpPushoverHandler(pushover_client)
    server = SmtpServer(handler, 25)
    server.start()
