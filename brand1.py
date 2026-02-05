import os
import sys
import time
import hashlib
from datetime import datetime

# --- AUTO-INSTALLER ---
try:
    import requests
except ImportError:
    os.system('pip install requests')
    import requests

# ==========================================================
# [ ADMIN CONTROL PANEL ] - FOZI KING OFFICIAL
# ==========================================================
OWNER_NAME = "FOZI KING"
VERSION = "V28.0 K3-SPECIAL"
GITHUB_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
# ==========================================================

history_list = []

def clear():
    os.system('clear' if os.name == 'nt' else 'clear')

def get_hwid():
    import platform, socket
    sig = platform.machine() + socket.gethostname() + platform.node()
    return f"FOZI-{hashlib.sha256(sig.encode()).hexdigest()[:10].upper()}"

def get_synced_period():
    now = datetime.now()
    total_minutes = (now.hour * 60) + now.minute
    # K3 1-Min standard base format
    base_code = "10101" 
    period = now.strftime("%Y%m%d") + base_code + f"{total_minutes:04d}"
    return period

def get_k3_logic(period):
    """
    K3 DICE LOGIC:
    Sum of 3 Dice (3-18)
    Small: 3-10 | Big: 11-18
    """
    seed = str(period) + "FOZI_K3_PREMIUM_999"
    hash_hex = hashlib.sha256(seed.encode()).hexdigest()
    
    # Dice sum generation (3 to 18 range)
    # Hum hash se 3 alag numbers nikalte hain (Dice 1, 2, 3)
    d1 = (int(hash_hex[0:2], 16) % 6) + 1
    d2 = (int(hash_hex[2:4], 16) % 6) + 1
    d3 = (int(hash_hex[4:6], 16) % 6) + 1
    
    total_sum = d1 + d2 + d3
    
    # K3 Rules Mapping
    if total_sum <= 10:
        bs = "\033[1;34mSMALL 🔵\033[0m"
    else:
        bs = "\033[1;31mBIG 🔴\033[0m"
        
    eo = "\033[1;35mEVEN 🟣\033[0m" if total_sum % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    
    return bs, eo, total_sum, (d1, d2, d3)

def start_engine():
    hwid = get_hwid()
    raw_key = hwid + "FOZI_KING_POWER_999"
    my_key = "FOZI-" + hashlib.md5(raw_key.encode()).hexdigest()[:8].upper()
    
    # Approval Check from GitHub
    try:
        res = requests.get(GITHUB_URL + f"?t={time.time()}", timeout=10).text
        if my_key not in res:
            clear()
            print(f"\033[1;31m[!] ACCESS DENIED! CONTACT FOZI KING")
            print(f"\033[1;37m[●] YOUR KEY: \033[1;32m{my_key}")
            sys.exit()
    except:
        pass

    last_p = ""
    while True:
        try:
            current_p = get_synced_period()
            sec = datetime.now().second
            
            if current_p != last_p:
                if last_p != "":
                    h_bs, h_eo, h_sum, h_dice = get_k3_logic(last_p)
                    history_list.insert(0, f"P: {last_p[-4:]} ➔ {h_bs} | Sum: {h_sum} | {h_eo}")
                    if len(history_list) > 6: history_list.pop()
                last_p = current_p

            bs, eo, total_sum, dice = get_k3_logic(current_p)

            clear()
            print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║           👑 {OWNER_NAME} K3 PREDICTOR 👑          ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f" \033[1;37m[●] GAME TYPE : \033[1;32mK3 LOTTERY (3-DICE)")
            print(f" \033[1;37m[●] LIVE PERIOD: \033[1;33m{current_p}")
            print("\033[1;32m" + "━"*58 + "\033[0m")

            print(f"\n   \033[1;33m🎲 K3 100% VIP TARGET:")
            print(f"   \033[1;37m[PREDICTION] : {bs}")
            print(f"   \033[1;37m[DICE SUM]   : \033[1;32m{total_sum}")
            print(f"   \033[1;37m[DICE LOOK]  : \033[1;36m{dice[0]} + {dice[1]} + {dice[2]}")
            print(f"   \033[1;37m[SIDE TYPE]  : {eo}")

            print("\033[1;32m\n" + "━"*15 + " [ K3 RECENT HISTORY ] " + "━"*20 + "\033[0m")
            if not history_list:
                print("   \033[1;30mSyncing with live K3 server data...")
            else:
                for line in history_list:
                    print(f"   {line}")

            rem_s = 60 - sec
            color = "\033[1;32m" if rem_s > 10 else "\033[1;31m"
            print(f"\n {color}[⏳] NEXT DRAW IN: {rem_s}s \033[0m")
            
            time.sleep(1)
        except Exception:
            time.sleep(1)

if __name__ == "__main__":
    start_engine()
