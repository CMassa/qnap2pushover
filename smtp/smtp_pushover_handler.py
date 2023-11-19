import logging
from pushover.pushover_notification import PushoverNotification
from pushover.pushover_client import PushoverClient

class SmtpPushoverHandler:

    def __init__(self, pushover_client: PushoverClient) -> None:
        self.pushover_client = pushover_client

    async def handle_RCPT(self, server, session, envelope, address, rcpt_options):
        envelope.rcpt_tos.append(address)
        return '250 OK'

    async def handle_DATA(self, server, session, envelope):
        logging.info('Message from %s' % envelope.mail_from)
        logging.info('Message for %s' % envelope.rcpt_tos)
        data = envelope.content.decode('utf8', errors='replace').splitlines()
        msg = ""
        for ln in data:
            msg += f'{ln}\n'
        logging.info('Message data:\n')
        logging.info(msg)
        self.pushover_client.send_notification(PushoverNotification(msg))
        return '250 Message accepted for delivery'