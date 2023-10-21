import keyboard
from ROMS import tetris
import os

load: str = None
ROMS = [
    "tetris"
]
ROM: int = 0
while True:
    if load is None:
        print(f"""
        >{ROMS[ROM]}<

        -- q - next game --
        """)
