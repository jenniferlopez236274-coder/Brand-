import os
import sys
import time
import hashlib
import socket
import platform
from datetime import datetime

# ==========================================================
# [ ADMIN CONTROL PANEL ] - POWER OF FOZI HACKER
# ==========================================================
OWNER_NAME = "POWER OF FOZI HACKER"
VERSION = "V17.0 PRO"
# ==========================================================

# History ko store karne ke liye list
history_list = []

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_stable_hwid():
    try:
        sig = platform.machine() + socket.gethostname() + platform.system()
        hwid = hashlib.sha256(sig.encode()).hexdigest()[:12].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-STABLE-ERR"

def get_prediction(period):
    """Har period ke liye fix calculation"""
    seed = str(period) + "FOZI_SECRET_KEY_99"
    hash_val = hashlib.md5(seed.encode()).hexdigest()
    last_digit = int(hash_val[-1], 16)
    
    # Game Logic
    bs = "BIG 🔴" if last_digit >= 5 else "SMALL 🔵"
    eo = "EVEN 🟣" if last_digit % 2 == 0 else "ODD ⚪"
    num = last_digit % 10
    
    return bs, eo, num

def start_engine():
    user_id = get_stable_hwid()
    last_period = ""

    while True:
        now = datetime.now()
        # 1-Minute Period Calculation
        total_mins = (now.hour * 60) + now.minute
        current_p = now.strftime("%Y%m%d") + "1000" + str(1000 + total_mins)
        sec = now.second

        # Jab period change ho toh history update karein
        if current_p != last_period:
            if last_period != "":
                h_bs, h_eo, h_num = get_prediction(last_period)
                res_str = f"P: {last_period[-3:]} -> {h_bs} | {h_num} | {h_eo}"
                history_list.insert(0, res_str)
                if len(history_list) > 5: history_list.pop()
            last_period = current_p

        # Current Prediction
        pred_bs, pred_eo, pred_num = get_prediction(current_p)
        
        clear()
        print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
        print(f"║        👑 {OWNER_NAME} {VERSION} 👑         ║")
        print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
        
        print(f" \033[1;37m[●] HWID   : \033[1;33m{user_id}")
        print(f" \033[1;37m[●] PERIOD : \033[1;36m{current_p}")
        print("\033[1;32m" + "━"*58 + "\033[0m")
        
        # Next Prediction Display
        print(f"\n   \033[1;33m🚀 NEXT PREDICTION:")
        print(f"   \033[1;37m[MAIN]   : \033[1;32m{pred_bs}")
        print(f"   \033[1;37m[NUMBER] : \033[1;32m{pred_num}")
        print(f"   \033[1;37m[SIDE]   : \033[1;32m{pred_eo}")
        
        # History Display
        print("\033[1;32m\n" + "━"*15 + " [ PREVIOUS RESULTS ] " + "━"*21 + "\033[0m")
        if not history_list:
            print("   \033[1;30m[!] Waiting for data sync...")
        else:
            for item in history_list:
                print(f"   \033[1;37m{item}")
        
        # Timer logic
        rem_sec = 60 - sec
        t_color = "\033[1;32m" if rem_sec > 10 else "\033[1;31m"
        print(f"\n {t_color}[⏳] TIME LEFT: {rem_sec}s \033[0m")
        
        time.sleep(1)

if __name__ == "__main__":
    try:
        start_engine()
    except Exception as e:
        print(f"Error: {e}")
    except KeyboardInterrupt:
        sys.exit()        clear()
        print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
        print(f"║        👑 {OWNER_NAME} {VERSION} 👑         ║")
        print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
        
        print(f" \033[1;37m[●] SERVER STATUS : \033[1;32mONLINE (STABLE)")
        print(f" \033[1;37m[●] CURRENT GAME  : \033[1;36mK3 1-MINUTE")
        print(f" \033[1;37m[●] ACTIVE PERIOD : \033[1;33m{p}")
        print("\033[1;32m" + "━"*58 + "\033[0m")
        
        print(f"\n\033[1;37m   🎯 PREDICTION RESULT:")
        print(f"   \033[1;32m-----------------------")
        print(f"   \033[1;37m[MAIN]   : {bs}")
        print(f"   \033[1;37m[SIDE]   : {eo}")
        print(f"   \033[1;37m[CONF.]  : \033[1;32m{acc}")
        print(f"   \033[1;32m-----------------------")
        
        # Countdown Timer
        rem_sec = 60 - sec
        color = "\033[1;32m" if rem_sec > 15 else "\033[1;31m"
        print(f"\n {color}[⏳] TIME LEFT: {rem_sec}s \033[0m")
        
        if rem_sec <= 3:
            print(f"\n\033[1;33m [!] FETCHING NEXT RESULT...")
            time.sleep(3)

        print("\033[1;32m\n" + "═"*58 + "\033[0m")
        time.sleep(1)

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] ENGINE STOPPED BY USER.")
        sys.exit()
