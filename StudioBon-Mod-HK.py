
# ba_meta require api 9
# StudioBon-Mod-HK

import babase
import bascenev1 as bs

_original_connect = bs.connect_to_party
_original_disconnect = bs.disconnect_from_host

_server_address = "127.0.0.1"
_join_token = 0


def _send_first(token):
    if token != _join_token:
        return

    try:
        info = bs.get_connection_to_host_info_2()
        if not info:
            return
        bs.chatmessage("Gift Pigord 100")
    except Exception:
        return

    babase.apptimer(1.0, lambda: _send_second(token))


def _send_second(token):
    if token != _join_token:
        return

    try:
        if bs.get_connection_to_host_info_2():
            bs.chatmessage("1")
    except Exception:
        pass


def _connect(address, port=43210, print_progress=False):
    global _server_address, _join_token

    result = _original_connect(address, port, print_progress)
    _server_address = str(address)
    _join_token += 1
    token = _join_token

    babase.apptimer(5.0, lambda: _send_first(token))
    return result


def _disconnect():
    global _server_address, _join_token

    _join_token += 1
    _server_address = "127.0.0.1"
    return _original_disconnect()


bs.connect_to_party = _connect
bs.disconnect_from_host = _disconnect


# ba_meta export babase.Plugin
class StudioBonModHKPlugin(babase.Plugin):
    pass
