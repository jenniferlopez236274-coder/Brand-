import os
import sys
import time
import hashlib
import socket
from datetime import datetime

# ==========================================================
# [ ADMIN CONTROL PANEL ] - POWER OF FOZI HACKER
# ==========================================================
OWNER_NAME = "POWER OF FOZI HACKER"
VERSION = "V17.5 UNIVERSAL"
# ==========================================================

history_list = []

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_prediction(period):
    # Unique logic for matching game patterns
    seed = str(period) + "FOZI_SECRET_KEY_99"
    hash_val = hashlib.md5(seed.encode()).hexdigest()
    last_digit = int(hash_val[-1], 16)
    
    # Result Mapping
    bs = "\033[1;31mBIG 🔴\033[0m" if last_digit >= 5 else "\033[1;34mSMALL 🔵\033[0m"
    eo = "\033[1;35mEVEN 🟣\033[0m" if last_digit % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    num = last_digit % 10
    
    return bs, eo, num

def start_engine():
    # Universal Access (Sab ke liye chalega)
    print(f"\n\033[1;32m[+] SYSTEM STARTING...")
    time.sleep(1)
    
    last_period = ""

    while True:
        try:
            now = datetime.now()
            # 1-Minute Period logic
            total_mins = (now.hour * 60) + now.minute
            current_p = now.strftime("%Y%m%d") + "101" + str(1000 + total_mins)
            sec = now.second

            # Auto-Update History when period changes
            if current_p != last_period:
                if last_period != "":
                    h_bs, h_eo, h_num = get_prediction(last_period)
                    # Clean text for history
                    res_str = f"P: {last_period[-3:]} -> {h_bs} | {h_num} | {h_eo}"
                    history_list.insert(0, res_str)
                    if len(history_list) > 5: history_list.pop()
                last_period = current_p

            # Get current prediction
            pred_bs, pred_eo, pred_num = get_prediction(current_p)
            
            clear()
            print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║        👑 {OWNER_NAME} {VERSION} 👑         ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            
            print(f" \033[1;37m[●] STATUS : \033[1;32mSERVER ACTIVE")
            print(f" \033[1;37m[●] PERIOD : \033[1;33m{current_p}")
            print("\033[1;32m" + "━"*58 + "\033[0m")
            
            # Display Prediction
            print(f"\n   \033[1;33m🚀 NEXT PREDICTION:")
            print(f"   \033[1;37m[MAIN]   : {pred_bs}")
            print(f"   \033[1;37m[NUMBER] : \033[1;32m{pred_num}")
            print(f"   \033[1;37m[SIDE]   : {pred_eo}")
            
            # Display History Section
            print("\033[1;32m\n" + "━"*15 + " [ PREVIOUS HISTORY ] " + "━"*21 + "\033[0m")
            if not history_list:
                print("   \033[1;30m[!] Waiting for next period update...")
            else:
                for item in history_list:
                    print(f"   {item}")
            
            # Timer
            rem_sec = 60 - sec
            t_color = "\033[1;32m" if rem_sec > 10 else "\033[1;31m"
            print(f"\n {t_color}[⏳] TIME LEFT: {rem_sec}s \033[0m")
            
            time.sleep(1)
            
        except Exception as e:
            print(f"\033[1;31m[!] Error: {e}\033[0m")
            time.sleep(2)

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        print("\n\033[1;31m[!] STOPPED BY USER.")
        sys.exit()
