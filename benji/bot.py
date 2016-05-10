"""Simple functionality atop jaraco's irc client library.

Heavily based upon the SimpleIRCBot from the same library.
"""
import irc.client

import benji


# Everything's stubbed thus far. See jaraco's irc.bot for examples on how to
# get started.
#https://github.com/jaraco/irc/blob/master/irc/bot.py
class BenjiBot(irc.client.SimpleIRCClient):
    """Handles IRC connection and identity state.

    All bot behavior is modeled via modules. See benji.modules for examples.
    """
    def __init__(self, **config):
        self.nick = config['nick']

        self._load_modules(**config)
        super(BenjiBot, self).__init__()

    def _load_modules(self, **config):
        pass

    def _on_disconnect(self, connection, event):
        # TODO
        pass

    def _on_join(self, connection, event):
        # TODO
        pass

    def _on_kick(self, connection, event):
        # TODO
        pass

    def _on_mode(self, connection, event):
        # TODO
        pass

    def _on_namreply(self, connection, event):
        # TODO
        pass

    def _on_nick(self, connection, event):
        # TODO
        pass

    def _on_part(self, connection, event):
        # TODO
        pass

    def _on_quit(self, connection, event):
        # TODO
        pass

    @staticmethod
    def get_version():
        """Returns a human-readable version string.

        This method is used to respond to ctcp.
        """
        return "Benji irc bot ({0})".format(benji.VERSION)

    def on_ctcp(self, connection, event):
        """Handler for ctcp events.

        Replies to VERSION and PING requests. DCC requests go to on_dccchat.
        """
        # TODO
        pass

    def on_dccchat(self, connection, event):
        """Default handler for DCC events."""
        # TODO
        pass

    def connect(self):
        # TODO
        pass

    def disconnect(self):
        """Disconnect from the server."""
        # TODO
        pass

    def start(self):
        """Start the IRC robot."""
        self.connect()
        super(BenjiBot, self).start()
