import asyncio
from aiosmtpd.controller import UnthreadedController
from typing import Any

class SmtpServer(UnthreadedController):

    def __init__(self, handler: Any, port: int):
        self.loop = asyncio.get_event_loop()
        self.controller = UnthreadedController(handler, "0.0.0.0", port, loop=self.loop)

    def start(self):
        try:
            self.controller.begin()
            self.loop.run_forever()
        except KeyboardInterrupt:
            self.controller.finalize()
        
