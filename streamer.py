import subprocess, os, signal, sys


class Streamer(object):
    STREAM_CMD = "dvblast"
    STREAM_CMD_ARGS = "-f %s 1 -c %s -m %s"
    PID_FILE = "dvblast.pid"
    CONFIG_FILE = "dvblast.config"
    CONFIG_ENTRY = "%s:%s 1 %s"
    MULTICAST_IP = "224.0.0.0"
    MULTICAST_PORT = "20000"

    def __init__(self, channel):
        self.channel = channel

    def stream(self):
        print("Streaming %s" % self.channel.getName())
        self.write_config()
        # print(self.STREAM_CMD_ARGS % (self.channel.getFrequency(), self.CONFIG_FILE, self.channel.modulation))
        self.terminate_if_running()
        process = subprocess.Popen([self.STREAM_CMD, self.STREAM_CMD_ARGS], stdout=subprocess.PIPE)
        self.write_pid(process.pid)

    def write_config(self):
        f = open(self.get_file_location(self.CONFIG_FILE), 'w')
        f.write(self.CONFIG_ENTRY % (self.MULTICAST_IP, self.MULTICAST_PORT, self.channel.getId()))
        f.close()

    def write_pid(self, pid):
        f = open(self.get_file_location(self.PID_FILE), 'w')
        f.write(str(pid))
        f.close()

    def is_running(self):
        os.getpgid()
        return True

    def get_pid(self):
        f = open(self.get_file_location(self.PID_FILE), 'r')
        pid = f.read()
        f.close()
        return pid

    def terminate_if_running(self):
        pid = self.get_pid()
        try:
            os.kill(int(pid), signal.SIGTERM)
        except OSError as e:
            # nothing to kill
            pass

    def get_file_location(self, file):
        return os.path.join(os.path.join(sys.path[0], file))

