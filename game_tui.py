#!/usr/bin/env python3
import random
import time
import sys
import os
from audio import get_note
import questionary
import caffeine
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from pyfiglet import figlet_format

console = Console()

C_MAJOR = ["C", "D", "E", "F", "G", "A", "B"]
CHROMATIC = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

def get_random_note(scale, last_note):
    note = random.choice(scale)
    while note == last_note:
        note = random.choice(scale)
    return note

def strip_octave(note):
    return "".join([char for char in note if not char.isdigit()])

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_note(note, accuracy):
    clear_screen()
    big_note = figlet_format(note, font="big")
    console.print(Panel(big_note, style="bold magenta on black", expand=False), justify="center")
    console.print(f"Accuracy: {accuracy:.2f}%", style="bold green", justify="center")

def run_game(scale):
    correct = 0
    attempts = 0
    last_wrong_note = None
    last_right_note = None
    last_target_note = None

    while True:
        target_note = get_random_note(scale, last_target_note)
        display_note(target_note, (correct / max(1, attempts)) * 100)

        for detected_note in get_note():
            detected_note_simple = strip_octave(detected_note)

            if detected_note_simple == target_note:
                correct += 1
                attempts += 1
                display_note(target_note, (correct / max(1, attempts)) * 100)
                console.print("[bold green]Correct![/bold green]", justify="center")
                time.sleep(0.5)
                last_target_note = target_note
                last_right_note = detected_note
                break
            elif (detected_note_simple != target_note
            and detected_note != last_wrong_note
            and detected_note != last_right_note):
                attempts += 1
                display_note(target_note, (correct / max(1, attempts)) * 100)  # Redraw everything
                console.print(f"[bold red]Try again... You played: {detected_note_simple}[/bold red]", justify="center")
                last_wrong_note = detected_note

def select_mode():
    choice = questionary.select(
        "Select mode:",
        choices=["C Major", "Chromatic"],
    ).ask()

    return C_MAJOR if choice == "C Major" else CHROMATIC

def main():
    scale = select_mode()
    time.sleep(0.8)

    caffeine.on()  # Prevents the system from sleeping
    run_game(scale)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        console.print("\n[bold yellow]Goodbye! Thanks for playing.[/bold yellow]", justify="center")
        caffeine.off()
        sys.exit(0)
