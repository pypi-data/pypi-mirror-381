from .C_M import CM; C = CM()
from.Random_INFO import R_I; RI = R_I()

C_Line = f"{C.r}{'_' * 61}"


# ---------------- Generate IMEI ----------------
def generate_imei():
    imei = ''.join(str(C.random.randint(0, 9)) for _ in range(14))
    check_digit = (sum(int(d) if i % 2 == 0 else sum(divmod(int(d) * 2, 10)) for i, d in enumerate(imei)) * 9) % 10
    return imei + str(check_digit)


isIMEI = generate_imei()


# ---------------- Generate lat lon hex ----------------
def generate_lat_lon_hex():
    scale_factor = 10**12
    lat, lon = round(C.random.uniform(-90.0, 90.0), 6), round(C.random.uniform(-180.0, 180.0), 6)
    lat_hex = hex(int(abs(lat) * scale_factor)) + "L"
    lon_hex = hex(int(abs(lon) * scale_factor)) + "L"
    return lat_hex, lon_hex


lat_hex, lon_hex = generate_lat_lon_hex()


# ---------------- Generate Mac Add ----------------
def generate_mac_add():
    return ':'.join([''.join(C.random.choices('0123456789ABCDEF', k=2)) for _ in range(6)])


isMac1, isMac2, isMac3, isMac4 = [generate_mac_add() for _ in range(4)]


# ---------------- Generate Device ID ----------------
def generateDeviceId():
    volatile_seed = "12345"
    seed = ''.join(C.random.choice(C.string.ascii_letters + C.string.digits) for _ in range(16))
    m = C.hashlib.md5()
    m.update(seed.encode('utf-8') + volatile_seed.encode('utf-8'))
    return m.hexdigest()[:16], seed


device_id, random_seed = generateDeviceId()


# ---------------- Regex Scan ----------------
def Regex_Scan(Smali_Path, Target_Regex, Count, Lock):

    Smali = open(Smali_Path, 'r', encoding='utf-8', errors='ignore').read()

    Regexs = [C.re.compile(r) for r in Target_Regex]

    for Regex in Regexs:
        if Regex.search(Smali):

            if Lock:
                try:
                    with Lock:
                        Count.value += 1
                        print(f"\r{C.lb}[ {C.c}Find Target Smali {C.lb}] {C.g}➸❥ {Count.value}", end='', flush=True)

                except Exception:
                    return None

            else:
                Count[0] += 1
                print(f"\r{C.lb}[ {C.c}Find Target Smali {C.lb}] {C.g}➸❥ {Count[0]}", end='', flush=True)

            return Smali_Path


# ---------------- Patch Random Info ----------------
def Patch_Random_Info(smali_folders, isID):

    RI.get_random_device_info()
    Smali_Paths, matching_files = [], []

    patterns = [
        # ---------------- Build Info ----------------
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->MANUFACTURER:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_manufacturer}"',
            f"MANUFACTURER ➸❥ {C.rkj}{RI.is_manufacturer}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->BRAND:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_brand}"',
            f"BRAND ➸❥ {C.rkj}{RI.is_brand}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->MODEL:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_model}"',
            f"MODEL ➸❥ {C.rkj}{RI.is_model}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->PRODUCT:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_product}"',
            f"PRODUCT ➸❥ {C.rkj}{RI.is_product}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->DEVICE:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_device}"',
            f"DEVICE ➸❥ {C.rkj}{RI.is_device}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->BOARD:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_board}"',
            f"BOARD ➸❥ {C.rkj}{RI.is_board}"
        ),
        (
            r'invoke-static \{\}, Landroid/os/Build;->getRadioVersion\(\)Ljava/lang/String;[^>]*?move-result-object ([pv]\d+)',
            rf'const-string \1, "Unknown"',
            f"getRadioVersion ➸❥ {C.rkj}Unknown"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->RADIO:Ljava/lang/String;',
            rf'const-string \1, "Unknown"',
            f"RADIO ➸❥ {C.rkj}Unknown"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->HARDWARE:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_hardware}"',
            f"HARDWARE ➸❥ {C.rkj}{RI.is_hardware}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->BOOTLOADER:Ljava/lang/String;',
            rf'const-string \1, "Unknown"',
            f"BOOTLOADER ➸❥ {C.rkj}Unknown"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->FINGERPRINT:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_fingerprint}"',
            f"FINGERPRINT ➸❥ {C.rkj}{RI.is_fingerprint}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->ID:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_id}"',
            f"ID ➸❥ {C.rkj}{RI.is_id}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->SERIAL:Ljava/lang/String;',
            rf'const-string \1, "Unknown"',
            f"SERIAL ➸❥ {C.rkj}Unknown"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->DISPLAY:Ljava/lang/String;',
            rf'const-string \1, "{RI.is_display}"',
            f"DISPLAY ➸❥ {C.rkj}{RI.is_display}"
        ),
        (
            r'sget-object ([pv]\d+), Landroid/os/Build;->HOST:Ljava/lang/String;',
            rf'const-string \1, "localhost"',
            f"HOST ➸❥ {C.rkj}localhost"
        ),
        (
            r'const-string [pv]\d+, "(?:generic|goldfish)"[^>]*?invoke-static \{[^\}]*\}, Landroid/os/Build;->get(?:Device|Hardware)\(\)Ljava/lang/String;[^>]*?move-result-object [pv]\d+[^>]*?invoke-virtual \{[^\}]*\}, Ljava/lang/String;->contains\(Ljava/lang/CharSequence;\)Z[^>]*?move-result ([pv]\d+)',
            rf'const/4 \1, 0x0',
            "Bypassed Device detection"
        ),

        # ---------------- Mock Location & Update & PKG Install Fixed ----------------
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/location/Location;->getLongitude\(\)D[^>]*?)move-result-wide ([pv]\d+)',
            rf'\1const-wide \2, {lon_hex}',
            f"Longitude ➸❥ {C.rkj}{lon_hex}"
        ),
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/location/Location;->getLatitude\(\)D[^>]*?)move-result-wide ([pv]\d+)',
            rf'\1const-wide \2, {lat_hex}',
            f"Latitude ➸❥ {C.rkj}{lat_hex}"
        ),
        (
            r'invoke-virtual \{[^\}]*\}, Landroid/location/Location;->(?:isFromMockProvider|isMock)\(\)Z[^>]*?move-result ([pv]\d+)',
            rf'const/4 \1, 0x0',
            "Bypassed Mock Detection"
        ),
        (
            r'iget-object ([pv]\d+), [pv]\d+, L[^;]*;->ip:Ljava/lang/String;',
            rf'const-string \1, "127.0.0.1"',
            f"IP To LocalHost ➸❥ {C.rkj}127.0.0.1"
        ),
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/content/pm/PackageManager;->getInstallerPackageName\(Ljava/lang/String;\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
            r'\1const-string \2, "com.android.vending"',
            "Fixed Installer"
        ),

        # ---------------- Settings$Secure ----------------
        (
            r'(const-string [pv]\d+, "bluetooth_address"[^>]*?invoke-static \{[^\}]*\}, Landroid/provider/Settings\$Secure;->getString\(Landroid/content/ContentResolver;Ljava/lang/String;\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
            rf'\1const-string \2, "{isMac1}"',
            f"Bluetooth Address ➸❥ {C.rkj}{isMac1}"
        ),

        # ---------------- Network Info ----------------
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/net/wifi/WifiInfo;->getBSSID\(\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
            rf'\1const-string \2, "{isMac2}"',
            f"WifiInfo BSSID ➸❥ {C.rkj}{isMac2}"
        ),
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/net/wifi/WifiInfo;->getMacAddress\(\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
            rf'\1const-string \2, "{isMac3}"',
            f"WifiInfo MacAddress ➸❥ {C.rkj}{isMac3}"
        ),
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/bluetooth/BluetoothDevice;->getAddress\(\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
            rf'\1const-string \2, "{isMac4}"',
            f"BluetoothDevice Address ➸❥ {C.rkj}{isMac4}"
        ),

        # ---------------- Telephony Manager ----------------
        (
            r'(invoke-virtual \{[^\}]*\}, Landroid/telephony/TelephonyManager;->getDeviceId\(\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
            rf'\1const-string \2, "{isIMEI}"',
            f"IMEI NO (Device ID) ➸❥ {C.rkj}{isIMEI}"
        ),

        # ---------------- Fix Play ----------------
        (
            r'(invoke-interface \{[^\}]*\}, Lcom/google/android/vending/licensing/Policy;->allowAccess\(\)Z[^>]*?\s+)move-result ([pv]\d+)',
            r'\1const/4 \2, 0x1',
            "Bypass Client-Side LVL (allowAccess)"
        ),
        (
            r'(\.method [^(]*connectToLicensingService\(\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
            r'\1\2',
            "connectToLicensingService"
        ),
        (
            r'(\.method [^(]*initializeLicenseCheck\(\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
            r'\1\2',
            "initializeLicenseCheck"
        ),
        (
            r'(\.method [^(]*processResponse\(ILandroid/os/Bundle;\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
            r'\1\2',
            "processResponse"
        )
    ]

    if isID:
        # ---------------- Custom Device ID ----------------
        patterns.append(
            (
                r'(const-string [pv]\d+, "android_id"[^>]*?invoke-static \{[^\}]*\}, Landroid/provider/Settings\$Secure;->getString\(Landroid/content/ContentResolver;Ljava/lang/String;\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
                rf'\1const-string \2, "{isID}"',
                f"Custom Android ID ➸❥ {C.rkj}{isID}"
            )
        )
    else:
        patterns.append(
            (
                r'(const-string [pv]\d+, "android_id"[^>]*?invoke-static \{[^\}]*\}, Landroid/provider/Settings\$Secure;->getString\(Landroid/content/ContentResolver;Ljava/lang/String;\)Ljava/lang/String;[^>]*?)move-result-object ([pv]\d+)',
                rf'\1const-string \2, "{device_id}"',
                f"Random Android ID ➸❥ {C.rkj}{device_id}"
            )
        )

    Target_Regex = [p[0] for p in patterns]

    for smali_folder in smali_folders:
        for root, _, files in C.os.walk(smali_folder):
            for file in files:
                if file.endswith('.smali'):
                    Smali_Paths.append(C.os.path.join(root, file))

    try:
        # ---------------- Multiple Threading ----------------
        with C.Manager() as M:
            Count = M.Value('i', 0); Lock = M.Lock()
            with C.Pool(C.cpu_count()) as PL:
                matching_files = [path for path in PL.starmap(Regex_Scan, [(Smali_Path, Target_Regex, Count, Lock) for Smali_Path in Smali_Paths]) if path]

    except Exception:
        # ---------------- Single Threading ----------------
        Count = [0]
        for Smali_Path in Smali_Paths:
            result = Regex_Scan(Smali_Path, Target_Regex, Count, None)

            if result:
                matching_files.append(result)

    print(f" {C.g}✔", flush=True)
    print(f'\n{C_Line}\n')

    if matching_files:
        for pattern, replacement, description in patterns:
            count_applied, applied_files = 0, set()

            for file_path in matching_files:
                content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
                new_content = C.re.sub(pattern, replacement, content)

                if new_content != content:
                    if file_path not in applied_files:
                        applied_files.add(file_path)

                    count_applied += 1

                    open(file_path, 'w', encoding='utf-8', errors='ignore').write(new_content)

            if count_applied > 0:
                print(f"\n{C.lb}[ {C.c}Tag {C.lb}] {C.g}{description}")
                print(f"\n{C.lb}[ {C.c}Pattern {C.lb}] {C.g}➸❥ {C.pr}{pattern}")

                for file_path in applied_files:
                    print(f"{C.g}  |\n  └──── {C.r}~{C.g}$ {C.y}{C.os.path.basename(file_path)} {C.g}✔")

                print(f"\n{C.lb}[ {C.c}Pattern Applied {C.lb}] {C.g}➸❥ {C.pr}{count_applied} {C.c}Time/Smali {C.g}✔\n\n{C_Line}\n")