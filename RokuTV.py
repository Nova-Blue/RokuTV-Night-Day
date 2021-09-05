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
    _UP_KEY = "Up"
    _DOWN_KEY = "Down"
    _LEFT_KEY = "Left"
    _RIGHT_KEY = "Right"
    _INFO_KEY = "Info"
    _BACK_KEY = "Back"
    _MUTE_KEY = "VolumeMute"

    # keypress sequences for modifying TV brightness
    _NIGHT_SEQ = [_INFO_KEY, _DOWN_KEY, _RIGHT_KEY, _DOWN_KEY, _DOWN_KEY, _LEFT_KEY,
                   _LEFT_KEY, _INFO_KEY, _MUTE_KEY]
    _DAY_SEQ = [_INFO_KEY, _DOWN_KEY, _LEFT_KEY, _DOWN_KEY, _DOWN_KEY, _RIGHT_KEY,
                   _RIGHT_KEY, _INFO_KEY, _MUTE_KEY]
    

    def __init__(self, ip_addr):
        # setup the API url
        self._keypress_url = RokuClient._PROTOCOL + "://" + ip_addr + ":" + str(RokuClient._PORT) + "/" + RokuClient._KEYPRESS_CMD + "/"


    def night_mode(self):
        self._sendreq(RokuClient._NIGHT_SEQ)


    def day_mode(self):
        self._sendreq(RokuClient._DAY_SEQ)
            
            
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
