import json
import os
import time
import requests

# Constants for GameSense game and event naming
GAME_NAME = "CUSTOM_OLED_ANIMATION"
EVENT_NAME = "ANIMATION"

# Frames for a simple dot animation to be displayed on the GameDAC OLED screen
ANIMATED_FRAMES = [
    "·              ·",
    " ·            · ",
    "  ·          ·  ",
    "   ·        ·   ",
    "    ·      ·    ",
    "     ·    ·     ",
    "      ˙  .      ",
    "       ˙.       ", 
    "       .˙       ", 
    "      .  ˙      ",
    "     ·    ·     ",
    "    ·      ·    ",
    "   ·        ·   ",
    "  ·          ·  ",
    " ·            · ",
]

def get_sse_address():
    """
    Reads the SteelSeries Engine coreProps.json file to retrieve the local SSE REST API address.
    Returns the full HTTP address or None if an error occurs.
    """
    try:
        corePropsPath = os.path.join(
            os.getenv("PROGRAMDATA"),
            "SteelSeries",
            "SteelSeries Engine 3",
            "coreProps.json",
        )
        with open(corePropsPath, "r") as f:
            address = json.load(f)["address"]
        return f"http://{address}"
    except Exception as e:
        print(f"[ERROR] Failed to get SSE address: {e}")
        return None

def register_game():
    """
    Registers a custom game with the SteelSeries Engine so that we can bind custom events.
    """
    url = f"{sse_address}/game_metadata"
    payload = {
        "game": GAME_NAME,
        "game_display_name": "Custom OLED Animation",
        "developer": "CDXX420",
    }
    try:
        requests.post(url, json=payload)
    except requests.RequestException as e:
        print(f"[ERROR] Failed to register game: {e}")

def register_event():
    """
    Registers a game event that will be triggered with our animation frames.
    """
    url = f"{sse_address}/register_game_event"
    payload = {"game": GAME_NAME, "event": EVENT_NAME, "value_optional": True}
    try:
        requests.post(url, json=payload)
    except requests.RequestException as e:
        print(f"[ERROR] Failed to register game event: {e}")

def bind_event():
    """
    Binds our custom event to the GameDAC's OLED screen using 'screened' device-type and zone 'one'.
    It allows us to send text directly to the screen using the 'value' field.
    """
    url = f"{sse_address}/bind_game_event"
    payload = {
        "game": GAME_NAME,
        "event": EVENT_NAME,
        "handlers": [
            {
                "device-type": "screened",
                "zone": "one",
                "mode": "screen",
                "datas": [{"has-text": True, "prefix": ""}],
            }
        ],
    }
    try:
        requests.post(url, json=payload)
    except requests.RequestException as e:
        print(f"[ERROR] Failed to bind game event: {e}")

def send_event(frames, delay=0.5):
    """
    Loops through the animation frames, sending each one as a game event to the GameDAC screen.
    Continues indefinitely until manually interrupted by the user.
    """
    print("Animating OLED.. Press Ctrl+C to stop.")
    try:
        while True:
            for frame in frames:
                url = f"{sse_address}/game_event"
                payload = {
                    "game": GAME_NAME,
                    "event": EVENT_NAME,
                    "data": {"value": frame},
                }
                try:
                    requests.post(url, json=payload)
                    time.sleep(delay)
                except requests.RequestException as e:
                    print(f"[ERROR] Fail to game event: {e}")
    except KeyboardInterrupt:
        print("[USER] Stopped the animation.")

# Entry point: set up and start animation if SSE is running
if __name__ == "__main__":
    sse_address = get_sse_address()
    if sse_address:
        register_game()
        register_event()
        bind_event()
        send_event(ANIMATED_FRAMES)
