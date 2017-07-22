import subprocess
import os, signal


class Streamer(object):
    STREAM_CMD = "dvblast"
    STREAM_CMD_ARGS = "-f %s 1 -c %s -m %s"
    PID_FILE = "/var/run/dvblast.pid"
    CONFIG_FILE = "/tmp/dvblast.config"
    CONFIG_ENTRY = "%s:%s 1 %s"
    MULTICAST_IP = "224.0.0.0"
    MULTICAST_PORT = "20000"

    def __init__(self, channel):
        self.channel = channel

    def stream(self):
        print("Streaming %s" % self.channel.getName())
        self.writeConfig()
        # print(self.STREAM_CMD_ARGS % (self.channel.getFrequency(), self.CONFIG_FILE, self.channel.modulation))
        self.terminateIfRunning()
        process = subprocess.Popen([self.STREAM_CMD, self.STREAM_CMD_ARGS], stdout=subprocess.PIPE)
        self.writePid(process.pid)

    def writeConfig(self):
        f = open(self.CONFIG_FILE, 'w')
        f.write(self.CONFIG_ENTRY % (self.MULTICAST_IP, self.MULTICAST_PORT, self.channel.getId()))
        f.close()

    def writePid(self, pid):
        f = open(self.PID_FILE, 'w')
        f.write(str(pid))
        f.close()

    def isRunning(self):
        os.getpgid()
        return True

    def getPid(self):
        f = open(self.PID_FILE, 'r')
        pid = f.read()
        f.close()
        return pid

    def terminateIfRunning(self):
        pid = self.getPid()
        try:
            os.kill(int(pid), signal.SIGTERM)
        except OSError as e:
            # nothing to kill
            pass
