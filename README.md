# Guitar Fretboard Memorization Tool

This tool helps you memorize the guitar fretboard like a reverse tuner. It prompts you to 'play [Note]' and listens for you to play the correct note on your guitar. It then provides feedback with a percentage of accuracy.

## Setup

1. Create a virtual environment:
```
python3 -m venv venv
```
2. Activate the virtual environment:
   - On Unix or MacOS:
```
source venv/bin/activate
```
   - On Windows:
```
.env\Scripts\activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage

This tool has two versions:

1. **Basic Version** (Fully Textual)
```
./game_basic.py
```

2. **TUI Version** (Recommended)
```
./game_tui.py
```

No arguments are required. Just run the desired version, connect your audio interface and guitar, and start playing.

The TUI version offers a more user-friendly experience with better feedback.

---

Happy practicing!
