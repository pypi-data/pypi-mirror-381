from .C_M import CM; C = CM()


# ---------------- Format Time ----------------
def Format_Time(timestamp):
    return C.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M:%S")


# ---------------- CRC Fix ----------------
def CRC_Fix(apk_path, build_dir, file_types):

    Logs = []

    origin_entries, mod_entries = [
       {
           entry.filename: (entry.CRC, entry.date_time)
           for entry in C.zipfile.ZipFile(file_path, 'r').infolist()
           if any(file_type in entry.filename for file_type in file_types)
       } for file_path in (apk_path, build_dir)
    ]

    binary_content = open(build_dir, 'rb').read()

    for filename, (origin_crc, origin_time) in origin_entries.items():
        if filename in mod_entries and origin_crc != mod_entries[filename][0]:
            origin_crc_bytes = origin_crc.to_bytes(4, 'little')
            mod_crc_bytes = mod_entries[filename][0].to_bytes(4, 'little')
            binary_content = binary_content.replace(mod_crc_bytes, origin_crc_bytes)

            Logs.append((filename, f"{origin_crc:08x}", f"{mod_entries[filename][0]:08x}", Format_Time(C.datetime(*origin_time).timestamp()), Format_Time(C.datetime(*mod_entries[filename][1]).timestamp())))

    open(build_dir, 'wb').write(binary_content)
    
    print(f"\n{'':20}✨ {C.g}CRCFix by {C.rkj}Kirlif{C.g}' ✨\n")
    print(f"{C.c}{'File Name':<22}{'CRC':<12}{'FIX':<12}{'Modified'}")

    for e in Logs:
        print(f"\n{C.g}{e[0]:<22}{e[1]}{'':<4}{e[2]}{'':<4}{e[4]}\n")
    print(f"{C.r}{'_' * 61}\n\n")
    
    return build_dir