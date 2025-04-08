#!/usr/bin/env python3
import random
import time
import sys
from audio import get_note

C_MAJOR = ["C", "D", "E", "F", "G", "A", "B"]
CHROMATIC = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def get_random_note(scale):
    return random.choice(scale)

def strip_octave(note):
    return "".join([char for char in note if not char.isdigit()])

def run_game(scale):
    print("Play the displayed note!")
    last_printed_note = None
    while True:
        target_note = get_random_note(scale)
        print(f"Play: {target_note}")
        for detected_note in get_note():
            detected_note_simple = strip_octave(detected_note)
            if detected_note_simple == target_note:
                if last_printed_note != target_note:
                    print("Correct!", flush=True)
                    last_printed_note = target_note
                time.sleep(0.5)
                break
            else:
                if last_printed_note != detected_note_simple:
                    print(f"Try again... You played: {detected_note_simple}", flush=True)
                    last_printed_note = detected_note_simple

def main():
    print("Select mode: (1) C Major (2) Chromatic")
    choice = input("Enter 1 or 2: ").strip()
    if choice == "1":
        scale = C_MAJOR
    elif choice == "2":
        scale = CHROMATIC
    else:
        print("Invalid choice.")
        sys.exit(1)
    run_game(scale)

if __name__ == "__main__":
    main()
