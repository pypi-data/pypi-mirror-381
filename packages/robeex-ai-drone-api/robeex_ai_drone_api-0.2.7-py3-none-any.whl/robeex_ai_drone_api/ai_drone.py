from typing import Optional
# from .utils import get_wifi_status
from .rc_api import RcApi
from .video_api import UDPVideoStream
from .rgb_led_api import RGBMode

class RobeexAIDrone:
    def __init__(self, drone_ip: str = "172.168.1.128", uuid: Optional[str] = None, debug = False):
        # if not isinstance(uuid, str) or len(uuid) != 6 or not all(c in "0123456789abcdefABCDEF" for c in uuid):
        #     raise ValueError("UUID must be a 6-digit hexadecimal string.")
        self.uuid = uuid
        self.rc = RcApi(drone_ip, drone_port=8585, debug=debug)  # Updated to include IP and port
        self.VideoCapture = lambda : UDPVideoStream(drone_ip, port=1234, debug=debug)  # Updated to include IP and port
        self.rc.start()

    def wait_for_telemetry(self):
        while True:
            telemetry = self.rc.get_next_telemetry_update()
            if telemetry:
                return True

    def __cleanup(self):
        self.rc.rgb.set_mode(RGBMode.AUTO)
        if self.rc.telemetry_data is None:
            print('no telemetry data ... skip flight cleanup')
            return
        if not self.rc.telemetry_data.is_armed:
            return
        if self.rc.telemetry_data.z > 0.1:
            self.rc.nav.land()
            print('force landing')
        else:
            self.rc.nav.disarm()
            print('force disarm')

    def cleanup(self):
        try:
            self.__cleanup()
        except Exception as e:
            print("Failed to cleanup", e)


    # def safe_run_async_func(self, async_func: callable, *args: tuple, **kwargs: dict) -> any:
    # def safe_run_async_func(self, cr: types.CoroutineType) -> any:
    #     try:
    #         asyncio.run(cr)
    #     except BaseException as e:
    #         print("Stopping...", e)
    #         self.cleanup()


    def __del__(self):
        self.cleanup()
        self.rc.stop()
