import os
import sys
import time
import hashlib
import socket
import platform
from datetime import datetime

# --- AUTO-FIX FOR REQUESTS ERROR ---
try:
    import requests
except ImportError:
    print("\033[1;33m[!] 'requests' module nahi mila. Install kar raha hoon...\033[0m")
    os.system('pip install requests')
    import requests
# ----------------------------------

# ==========================================================
# [ ADMIN CONTROL PANEL ] - FOZI KING OFFICIAL
# ==========================================================
OWNER_NAME = "FOZI KING"
CONTACT_NO = "+923186757671"
VERSION = "V23.0 ULTIMATE"

# GitHub Link for Approval
GITHUB_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
# ==========================================================

history_list = []

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_hwid():
    try:
        sig = platform.machine() + socket.gethostname() + platform.node()
        hwid = hashlib.sha256(sig.encode()).hexdigest()[:12].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-ERR-ID"

def check_approval(user_id):
    try:
        # Cache busting taake latest approval foran mile
        url = f"{GITHUB_URL}?t={int(time.time())}"
        response = requests.get(url, timeout=10)
        return user_id in response.text
    except:
        return False

def bypass_animation():
    clear()
    frames = ["[■□□□□□□□□□]", "[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", 
              "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", 
              "[■■■■■■■■■□]", "[■■■■■■■■■■]"]
    
    print(f"\033[1;32m[+] CONNECTING TO FOZI CLOUD...")
    time.sleep(1)
    for frame in frames:
        clear()
        print(f"\n\033[1;32m      👑 {OWNER_NAME} SYSTEM 👑")
        print(f"\n\033[1;37m[#] BYPASSING PAK GAMES ANTI-CHEAT...")
        print(f"\033[1;32m    {frame} 100%")
        print(f"\033[1;37m[#] LOADING VIP PATTERNS...")
        time.sleep(0.2)
    print(f"\033[1;32m[✓] INJECTION SUCCESSFUL!")
    time.sleep(1)

def get_prediction(period):
    seed = str(period) + "FOZI_PREMIUM_SECURE_99"
    h = hashlib.sha256(seed.encode()).hexdigest()
    val = int(h[-1], 16)
    
    bs = "\033[1;31mBIG 🔴\033[0m" if val >= 8 else "\033[1;34mSMALL 🔵\033[0m"
    eo = "\033[1;35mEVEN 🟣\033[0m" if val % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    num = val % 10
    return bs, eo, num

def start_engine():
    user_id = get_hwid()
    
    # Login Check
    while True:
        clear()
        print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
        print(f"║          👑 {OWNER_NAME} CLOUD SYSTEM 👑          ║")
        print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
        print(f"\n \033[1;37m[●] YOUR DEVICE ID : \033[1;36m{user_id}")
        print(f" \033[1;37m[●] STATUS         : \033[1;31mCHECKING APPROVAL...")
        
        if check_approval(user_id):
            bypass_animation()
            break
        else:
            print(f"\n \033[1;31m [X] ACCESS DENIED: ID NOT APPROVED")
            print(f" \033[1;32m [#] Send ID to Admin: {CONTACT_NO}")
            input(f"\n \033[1;33m Press Enter to refresh approval...")

    last_p = ""
    while True:
        try:
            now = datetime.now()
            sec = now.second
            total_min = (now.hour * 60) + now.minute
            current_p = now.strftime("%Y%m%d") + "10101" + str(1141 + total_min)

            if current_p != last_p:
                if last_p != "":
                    h_bs, h_eo, h_num = get_prediction(last_p)
                    history_list.insert(0, f"P: {last_p[-3:]} ➔ {h_bs} | {h_num} | {h_eo}")
                    if len(history_list) > 5: history_list.pop()
                last_p = current_p

            bs, eo, num = get_prediction(current_p)

            clear()
            print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║           👑 {OWNER_NAME} OFFICIAL 👑            ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f" \033[1;37m[●] SERVER   : \033[1;32mPAK GAMES (ENCRYPTED)")
            print(f" \033[1;37m[●] PERIOD   : \033[1;33m{current_p}")
            print("\033[1;32m" + "━"*58 + "\033[0m")

            print(f"\n   \033[1;33m🎯 TARGET PREDICTION (100%):")
            print(f"   \033[1;37m[MAIN]   : {bs}")
            print(f"   \033[1;37m[NUMBER] : \033[1;32m{num}")
            print(f"   \033[1;37m[SIDE]   : {eo}")

            print("\033[1;32m\n" + "━"*15 + " [ PREVIOUS RESULTS ] " + "━"*21 + "\033[0m")
            if not history_list:
                print("   \033[1;30mSyncing cloud database...")
            else:
                for line in history_list:
                    print(f"   {line}")

            rem_s = 60 - sec
            color = "\033[1;32m" if rem_s > 10 else "\033[1;31m"
            print(f"\n {color}[⏳] REMAINING: {rem_s}s \033[0m")
            
            time.sleep(1)
        except Exception:
            pass

if __name__ == "__main__":
    start_engine()
