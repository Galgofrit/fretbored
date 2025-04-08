#!/usr/bin/env python3
import numpy as np
import sounddevice as sd
import aubio
import time

win_s = 2048
hop_s = win_s // 8
samplerate = 44100
min_db = -44  # Increase sensitivity by lowering threshold

detector = aubio.pitch("default", win_s, hop_s, samplerate)

current_note = None
note_start_time = None

def get_note():
    global current_note, note_start_time
    stream = sd.InputStream(samplerate=samplerate, channels=1, blocksize=hop_s)
    with stream:
        while True:
            audio_data, _ = stream.read(hop_s)
            samples = np.frombuffer(audio_data, dtype=np.float32)
            pitch = detector(samples)[0]
            volume_db = 20 * np.log10(np.max(np.abs(samples)) + 1e-10)

            note = aubio.freq2note(pitch)
            current_time = time.time()

            if pitch > 0 and volume_db > min_db:
                if note != current_note:
                    current_note = note
                    note_start_time = current_time

                if current_note and current_time - note_start_time > 0.5:
                    yield current_note
                    current_note = None
                    note_start_time = None

if __name__ == "__main__":
    print("Tuner Mode: Showing detected notes.")
    for note in get_note():
        print(note)
