#!/usr/bin/env python3
import os
import sys
import time
import hashlib
import socket
import platform
from datetime import datetime

# --- AUTO-INSTALLER ---
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# ==========================================================
# [ CONFIGURATION ]
# ==========================================================
GITHUB_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
ADMIN_NUMBER = "923207706955" 
# ==========================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_unique_hwid():
    try:
        raw_info = platform.processor() + platform.node() + platform.machine() + socket.gethostname()
        unique_hash = hashlib.sha256(raw_info.encode()).hexdigest()
        return f"FK-{unique_hash[:8].upper()}"
    except:
        return "FK-ERROR-USER"

def force_whatsapp_redirect(hwid):
    """Deep Linking for Android and Termux"""
    msg = f"Assalam-o-Alaikum Admin, Please Approve My Key.\n\nMY KEY: {hwid}"
    encoded_msg = msg.replace(" ", "%20").replace("\n", "%0A")
    # Universal WhatsApp link
    url = f"https://api.whatsapp.com/send?phone={ADMIN_NUMBER}&text={encoded_msg}"
    
    print(f"\n\033[1;33m[→] REDIRECTING TO WHATSAPP... PLEASE WAIT\033[0m")
    time.sleep(2)

    # 1. Sabse pehle Android ka system command try karein (Termux ke liye best hai)
    try:
        os.system(f"am start -a android.intent.action.VIEW -d '{url}' > /dev/null 2>&1")
    except:
        pass

    # 2. Agar upar wala fail ho toh termux-open use karein
    os.system(f"termux-open '{url}' > /dev/null 2>&1")
    
    # 3. Agar kuch bhi kaam na kare toh link print kar dein takay user click kar sakay
    print(f"\n\033[1;36m[!] AGAR AUTO OPEN NA HO TO IS LINK PAR CLICK KAREIN:\033[0m")
    print(f"\033[4;34m{url}\033[0m\n")

def check_online_key(user_key):
    try:
        response = requests.get(f"{GITHUB_URL}?t={time.time()}", timeout=10)
        if response.status_code == 200:
            approved_keys = response.text.splitlines()
            return user_key in approved_keys
        return False
    except:
        return False

def get_lzr_prediction(p_id):
    seed = f"{p_id}-FOZI-LZR-V6"
    hash_obj = hashlib.sha256(seed.encode()).hexdigest()
    dice_sum = (int(hash_obj[-3:], 16) % 16) + 3
    confidence = (int(hash_obj[0:2], 16) % 15) + 84 
    res = "SMALL 🔵" if dice_sum <= 10 else "BIG 🔴"
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
    print(f" [●] ADMIN   : FOZI KING")
    print(f" [●] CONTACT : \033[1;32m+{ADMIN_NUMBER}\033[1;33m")
    print(f" [●] YOUR ID : \033[1;36m{my_hwid}\033[1;33m")
    print("="*55 + "\033[0m")
    
    user_input = input("\n\033[94m[+] ENTER ACTIVATION KEY: \033[0m").strip()
    
    if user_input == my_hwid and check_online_key(my_hwid):
        print(f"\n\033[1;32m[✔] KEY VERIFIED! ACCESS GRANTED.")
        time.sleep(1.5)
    else:
        # Redirect trigger
        force_whatsapp_redirect(my_hwid)
        # 5 second wait takay user link dekh sakay
        time.sleep(5)
        sys.exit()

    last_p = ""
    while True:
        try:
            now = datetime.now()
            total_m = (now.hour * 60) + now.minute
            p_id = now.strftime("%Y%m%d") + "10101" + str(total_m).zfill(4)
            
            if p_id != last_p:
                res_bs, res_eo, val, conf = get_lzr_prediction(p_id)
                last_p = p_id
                clear()
                
                print("\033[1;32m" + "╔═══════════════════════════════════════╗")
                print(f"  MODE      : LZR FULL RECOVERY")
                print(f"  PERIOD    : {p_id}")
                print(f"  ADMIN WA  : +{ADMIN_NUMBER}")
                print("╚═══════════════════════════════════════╝\033[0m")
                
                print(f"\n\033[1;33m[●] NEXT PREDICTION:")
                print(f"    RESULT : {res_bs} | {res_eo}")
                print(f"    SUM    : {val}")
                print(f"    CHANCE : {conf}% Confidence")
                
                print(f"\n\033[1;31m[!] LZR TIP: Use 3x Martingale if Loss.\033[0m")

            rem_sec = 60 - now.second
            sys.stdout.write(f"\r\033[90m[SYNCING]: {rem_sec}s | SERVER STABLE... \033[0m")
            sys.stdout.flush()
            time.sleep(1)
        except KeyboardInterrupt: break
        except Exception: continue

if __name__ == "__main__":
    start_tool()
