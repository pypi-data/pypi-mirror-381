import mido
import time
from textual import log


class MidiController:
    @staticmethod
    def send_preset_change(port: str, cc: int, pgm: int):
        try:
            output = mido.open_output(port)
            log(f"opened port: {port}")
        except OSError as e:
            log(f"Error opening MIDI port '{port}': {e}")
            return False

        cc_msg = mido.Message("control_change", channel=0, control=0, value=cc)
        log(f"Sending CC message: {cc_msg.hex()}")
        time.sleep(1.0)
        output.send(cc_msg)
        log(f"Sent CC message: {cc_msg.hex()}")

        time.sleep(0.4)

        pgm_msg = mido.Message("program_change", channel=0, program=pgm)
        log(f"Sending PGM message: {pgm_msg.hex()}")
        output.send(pgm_msg)
        log(f"Sent PGM message: {pgm_msg.hex()}")

        output.close()
