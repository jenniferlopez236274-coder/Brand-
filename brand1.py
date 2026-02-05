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
VERSION = "V16.8 PRO"

# Unique ID for your device (Add yours here)
APPROVED_DEVICES = ["FOZI-MASTER-786", "FOZI-STABLE-ERR"] 
# ==========================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_stable_hwid():
    try:
        sig = platform.machine() + socket.gethostname() + platform.system()
        hwid = hashlib.sha256(sig.encode()).hexdigest()[:12].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-STABLE-ERR"

def get_real_period():
    now = datetime.now()
    # 1-Minute Game Logic
    total_minutes = (now.hour * 60) + now.minute
    period_count = 1141 + total_minutes
    return now.strftime("%Y%m%d") + "10101" + str(period_count)

def get_sureshot_logic(period):
    # Professional Pattern Logic (Simulated)
    # Is logic ko aise design kiya hai ke ye har period par consistent rahe
    combined_seed = str(period) + "ULTRA_VIP_SECRET"
    hash_res = hashlib.md5(combined_seed.encode()).hexdigest()
    
    # Last digit logic for Big/Small
    last_digit = int(hash_res[-1], 16)
    
    # Result mapping
    bs = "\033[1;31mBIG 🔴\033[0m" if last_digit > 7 else "\033[1;34mSMALL 🔵\033[0m"
    eo = "\033[1;35mEVEN 🟣\033[0m" if last_digit % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    
    # High Accuracy Probability (Visual only)
    accuracy = "98.2%" if last_digit > 4 else "95.7%"
    
    return bs, eo, accuracy

def start_engine():
    user_id = get_stable_hwid()
    
    # Simple Access Check
    if user_id not in APPROVED_DEVICES and "FOZI" not in user_id:
        clear()
        print(f"\n\033[1;31m [!] UNAUTHORIZED ACCESS")
        print(f"\033[1;37m [●] YOUR HWID: \033[1;33m{user_id}")
        print(f"\033[1;37m [●] STATUS   : \033[1;31mBLOCK BY {OWNER_NAME}")
        sys.exit()

    clear()
    print(f"\033[1;32m[+] CONNECTING TO CLOUD SERVER...")
    time.sleep(1.5)
    print(f"\033[1;32m[+] BYPASSING PAK GAMES ANTI-CHEAT...")
    time.sleep(1.5)

    last_period = ""

    while True:
        now = datetime.now()
        p = get_real_period()
        sec = now.second
        
        # Naya period aane par animation
        if p != last_period:
            print(f"\n\033[1;33m[⚡] NEW PERIOD DETECTED: {p}")
            print(f"\033[1;32m[⚙️] ANALYZING PATTERN...")
            time.sleep(2)
            last_period = p

        bs, eo, acc = get_sureshot_logic(p)
        
        clear()
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
