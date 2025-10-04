import os
import subprocess

import platform
from colorama import Fore, Style, init
init(autoreset=True)

if platform.system() == "Windows":
    SPELLS = {
        "lumos": "dir",
        "obliviate": "cls",
        "accio": "mkdir",
        "confringo": "del",
        "wingardium_leviosa": "move",
        "horcrux": "copy",
    }
else:  # Linux / Mac
    SPELLS = {
        "lumos": "ls",
        "obliviate": "clear",
        "accio": "mkdir",
        "confringo": "rm",
        "wingardium_leviosa": "mv",
        "horcrux": "cp",
    }


def cast_spell(spell, *args):
    if spell == "spells":
        print(Fore.CYAN + "📜 Available spells:")
        for s, c in SPELLS.items():
            print(f"   🪄{ s} → {c}")
        return
    if spell not in SPELLS:
        print(Fore.RED + f"⚡ Unknown spell: {spell}")
        return
    command = SPELLS[spell] + " " + " ".join(args)
    subprocess.run(command, shell=True)

def list_spells():
    print("📜 Available Spells:")
    for spell, cmd in SPELLS.items():
        print(f"   🪄 {spell} → {cmd}")



def main():
    print(Fore.YELLOW + "⚡ Welcome to Magic Terminal!")
    print(Fore.BLUE + "Type 'spells' to see available spells.")

    print(Fore.CYAN + "Type 'nox' to leave." + Style.RESET_ALL)
    while True:
        user_input = input("🪄 cast: ").strip().split()
        if not user_input:
            continue
        spell = user_input[0]
        if spell in ("nox", "exit"):
            print("✨ Mischief managed.")
            break
        cast_spell(spell, *user_input[1:])

if __name__ == "__main__":
    main()
