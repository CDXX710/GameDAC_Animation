# 🎛️ SteelSeries GameDAC 2.0 Custom OLED Animation

Animate text frames on your SteelSeries GameDAC 2.0 OLED screen using the GameSense API.

This script displays a looping animation of moving dots using text frames. You can customize it or create your own frame animations easily.

---

## 🔧 Requirements

- **SteelSeries GG (Engine 3+)** installed and running  
- **GameDAC 2.0** connected and recognized by SteelSeries Engine  
- **Python 3.6+**
- `requests` module (`pip install requests`)

---

## 🚀 Getting Started

1. Clone the repo or download the script:
   ```bash
   git clone https://github.com/yourname/custom-oled-animation.git
   cd custom-oled-animation
   ```

2. Install dependencies:
   ```bash
   pip install requests
   ```

3. Run the script:
   ```bash
   python oled_animation.py
   ```

4. The OLED will begin animating. Press `Ctrl+C` to stop.

---

## ✏️ Customizing the Animation

The animation frames are defined in the `ANIMATED_FRAMES` list:

```python
ANIMATED_FRAMES = [
    "·              ·",
    " ·            · ",
    ...
]
```

Each string is one frame (max 128px wide text), centered manually to fit within the 128x52 OLED display. You can replace these with your own patterns, text, or ASCII effects.

---

## 📂 File Structure

```bash
GameDAC_Animation/
├── CUSTOM_OLED_ANIMATION.py  # Main script
└── README.md                 # You're here
```

---

## 🧠 Notes

- The GameSense API listens locally on a dynamic port. This script reads the `coreProps.json` file from `C:\ProgramData\SteelSeries\SteelSeries Engine 3` to get the correct address.
- Tested on SteelSeries GG v83.0.1 with GSDK 2.5.18.0 and GameDAC 2.0.

---

## 📜 License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International
> [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

## 🧑‍💻 Credits

Made by **CDXX420**  
Powered by SteelSeries GameSense
