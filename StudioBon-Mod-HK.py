# ba_meta require api 9
# StudioBon-Mod-HK
# Sends two chat messages once after joining a server.

import babase
import bascenev1 as bs


class StudioBonModHK(babase.Plugin):
    """StudioBon-Mod-HK for BombSquad API 9."""

    def __init__(self):
        self._was_connected = False
        self._join_generation = 0
        self._poll_timer = babase.apptimer(0.5, self._check_connection, repeat=True)

    def _is_connected(self):
        try:
            info = bs.get_connection_to_host_info_2()
            return bool(info)
        except Exception:
            return False

    def _check_connection(self):
        connected = self._is_connected()

        if connected and not self._was_connected:
            self._join_generation += 1
            generation = self._join_generation
            babase.apptimer(5.0, lambda: self._send_first_message(generation))

        self._was_connected = connected

    def _send_first_message(self, generation):
        if generation != self._join_generation or not self._is_connected():
            return
        try:
            bs.chatmessage("Gift Mobile 100")
        except Exception:
            return
        babase.apptimer(1.0, lambda: self._send_second_message(generation))

    def _send_second_message(self, generation):
        if generation != self._join_generation or not self._is_connected():
            return
        try:
            bs.chatmessage("1")
        except Exception:
            pass


# ba_meta export babase.Plugin
class StudioBonModHKPlugin(StudioBonModHK):
    pass
