import os
import sys
import time
import hashlib
import socket
import requests  # Ye library internet se ID check karegi
from datetime import datetime

# ==========================================================
# [ ADMIN CONTROL PANEL ]
# ==========================================================
OWNER_NAME = "FOZI KING HACKER"
CONTACT_NO = "+923186757671"

# Aapki GitHub Raw File ka sahi link
APPROVAL_URL = "https://raw.githubusercontent.com/jenniferlopez236274-coder/Aprowl.txt/main/Aprowl.txt"
# ==========================================================

def clear():
    os.system('clear' if os.name == 'posix' else 'cls')

def get_hwid():
    try:
        # Aapka original hardware ID logic
        raw_info = socket.gethostname() + os.getlogin()
        hwid = hashlib.md5(raw_info.encode()).hexdigest()[:10].upper()
        return f"FOZI-{hwid}"
    except:
        return "FOZI-ERR-786"

def check_security():
    clear()
    user_hwid = get_hwid()
    
    print("\033[1;32m [●] Connecting to Server...")
    
    try:
        # GitHub se list fetch karna
        response = requests.get(APPROVAL_URL, timeout=10)
        # Har line se ID uthayega aur extra space khatam karega
        approved_list = [line.strip() for line in response.text.splitlines()]
        
        if user_hwid in approved_list:
            print(f"\n\033[1;32m [✔] DEVICE {user_hwid} REGISTERED!")
            time.sleep(2)
            return True
        else:
            print(f"\n\033[1;91m [!] ACCESS DENIED: YOUR KEY IS NOT APPROVED")
            print(f"\033[1;97m [●] YOUR ID : \033[1;36m{user_hwid}")
            print(f"\n\033[1;33m [#] TO BUY ACCESS, SEND ID TO : \033[1;97m{CONTACT_NO}")
            sys.exit()
            
    except Exception as e:
        print("\033[1;31m [!] CONNECTION ERROR: Check your Internet!")
        print("\033[1;90m Hint: Make sure 'requests' library is installed (pip install requests)")
        sys.exit()

# --- Prediction Logic Start ---
def get_k3_logic():
    now = datetime.now()
    base = "10101"
    mins = (now.hour * 60) + now.minute
    p_suffix = 9701 + mins 
    period = now.strftime("%Y%m%d") + base + str(p_suffix)
    seed = period + "FOZI_ULTRA_SECRET_V29"
    h = hashlib.sha256(seed.encode()).hexdigest()
    val = (int(h[:2], 16) % 16) + 3
    res = "BIG 🔴" if val >= 11 else "SMALL 🔵"
    pattern = "ODD" if val % 2 != 0 else "EVEN"
    return period, val, res, pattern

def start_tool():
    last_p = ""
    while True:
        p, v, r, patt = get_k3_logic()
        if p != last_p:
            last_p = p
            clear()
            print(f"\033[1;32m 👑 {OWNER_NAME} 👑")
            print(f"\n\033[1;96m [PERIOD] : {p}")
            print(f" [PREDICTION] : \033[1;33m{r}\033[0m")
            print(f" [PATTERN] : {patt}")
            time.sleep(1)
        time.sleep(1)

if __name__ == "__main__":
    if check_security():
        start_tool()
