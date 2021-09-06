import requests
import time


class RokuClient:

    _PROTOCOL = "http"
    _PORT = 8060
    _MAX_RETIRES_PER_REQUEST = 3
    _SECS_BETWEEN_REQUESTS = 0.25      # seconds to wait between keypress commands
    _ALLOW_WAKE_SECS = 6               # seconds to wait for TV to wake
    
    # constants for Roku API
    _KEYPRESS_CMD = "keypress"
    

    def __init__(self, ip_addr):
        # setup the API url
        self._keypress_url = RokuClient._PROTOCOL + "://" + ip_addr + ":" + str(RokuClient._PORT) + "/" + RokuClient._KEYPRESS_CMD + "/"
        self._read_command_file()

    def _read_command_file(self):
        modes_read = 0
        f = open('commands.txt', 'r')

        for line in f:
            line = line.strip()
            if (line.startswith('#') or len(line) == 0):
                continue

            if modes_read == 0:
                self._day_seq = line.split(',')
            elif modes_read == 1:
                self._night_seq = line.split(',')

            modes_read += 1

        f.close()


    def night_mode(self):
        self._sendreq(self._night_seq)


    def day_mode(self):
        self._sendreq(self._day_seq)
            
            
    def _sendreq(self, keypress_seq):
        for i, key in enumerate(keypress_seq):
            
            success = False
            retry = 0
            
            while (success is False) and (retry <= RokuClient._MAX_RETIRES_PER_REQUEST) :
                resp = requests.post(self._keypress_url + key)
                success = resp.ok
                ++retry

            # allow additional time after first request, TV may be in sleep mode
            if i == 0:
                time.sleep(RokuClient._ALLOW_WAKE_SECS)
            else:
                time.sleep(RokuClient._SECS_BETWEEN_REQUESTS)
