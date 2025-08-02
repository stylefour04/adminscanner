import requests
import os
import concurrent.futures

# Warna untuk tampilan terminal
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

# ASCII Art
ascii_art = f"""{GREEN}

     _    ____  __  __ ___ _   _   ____   ____    _    _   _ 
    / \  |  _ \|  \/  |_ _| \ | | / ___| / ___|  / \  | \ | |
   / _ \ | | | | |\/| || ||  \| | \___ \| |     / _ \ |  \| |
  / ___ \| |_| | |  | || || |\  |  ___) | |___ / ___ \| |\  |
 /_/   \_\____/|_|  |_|___|_| \_| |____/ \____/_/   \_\_| \_|
                                                             

                         
{YELLOW}STYLE04 Admin Login Scanner{RESET}
"""

def check_url(url):
    """Memeriksa URL dan mengembalikan hasilnya."""
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return f"{GREEN}[+] : {url}{RESET}"
        else:
            return f"{RED}[-] : {url}{RESET}"
    except requests.exceptions.RequestException:
        return f"{RED}[-] : {url}{RESET}"

def scan_admin_login(domain):
    """Proses Scanning..."""

    directories = [
        "/admin/", "/administrator/", "/login/", "/wp-admin/", "/wp-login.php",
        "/backend/", "/panel/", "/cpanel/", "/webadmin/", "/siteadmin/",
        "/user/", "/useradmin/", "/bb-admin/", "/memberadmin/", "/adminarea/",
        "/admin1/", "/admin2/", "/uploads", "/admin3/", "/moderator/", "/moderatoradmin/",
        "/accounts/", "/account/", "/controlpanel/", "/cp/", "/phpadmin/",
        "/phpMyAdmin/", "/shell/", "/server/", "/config/", "/configuration/",
        "/database/", "/dbadmin/", "/sqladmin/", "/websql/", "/myadmin/",
        "/myadmin2/", "/pma/", "/xampp/", "/cfg/", "/tools/", "/scripts/",
        "/setup/", "/install/", "/update/", "/upgrade/", "/upload/", "/files/",
        "/filemanager/", "/file-manager/", "/file_manager/", "/cms/", "/data/",
        "/inc/", "/include/", "/includes/"
    ]

    print(f"{YELLOW}[STYLE04] Memindai {domain}...{RESET}")

    urls = [f"{domain}{directory}" for directory in directories]

    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        results = list(executor.map(check_url, urls))

    for result in results:
        print(result)

if __name__ == "__main__":
    os.system("clear")
    print(ascii_art)
    domain = input(f"{YELLOW}Masukkan domain (https://example.com): {RESET}")
    scan_admin_login(domain)
