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
        super(BenjiBot, self).__init__()

        self.meta_config = config['meta']
        self.connection_config = config['connection']
        self.channels = config['channels']

        self._load_modules()


    def _load_modules(self):
        pass

    def _join_channels(self):
        for channel in self.channels:
            self.connection.join(channel)

    def on_disconnect(self, connection, event):
        # TODO
        print('disconnect event')
        pass

    def on_welcome(self, connection, event):
        self._join_channels()

    def on_nicknameinuse(self, connection, event):
        new_nick = self.meta_config['nick'] + '_'
        self.meta_config['nick'] = new_nick
        connection.nick(new_nick)

    def on_join(self, connection, event):
        # TODO
        print('join event')
        pass

    def on_kick(self, connection, event):
        # TODO
        print('kick event')
        pass

    def on_mode(self, connection, event):
        # TODO
        print('mode event')
        pass

    def on_namreply(self, connection, event):
        # TODO
        print('namreply event')
        pass

    def on_nick(self, connection, event):
        # TODO
        print('nick event')
        pass

    def on_part(self, connection, event):
        # TODO
        print('part event')
        pass

    def on_quit(self, connection, event):
        # TODO
        print('quit event')
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
        print("ctcp event")
        source_nick = event.source.nick
        if event.arguments[0] == 'VERSION':
            connection.ctcp_reply(source_nick, "VERSION " + self.get_version())
        elif event.arguments[0] == "PING":
            if len(event.arguments) > 1:
                connection.ctcp_reply(source_nick, "PING " + event.arguments[1])
        elif event.arguments[0] == "DCC" and event.arguments[1].split(" ", 1)[0] == "CHAT":
            self.on_dccchat(connection, event)
        # TODO
        pass

    def on_dccchat(self, connection, event):
        """Default handler for DCC events."""
        print("dccchat event")
        # TODO
        pass

    def on_privmsg(self, connection, event):
        print("privmsg event")
        # TODO
        pass

    def on_pubmsg(self, connection, event):
        print("pubmsg event")
        # TODO
        pass

    def connect(self):
        print("Connecting...")
        super(BenjiBot, self).connect(
            server=self.connection_config['host'],
            port=self.connection_config['port'],
            nickname=self.meta_config['nick'],
            password=self.meta_config['password'],
            username=self.meta_config['username'],
            ircname=self.meta_config['realname'])
        self._join_channels()
        print("Done.")

    def disconnect(self):
        """Disconnect from the server."""
        print("Disconnecting")
        # TODO
        pass

    def start(self):
        """Start the IRC robot."""
        self.connect()
        super(BenjiBot, self).start()
