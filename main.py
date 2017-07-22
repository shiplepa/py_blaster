import argparse, sys
from channel_parser import ChannelParser
from channel_chooser import ChannelChooser

channels = {}


def process_channels(content):
    for row in content:
        parser = ChannelParser()
        ch = parser.parse(row)
        if ch:
            channels[ch.getId()] = ch
    sorted(channels.values(), key=lambda x:x.name)



def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-f", "--file", help="Channel configuration file to load")
    parser.add_argument("-s", "--stream", help="Channel to broadcast")

    args = parser.parse_args()

    file = None
    stream = None

    if args.file is not None:
        file = args.file

    if args.stream is not None:
        stream = args.stream

    if file is None:
        parser.usage
        sys.exit(1)

    with open(file) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    process_channels(content)

    if stream is None:
        # Show channels
        channel_chooser = ChannelChooser(channels)
        channel_chooser.display()


if __name__ == "__main__":
    main()
