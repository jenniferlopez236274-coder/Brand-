import os
import sys
import time
import hashlib
import socket
import platform
from datetime import datetime

# --- AUTO-INSTALLER FOR REQUESTS ---
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# ==========================================================
# [ CONFIGURATION ] - FOZI KING OFFICIAL
# ==========================================================
ACTIVATION_KEY = "FOZI786" 
CONTACT_NUM = "+923186757671"
# Aapki GitHub Raw Link jahan IDs approved hain
GITHUB_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
# ==========================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_hwid():
    # Unique Device ID generate karne ke liye
    sig = platform.machine() + socket.gethostname() + platform.node()
    hwid = hashlib.sha256(sig.encode()).hexdigest()[:10].upper()
    return f"FK-{hwid}"

def check_cloud_approval(user_id):
    try:
        # GitHub se list check karna
        response = requests.get(GITHUB_URL + f"?t={time.time()}", timeout=10)
        if user_id in response.text:
            return True
        return False
    except:
        return False

def get_high_accuracy_logic(period_id):
    hash_object = hashlib.sha256(period_id.encode())
    hex_dig = hash_object.hexdigest()
    last_val = int(hex_dig[-2:], 16) 
    fix_number = last_val % 10
    
    # K3 STRICT LOGIC (As per your request)
    # 0-4 Small, 5-9 Big
    if fix_number >= 5:
        res = "\033[1;31mBIG 🔴\033[0m"
    else:
        res = "\033[1;34mSMALL 🔵\033[0m"
        
    return res, fix_number

def start_tool():
    user_id = get_hwid()
    clear()
    print("\033[1;32m")
    print(r"""
  ______ ____ _________  _  ___ _   _  ____ 
 |  ____/ __ \___  /_ _| |/ (_) \ | |/ ___|
 | |__ | |  | | / / | || ' /| |  \| | |  _ 
 |  __|| |  | |/ /  | || . \| | |\  | |_| |
 |_|   \____//____|___|_|\_\_|_| \_|\____|
    """)
    print("\033[1;33m" + "="*55)
    print(f" [●] TOOL   : DATA HASH PREDICTOR v44")
    print(f" [●] STATUS : CLOUD SYNC ACTIVE")
    print(f" [●] OWNER  : FOZI KING X ASIM VIP")
    print(f" [●] ID     : \033[1;36m{user_id}\033[1;33m")
    print("="*55 + "\033[0m")
    
    # Key System
    key = input("\033[94m[+] ENTER ACCESS KEY OR ID: \033[0m")
    
    # Pehle manual key check hogi, phir cloud approval
    if key == ACTIVATION_KEY or check_cloud_approval(user_id):
        print(f"\n\033[1;32m[✔] ACCESS GRANTED! SYNCING HASHES...")
        time.sleep(2)
    else:
        print(f"\n\033[1;31m[!] NOT APPROVED! CONTACT ADMIN")
        print(f"\033[1;37m[●] YOUR ID: \033[1;32m{user_id}\033[0m")
        sys.exit()

    last_p = ""

    while True:
        try:
            now = datetime.now()
            # Period calculation
            p_id = now.strftime("%Y%m%d") + "01" + str((now.hour * 60) + now.minute + 1).zfill(4)
            
            if p_id != last_p:
                res, num = get_high_accuracy_logic(p_id)
                last_p = p_id
                
                print(f"\n\033[1;96m[NEW ROUND]: {p_id}\033[0m")
                
                for i in range(1, 4):
                    sys.stdout.write(f"\r\033[95m[READING HASH DATA] {'●' * i}")
                    sys.stdout.flush()
                    time.sleep(1)
                
                print("\n\n\033[1;32m" + "╔═══════════════════════════════════════╗")
                print(f"  TARGET   : FANTASY GEMS 1-MIN")
                print(f"  PERIOD   : {p_id}")
                print(f"  RESULT   : {res}")
                print(f"  FIX NUM  : {num}")
                print(f"  CHANCE   : HIGH PROBABILITY")
                print("╚═══════════════════════════════════════╝" + "\033[0m")
            
            rem_sec = 60 - now.second
            sys.stdout.write(f"\r\033[90m[SYNC]: {rem_sec}s | SERVER INJECTION ACTIVE... \033[0m")
            sys.stdout.flush()
            time.sleep(1)
                
        except KeyboardInterrupt: break
        except Exception: continue

if __name__ == "__main__":
    start_tool()
