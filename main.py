from mitmproxy.options import Options
from mitmproxy.proxy.config import ProxyConfig
from mitmproxy.proxy.server import ProxyServer
from mitmproxy.tools.dump import DumpMaster

import threading
import asyncio
import time


import re



class InstagramDM(object):
    """
    Leaves message as unseen by blocking the seen request.
    Leaves story as unseen by blocking the seen request.
    """

    _targets = [
        r"https://i.instagram.com/api/v1/direct_v2/threads/.*/items/.*/seen/",
        r"https://www.instagram.com/stories/reel/seen"
    ]

    def match_url(self, url):
        """
        Match url against target url
        """
        coms = [
            re.compile(url) for url in self._targets
        ]
        return any([True if re.search(c_url, url) else False for c_url in coms])

    def request(self, flow):
        """Kill spesific request.
        """

        if self.match_url(flow.request.pretty_url) and flow.request.method == "POST":
            print("Marked as unseen :)")
            flow.kill()



class MitmClass:
    """Lunch mitmproxy within python.
    """
    def __init__(self, host, port, addons):

        self.options = Options(
            listen_host=str(host),
            listen_port=int(port),
            http2=True)

        self.mitm = DumpMaster(
            self.options,
            with_termlog=False,
            with_dumper=False)

        self.addons = addons
        self.config_server()

    def config_server(self):
        config = ProxyConfig(self.options)
        self.mitm.server = ProxyServer(config)
        self.mitm.addons.add(self.addons)


def loop_in_thread(loop, m):
    asyncio.set_event_loop(loop)
    m.mitm.run_loop(loop.run_forever)


if __name__ == "__main__":
    
    # setup
    mitm = MitmClass(
        host="127.0.0.1",
        port="8080",
        addons=InstagramDM()
    )

    # run mitm mproxy in backgroud
    loop = asyncio.get_event_loop()
    t = threading.Thread(target=loop_in_thread, args=(loop, mitm))
    t.start()
