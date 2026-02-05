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
CONTACT_NO = "+923186757671"
VERSION = "V18.0 KEY-LOCK"

# Secret Salt: Isko change mat karna, ye key generate karne ke liye hai
SECRET_SALT = "FOZI_PREMIUM_889" 
# ==========================================================

history_list = []

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_stable_hwid():
    try:
        # Device ki unique information se HWID banana
        sig = platform.machine() + socket.gethostname() + platform.node()
        hwid = hashlib.sha256(sig.encode()).hexdigest()[:10].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-USER-ERR"

def generate_key_from_hwid(hwid):
    # HWID aur Secret Salt ko mila kar unique key banana
    raw_key = hwid + SECRET_SALT
    valid_key = hashlib.md5(raw_key.encode()).hexdigest()[:8].upper()
    return f"KEY-{valid_key}"

def get_prediction(period):
    seed = str(period) + "FOZI_ULTRA_SURE"
    hash_val = hashlib.sha256(seed.encode()).hexdigest()
    val = int(hash_val[-1], 16)
    
    bs = "\033[1;31mBIG 🔴\033[0m" if val >= 8 else "\033[1;34mSMALL 🔵\033[0m"
    eo = "\033[1;35mEVEN 🟣\033[0m" if val % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    num = val % 10
    return bs, eo, num

def login():
    hwid = get_stable_hwid()
    correct_key = generate_key_from_hwid(hwid)
    
    while True:
        clear()
        print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
        print(f"║        👑 {OWNER_NAME} KEY SYSTEM 👑         ║")
        print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
        print(f"\n \033[1;37m[●] YOUR HWID : \033[1;36m{hwid}")
        print(f" \033[1;37m[●] STATUS    : \033[1;31mLICENSE EXPIRED / NO KEY")
        print(f"\033[1;32m" + "─"*58 + "\033[0m")
        print(f"\n \033[1;33m[!] Note: Send your HWID to Admin for Activation Key.")
        print(f" \033[1;32m[#] Admin Contact: {CONTACT_NO}")
        
        user_key = input(f"\n \033[1;37m[+] ENTER YOUR KEY: \033[1;32m").strip()
        
        if user_key == correct_key:
            print(f"\n \033[1;32m[✓] ACCESS GRANTED! INITIALIZING...")
            time.sleep(2)
            break
        else:
            print(f"\n \033[1;31m[X] INVALID KEY! TRY AGAIN.")
            time.sleep(2)

def start_engine():
    login()
    last_period = ""

    while True:
        now = datetime.now()
        sec = now.second
        total_minutes = (now.hour * 60) + now.minute
        current_p = now.strftime("%Y%m%d") + "10101" + str(1141 + total_minutes)
        
        # History Update Logic
        if current_p != last_period:
            if last_period != "":
                h_bs, h_eo, h_num = get_prediction(last_period)
                res_str = f"P: {last_period[-3:]} -> {h_bs} | {h_num} | {h_eo}"
                history_list.insert(0, res_str)
                if len(history_list) > 5: history_list.pop()
            last_period = current_p

        bs, eo, num = get_prediction(current_p)
        
        clear()
        print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
        print(f"║        👑 {OWNER_NAME} {VERSION} 👑         ║")
        print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
        print(f" \033[1;37m[#] GAME     : \033[1;32mK3 1-MINUTE")
        print(f" \033[1;37m[#] PERIOD   : \033[1;33m{current_p}")
        print(f" \033[1;37m[#] SYSTEM   : \033[1;32mVIP PREMIUM ACTIVE")
        print("\033[1;32m" + "─"*58 + "\033[0m")
        
        print(f"\n \033[1;33m[⚡] PREDICTION:")
        print(f" \033[1;37m[RESULT] : {bs}")
        print(f" \033[1;37m[NUMBER] : \033[1;32m{num}")
        print(f" \033[1;37m[TYPE]   : {eo}")
        
        print("\033[1;32m\n" + "─"*15 + " [ PREVIOUS HISTORY ] " + "─"*21 + "\033[0m")
        if not history_list:
            print("   \033[1;30mFetching server data...")
        for h in history_list:
            print(f"   {h}")
            
        rem_sec = 60 - sec
        color = "\033[1;32m" if rem_sec > 10 else "\033[1;31m"
        print(f"\n {color}[⏳] TIME LEFT: {rem_sec}s \033[0m")
        
        time.sleep(1)

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        sys.exit()
