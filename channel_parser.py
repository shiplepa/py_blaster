from channel import Channel
import re


class ChannelParser:

    ENTRY_FORMAT = "(.*):(.*):.*:.*:.*:.*:(.*):.*:.*:.*:.*:.*:(.*)"

    def parse(self, row):
        match = re.match(self.ENTRY_FORMAT, row)
        if match:
            return Channel(match.group(1), match.group(2), match.group(3), match.group(4))
        else:
            print("Failed to parse row: %s" % row)
