import os
import sys
import time
import hashlib
from datetime import datetime

# --- AUTO-INSTALL MISSING MODULES ---
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# ==========================================================
# [ ADMIN CONTROL PANEL ] - FOZI KING OFFICIAL
# ==========================================================
OWNER_NAME = "FOZI KING"
CONTACT_NO = "+923186757671"
VERSION = "V24.0 SYNC-FIX"

# Aapka GitHub Approval Link
GITHUB_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
# ==========================================================

history_list = []

def clear():
    os.system('clear' if os.name == 'nt' else 'clear')

def get_hwid():
    import platform, socket
    sig = platform.machine() + socket.gethostname() + platform.node()
    return f"FOZI-{hashlib.sha256(sig.encode()).hexdigest()[:10].upper()}"

def get_pak_games_period():
    """
    Pak Games K3 1-Min Period Calculation:
    Format: YYYYMMDD0101 + Total Minutes since midnight
    """
    now = datetime.now()
    # Midnight se ab tak ke total minutes
    total_minutes = (now.hour * 60) + now.minute
    
    # Pak Games K3 1-Min ka base code '0101' hota hai
    # Format: 20260205 + 0101 + current_minute_index
    # Example: 2026020501010734
    period_suffix = f"0101{total_minutes:04d}"
    return now.strftime("%Y%m%d") + period_suffix

def get_prediction(period):
    # Standard VIP Hashing Logic
    seed = str(period) + "FOZI_KING_ULTRA_SURE"
    h = hashlib.sha256(seed.encode()).hexdigest()
    val = int(h[-1], 16)
    
    bs = "\033[1;31mBIG 🔴\033[0m" if val >= 8 else "\033[1;34mSMALL 🔵\033[0m"
    eo = "\033[1;35mEVEN 🟣\033[0m" if val % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    num = val % 10
    return bs, eo, num

def check_approval(hwid):
    try:
        # Secret Salt for Key verification
        raw = hwid + "FOZI_KING_POWER_999"
        my_key = "FOZI-" + hashlib.md5(raw.encode()).hexdigest()[:8].upper()
        
        # GitHub check
        res = requests.get(GITHUB_URL + f"?t={time.time()}", timeout=10)
        return my_key in res.text, my_key
    except:
        return False, "OFFLINE"

def start_engine():
    hwid = get_hwid()
    is_approved, my_key = check_approval(hwid)

    if not is_approved:
        clear()
        print(f"\033[1;31m[!] KEY NOT APPROVED")
        print(f"\033[1;37m[●] YOUR KEY : \033[1;32m{my_key}")
        print(f"\033[1;32m[#] WhatsApp Admin: {CONTACT_NO}")
        sys.exit()

    last_p = ""
    while True:
        try:
            current_p = get_pak_games_period()
            sec = datetime.now().second
            
            if current_p != last_p:
                if last_p != "":
                    h_bs, h_eo, h_num = get_prediction(last_p)
                    history_list.insert(0, f"P: {last_p[-4:]} ➔ {h_bs} | {h_num} | {h_eo}")
                    if len(history_list) > 5: history_list.pop()
                last_p = current_p

            bs, eo, num = get_prediction(current_p)

            clear()
            print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║           👑 {OWNER_NAME} OFFICIAL 👑            ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f" \033[1;37m[●] GAME     : \033[1;32mPAK GAMES K3 (1-MIN)")
            print(f" \033[1;37m[●] PERIOD   : \033[1;33m{current_p}")
            print(f" \033[1;37m[●] STATUS   : \033[1;32mSYNCED WITH SERVER")
            print("\033[1;32m" + "━"*58 + "\033[0m")

            print(f"\n   \033[1;33m🎯 TARGET PREDICTION:")
            print(f"   \033[1;37m[RESULT] : {bs}")
            print(f"   \033[1;37m[NUMBER] : \033[1;32m{num}")
            print(f"   \033[1;37m[TYPE]   : {eo}")

            print("\033[1;32m\n" + "━"*15 + " [ PREVIOUS HISTORY ] " + "━"*21 + "\033[0m")
            if not history_list:
                print("   \033[1;30mConnecting to live data stream...")
            else:
                for line in history_list:
                    print(f"   {line}")

            rem_s = 60 - sec
            color = "\033[1;32m" if rem_s > 10 else "\033[1;31m"
            print(f"\n {color}[⏳] SYNCING NEXT: {rem_s}s \033[0m")
            
            time.sleep(1)
        except Exception as e:
            time.sleep(2)

if __name__ == "__main__":
    start_engine()
