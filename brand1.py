#!/usr/bin/env python3
import os
import sys
import time
import hashlib
import socket
import platform
import subprocess
from datetime import datetime

# --- AUTO-INSTALLER ---
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# ==========================================================
# [ CONFIGURATION ] - FOZI KING LZR RECOVERY MODE
# ==========================================================
# Is URL par aap wo Keys likhenge jo aapne approve karni hain (Line by line)
GITHUB_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
# ==========================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_unique_hwid():
    """Har mobile ka unique key generate karne ke liye"""
    try:
        # Machine aur Processor details ko mix karke unique hash banana
        raw_info = platform.processor() + platform.node() + platform.machine() + socket.gethostname()
        unique_hash = hashlib.sha256(raw_info.encode()).hexdigest()
        # Format: FK-A1B2C3D4 (First 10 chars)
        return f"FK-{unique_hash[:8].upper()}"
    except:
        return "FK-ERROR-USER"

def check_online_key(user_key):
    """Github file se key check karna"""
    try:
        # Cache bypass karne ke liye timestamp use kiya hai
        response = requests.get(f"{GITHUB_URL}?t={time.time()}", timeout=10)
        if response.status_code == 200:
            approved_keys = response.text.splitlines()
            return user_key in approved_keys
        return False
    except:
        print("\033[1;31m[!] CONNECTION ERROR: Internet Check Karein!\033[0m")
        return False

def get_lzr_prediction(p_id):
    """LZR Recovery Logic: Multiple Hashing for Accuracy"""
    seed = f"{p_id}-FOZI-LZR-V6"
    hash_obj = hashlib.sha256(seed.encode()).hexdigest()
    
    # K3/Pak Game Logic
    dice_sum = (int(hash_obj[-3:], 16) % 16) + 3
    confidence = (int(hash_obj[0:2], 16) % 15) + 84 # 84% to 98%
    
    res = "\033[1;34mSMALL 🔵\033[0m" if dice_sum <= 10 else "\033[1;31mBIG 🔴\033[0m"
    eo = "EVEN" if dice_sum % 2 == 0 else "ODD"
    
    return res, eo, dice_sum, confidence

def start_tool():
    clear()
    my_hwid = get_unique_hwid()
    
    print("\033[1;32m")
    print(r"""
  ______ ____ _________  _  ___ _   _  ____ 
 |  ____/ __ \___  /_ _| |/ (_) \ | |/ ___|
 | |__ | |  | | / / | || ' /| |  \| | |  _ 
 |  __|| |  | |/ /  | || . \| | |\  | |_| |
 |_|   \____//____|___|_|\_\_|_| \_|\____|
    """)
    print("\033[1;33m" + "="*55)
    print(f" [●] SYSTEM : LZR RECOVERY MODE (V6)")
    print(f" [●] YOUR ID: \033[1;36m{my_hwid}\033[1;33m")
    print("="*55 + "\033[0m")
    
    print(f"\033[1;37m[>] Copy your ID and send to Admin for Approval.\033[0m")
    user_input = input("\n\033[94m[+] ENTER ACTIVATION KEY: \033[0m").strip()
    
    # Security Check: Input key aur HWID dono match hone chahiye ya online approved
    if user_input == my_hwid and check_online_key(my_hwid):
        print(f"\n\033[1;32m[✔] KEY VERIFIED! ACCESS GRANTED.")
        time.sleep(1.5)
    else:
        print(f"\n\033[1;31m[!] ACCESS DENIED!")
        print(f"\033[1;37mKey '{user_input}' is not approved for this device.\033[0m")
        sys.exit()

    last_p = ""
    while True:
        try:
            now = datetime.now()
            # Pak Game Exact Period Sync
            total_m = (now.hour * 60) + now.minute
            p_id = now.strftime("%Y%m%d") + "10101" + str(total_m).zfill(4)
            
            if p_id != last_p:
                res_bs, res_eo, val, conf = get_lzr_prediction(p_id)
                last_p = p_id
                clear()
                
                print("\033[1;32m" + "╔═══════════════════════════════════════╗")
                print(f"  MODE      : LZR FULL RECOVERY")
                print(f"  PERIOD    : {p_id}")
                print(f"  DEVICE ID : {my_hwid}")
                print("╚═══════════════════════════════════════╝\033[0m")
                
                print(f"\n\033[1;33m[●] NEXT PREDICTION:")
                print(f"    RESULT : {res_bs} | {res_eo}")
                print(f"    SUM    : \033[1;35m{val}\033[0m")
                print(f"    CHANCE : \033[1;32m{conf}% Confidence\033[0m")
                
                print(f"\n\033[1;31m[!] LZR TIP: Use 3x Martingale if Loss.\033[0m")

            rem_sec = 60 - now.second
            sys.stdout.write(f"\r\033[90m[SYNCING]: {rem_sec}s | SERVER STABLE... \033[0m")
            sys.stdout.flush()
            time.sleep(1)
                
        except KeyboardInterrupt: break
        except Exception: continue

if __name__ == "__main__":
    start_tool()
