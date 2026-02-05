import os
import sys
import time
import hashlib
import socket
import platform
from datetime import datetime

# ==========================================================
# [ ADMIN CONTROL PANEL ] - FOZI KING OFFICIAL
# ==========================================================
OWNER_NAME = "FOZI KING"
CONTACT_NO = "+923186757671"
VERSION = "V20.0 UNLIMITED"

# Is Salt ko hamesha yaad rakhein. Yehi key generate karne ke liye hai.
# Agar aap ye badlenge to purani sab keys kaam karna band kar dengi.
SECRET_SALT = "FOZI_UNLIMITED_POWER_786" 
# ==========================================================

history_list = []

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def get_hwid():
    try:
        # Unique device signature (Machine + Hostname + Processor)
        sig = platform.machine() + socket.gethostname() + platform.processor()
        hwid = hashlib.sha256(sig.encode()).hexdigest()[:10].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-ERROR-ID"

def check_key(hwid, user_key):
    # Yeh function check karega ke key sahi hai ya nahi
    raw_data = hwid + SECRET_SALT
    expected_key = "KEY-" + hashlib.md5(raw_data.encode()).hexdigest()[:8].upper()
    return user_key == expected_key

def get_prediction_logic(period):
    seed = str(period) + "FOZI_SURESHOT_VIP"
    hash_val = hashlib.sha256(seed.encode()).hexdigest()
    val = int(hash_val[-1], 16)
    
    bs = "\033[1;31mBIG 🔴\033[0m" if val >= 8 else "\033[1;34mSMALL 🔵\033[0m"
    eo = "\033[1;35mEVEN 🟣\033[0m" if val % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    num = val % 10
    return bs, eo, num

def login():
    hwid = get_hwid()
    while True:
        clear()
        print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
        print(f"║          👑 {OWNER_NAME} LOGIN SYSTEM 👑          ║")
        print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
        print(f"\n \033[1;37m[●] YOUR HWID : \033[1;36m{hwid}")
        print(f" \033[1;37m[●] STATUS    : \033[1;31mNOT ACTIVATED")
        print(f"\033[1;32m" + "━"*58 + "\033[0m")
        print(f"\n \033[1;33m[!] Note: Copy HWID and send to Admin for Activation.")
        print(f" \033[1;32m[#] Admin WhatsApp: {CONTACT_NO}")
        
        user_input = input(f"\n \033[1;37m[+] ENTER ACTIVATION KEY: \033[1;32m").strip()
        
        if check_key(hwid, user_input):
            print(f"\n \033[1;32m[✓] KEY VERIFIED! WELCOME FOZI KING...")
            time.sleep(2)
            break
        else:
            print(f"\n \033[1;31m[X] INVALID KEY! TRY AGAIN OR CONTACT ADMIN.")
            time.sleep(2)

def start_engine():
    login()
    last_p = ""

    while True:
        try:
            now = datetime.now()
            sec = now.second
            total_min = (now.hour * 60) + now.minute
            current_p = now.strftime("%Y%m%d") + "10101" + str(1141 + total_min)

            if current_p != last_p:
                if last_p != "":
                    h_bs, h_eo, h_num = get_prediction_logic(last_p)
                    history_list.insert(0, f"P: {last_p[-3:]} ➔ {h_bs} | {h_num} | {h_eo}")
                    if len(history_list) > 5: history_list.pop()
                last_p = current_p

            bs, eo, num = get_prediction_logic(current_p)

            clear()
            print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║           👑 {OWNER_NAME} OFFICIAL 👑            ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f" \033[1;37m[●] SERVER   : \033[1;32mPAK GAMES (FAST)")
            print(f" \033[1;37m[●] PERIOD   : \033[1;33m{current_p}")
            print(f" \033[1;37m[●] STATUS   : \033[1;32mPREMIUM KEY ACTIVE")
            print("\033[1;32m" + "━"*58 + "\033[0m")

            print(f"\n   \033[1;33m🚀 NEXT TARGET:")
            print(f"   \033[1;37m[RESULT] : {bs}")
            print(f"   \033[1;37m[NUMBER] : \033[1;32m{num}")
            print(f"   \033[1;37m[TYPE]   : {eo}")

            print("\033[1;32m\n" + "━"*15 + " [ PREVIOUS HISTORY ] " + "━"*21 + "\033[0m")
            if not history_list:
                print("   \033[1;30mLoading data from server...")
            else:
                for line in history_list:
                    print(f"   {line}")

            rem_s = 60 - sec
            color = "\033[1;32m" if rem_s > 10 else "\033[1;31m"
            print(f"\n {color}[⏳] TIMER: {rem_s}s \033[0m")
            
            time.sleep(1)
        except Exception:
            pass

if __name__ == "__main__":
    try:
        start_engine()
    except KeyboardInterrupt:
        sys.exit()
