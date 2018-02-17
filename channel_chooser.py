import re
from streamer import Streamer


class ChannelChooser(object):
    NUM_PER_PAGE = 15

    channel_list = []
    search_filter = None

    def __init__(self, channels):
        self.full_channel_list = channels

    def get_num_pages(self, channel_list):
        num_pages = round(len(channel_list) / self.NUM_PER_PAGE)
        if num_pages < 1:
            return 1
        else:
            return num_pages

    def get_user_input(self):
        user_input = input()
        if user_input == 'q':
            exit(0)
        elif user_input[:1] == '!':
            channel_id = user_input[1:]
            self.stream_channel(channel_id)
        elif user_input[:1] == 'r':
            self.search_filter = None
            self.display(self.full_channel_list)
        elif str.isdigit(user_input):
            try:
                page_number = int(user_input)
            except:
                print("Please enter a valid number. Defaulting to 1")
                page_number = 1
            self.display(self.channel_list, page_number)
        else:
            # search
            self.search_filter = user_input
            p = re.compile(user_input, re.IGNORECASE )
            search_list = []
            for channel in self.full_channel_list:
                if p.match(channel.getName()):
                    search_list.append(channel)
            self.display(search_list)

    def stream_channel(self, channel_id):
        for channel in self.full_channel_list:
            if channel.getChannelId() == channel_id:
                Streamer(channel).stream()

    def display(self, channels=None, page=1):
        if channels is None:
            self.channel_list = self.full_channel_list
        else:
            self.channel_list = channels

        if self.search_filter is None:
            print("All channels:")
        else:
            print("Channels matching '%s'" % self.search_filter)

        num_pages = self.get_num_pages(self.channel_list)

        offset = 0
        limit = self.NUM_PER_PAGE

        if page > num_pages:
            print("Bad page number, only %s pages. defaulting to 1" % int(num_pages))
            page = 1
        elif page > 0:
            offset = page * self.NUM_PER_PAGE - self.NUM_PER_PAGE

        channel_counter = 0
        num_printed = 0
        for channel in self.channel_list:
            if channel_counter >= offset and num_printed < limit:
                print("%s: %s" % (channel.getChannelId(), channel.getName()))
                num_printed += 1
            channel_counter += 1

        print("Showing page %d of %d" % (page, num_pages))
        print("Choose page to show, r to reset, q to quit or ![channelnumber] to broadcast the channel: ")
        self.get_user_input()
