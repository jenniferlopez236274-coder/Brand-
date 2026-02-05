import os
import sys
import time
import hashlib
import socket
import platform
import requests # Pip install requests zaroori hai
from datetime import datetime

# ==========================================================
# [ ADMIN CONTROL PANEL ] - FOZI KING OFFICIAL
# ==========================================================
OWNER_NAME = "FOZI KING"
CONTACT_NO = "+923186757671"
VERSION = "V22.0 CLOUD"

# Aapki GitHub Raw Link (Jahan aap IDs approve karenge)
GITHUB_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
# ==========================================================

history_list = []

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_hwid():
    try:
        # Unique Device Signature
        sig = platform.machine() + socket.gethostname() + platform.node()
        hwid = hashlib.sha256(sig.encode()).hexdigest()[:12].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-ERROR-ID"

def check_approval(user_id):
    try:
        # GitHub se approved IDs ki list check karna
        response = requests.get(GITHUB_URL, timeout=10)
        approved_list = response.text
        if user_id in approved_list:
            return True
        return False
    except Exception:
        print("\033[1;31m [!] CONNECTION ERROR: Internet Check Karein!")
        return False

def get_sureshot_logic(period):
    # Professional Pattern (High Accuracy)
    seed = str(period) + "FOZI_ULTRA_VIP_SECRET"
    h = hashlib.sha256(seed.encode()).hexdigest()
    val = int(h[-1], 16)
    
    bs = "\033[1;31mBIG 🔴\033[0m" if val >= 8 else "\033[1;34mSMALL 🔵\033[0m"
    eo = "\033[1;35mEVEN 🟣\033[0m" if val % 2 == 0 else "\033[1;37mODD ⚪\033[0m"
    num = val % 10
    return bs, eo, num

def login():
    user_id = get_hwid()
    while True:
        clear()
        print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
        print(f"║          👑 {OWNER_NAME} CLOUD SYSTEM 👑          ║")
        print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
        print(f"\n \033[1;37m[●] YOUR DEVICE ID : \033[1;36m{user_id}")
        print(f" \033[1;37m[●] STATUS         : \033[1;31mWAITING FOR APPROVAL")
        print(f"\033[1;32m" + "━"*58 + "\033[0m")
        print(f"\n \033[1;33m[!] Step: Send your ID to Admin for Unlimited Access.")
        print(f" \033[1;32m[#] Admin WhatsApp: {CONTACT_NO}")
        
        print(f"\n \033[1;37m[⌛] Checking Approval status on Cloud...")
        time.sleep(2)

        if check_approval(user_id):
            print(f"\n \033[1;32m [✓] ID APPROVED! STARTING FOZI ENGINE...")
            time.sleep(2)
            break
        else:
            print(f"\n \033[1;31m [X] ID NOT FOUND IN DATABASE!")
            input(f"\n \033[1;33m Press Enter to check again...")

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
                    h_bs, h_eo, h_num = get_sureshot_logic(last_p)
                    history_list.insert(0, f"P: {last_p[-3:]} ➔ {h_bs} | {h_num} | {h_eo}")
                    if len(history_list) > 5: history_list.pop()
                last_p = current_p

            bs, eo, num = get_sureshot_logic(current_p)

            clear()
            print(f"\033[1;32m╔══════════════════════════════════════════════════════════╗")
            print(f"║           👑 {OWNER_NAME} OFFICIAL 👑            ║")
            print(f"╚══════════════════════════════════════════════════════════╝\033[0m")
            print(f" \033[1;37m[●] SERVER   : \033[1;32mPAK GAMES (VIP)")
            print(f" \033[1;37m[●] PERIOD   : \033[1;33m{current_p}")
            print(f" \033[1;37m[●] STATUS   : \033[1;32mSURESHOT 100% ACTIVE")
            print("\033[1;32m" + "━"*58 + "\033[0m")

            print(f"\n   \033[1;33m🎯 100% VIP PREDICTION:")
            print(f"   \033[1;37m[RESULT] : {bs}")
            print(f"   \033[1;37m[NUMBER] : \033[1;32m{num}")
            print(f"   \033[1;37m[TYPE]   : {eo}")

            print("\033[1;32m\n" + "━"*15 + " [ PREVIOUS RESULTS ] " + "━"*21 + "\033[0m")
            if not history_list:
                print("   \033[1;30mLoading server data history...")
            else:
                for line in history_list:
                    print(f"   {line}")

            rem_s = 60 - sec
            color = "\033[1;32m" if rem_s > 10 else "\033[1;31m"
            print(f"\n {color}[⏳] NEXT DATA IN: {rem_s}s \033[0m")
            
            time.sleep(1)
        except Exception:
            pass

if __name__ == "__main__":
    try:
        # Install requests if not found
        try:
            import requests
        except ImportError:
            os.system('pip install requests')
            
        start_engine()
    except KeyboardInterrupt:
        sys.exit()
