from streamer import Streamer


class ChannelChooser(object):
    NUM_PER_PAGE = 15

    def __init__(self, channels):
        self.channels = channels

    def getNumPages(self):
        return len(self.channels) / self.NUM_PER_PAGE

    def getNextPage(self):
        user_page_number = input()
        if user_page_number == 'q':
            exit(0)
        elif user_page_number[:1] == '!':
            channel_id = user_page_number[1:];
            Streamer(self.channels[channel_id]).stream()
        else:
            try:
                page_number = int(user_page_number)
            except:
                print("Please enter a valid number. Defaulting to 1")
                page_number = 1
            self.display(page_number)

    def display(self, page=1):
        print("Parsed channels:")
        num_pages = self.getNumPages()

        offset = 0
        limit = self.NUM_PER_PAGE

        if page > num_pages:
            print("Bad page number, only %s pages. defaulting to 1" % int(num_pages))
            page = 1
        elif page > 0:
            offset = page * self.NUM_PER_PAGE - self.NUM_PER_PAGE

        channel_counter = 0
        num_printed = 0
        for channel in self.channels:
            if channel_counter >= offset and num_printed < limit:
                print("%s: %s" % (channel, self.channels[channel].getName()))
                num_printed += 1
            channel_counter += 1

        if num_pages > 1:
            print("Showing page %d of %d" % (page, num_pages))
            print("Choose page to show, q to quit or ![channelnumber] to broadcast the channel: ")
            self.getNextPage()
