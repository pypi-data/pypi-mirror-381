from.Package import P
from.C_M import CM; C = CM()


# ---------------- Fix Manifest ----------------
def Fix_Manifest(manifest_path, smali_folders, isPKG):

    isPC = bool(C.re.search('piracychecker', open(manifest_path).read(), C.re.I))

    patterns = [
        (
            r'\s+android:(splitTypes|requiredSplitTypes)="[^"]*?"',
            r'',
            'Splits'
        ),
        (
            r'(isSplitRequired=)"true"',
            r'\1"false"',
            'isSplitRequired'
        ),
        (
            r'\s+<meta-data[^>]*"com.android.(vending.|stamp.|dynamic.apk.)[^"]*"[^>]*/>',
            r'',
            '<meta-data>'
        ),
        (
            r'\s+<[^>]*"(com.pairip.licensecheck)[^"]*"[^>]*/>' if isPC else r'\s+<[^>]*"com.(pairip.licensecheck|android.vending.CHECK_LICENSE)[^"]*"[^>]*/>',
            r'',
            'CHECK_LICENSE'
        )
    ]

    if isPKG:
        patterns.extend(
            [
                (
                    rf'{P.Menifest_Regex}',
                    r'',
                    'Spoof Package Detection'
                )
            ]
        )

    for pattern, replacement, description in patterns:
        content = open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()
        new_content = C.re.sub(pattern, replacement, content)

        if new_content != content:
            print(f"\n{C.lb}[ {C.c}Tag {C.lb}] {C.rkj}{description}\n\n{C.lb}[ {C.c}Applying Pattern {C.lb}] {C.g}➸❥ {C.pr}{pattern}\n{C.g}  |\n  └──── {C.r}~{C.g}$ {C.c} Patch Cleaned Up {C.pr}'{C.g}{C.os.path.basename(manifest_path)}{C.pr}' {C.g}✔\n")

        open(manifest_path, 'w', encoding='utf-8', errors='ignore').write(new_content)


# ---------------- Patch Manifest ----------------
def Patch_Manifest(decompile_dir, manifest_path):

    content = open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()

    application_tag = C.re.search(r'<application\s+[^>]*>', content)[0]

    cleaned_tag = C.re.sub(r'\s+android:(usesCleartextTraffic|networkSecurityConfig)="[^"]*?"', '', application_tag)

    content = content.replace(application_tag, C.re.sub(r'>','\n\tandroid:usesCleartextTraffic="true"\n\tandroid:networkSecurityConfig="@xml/network_security_config">', cleaned_tag))

    open(manifest_path, 'w', encoding='utf-8', errors='ignore').write(content)

    print(f'\n{C.lb}[ {C.pr}Updated {C.lb}] {C.c} android:networkSecurityConfig={C.pr}"{C.g}@xml/network_security_config{C.pr}" {C.g}➸❥ {C.y}{C.os.path.basename(manifest_path)} {C.g}✔\n')

    print(f'\n{C.lb}[ {C.pr}Updated {C.lb}] {C.c} android:usesCleartextTraffic={C.pr}"{C.g}true{C.pr}" {C.g}➸❥ {C.y}{C.os.path.basename(manifest_path)} {C.g}✔\n')


# ---------------- Permission Manifest ----------------
def Permission_Manifest(decompile_dir, manifest_path, isAPKEditor):

    A_Y_P = C.os.path.join(decompile_dir, 'apktool.yml')

    content = open(manifest_path, 'r', encoding='utf-8', errors='ignore').read()

    new_permissions = '''\t<uses-permission android:name="android.permission.READ_EXTERNAL_STORAGE"/>\n\t<uses-permission android:name="android.permission.WRITE_EXTERNAL_STORAGE"/>\n\t<uses-permission android:name="android.permission.MANAGE_EXTERNAL_STORAGE"/>'''

    content = C.re.sub(r'\s+<uses-permission[^>]*android:name="(android.permission.((READ|WRITE|MANAGE)_EXTERNAL_STORAGE))"[^>]*>', '', content)
        
    content = C.re.sub(r'android:targetSdkVersion="\d+"', 'android:targetSdkVersion="28"', content)

    content = C.re.sub(r'(<manifest\s+[^>]*>)', r'\1\n' + new_permissions, content)

    application_tag = C.re.search(r'<application\s+[^>]*>', content)[0]

    cleaned_tag = C.re.sub(r'\s+android:(request|preserve)LegacyExternalStorage="[^"]*?"', '', application_tag)

    content = content.replace(application_tag, C.re.sub(r'>','\n\tandroid:requestLegacyExternalStorage="true"\n\tandroid:preserveLegacyExternalStorage="true">', cleaned_tag))
        
    open(manifest_path, 'w', encoding='utf-8', errors='ignore').write(content)
        
    print(f"\n{C.lb}[ {C.c}Storage Permission {C.lb}] {C.g}➸❥ {C.pr}'{C.g}AndroidManifest.xml{C.pr}' {C.g}✔\n")

    if not isAPKEditor:
        yml = open(A_Y_P, 'r', encoding='utf-8', errors='ignore').read()
        update_yml = C.re.sub(r'(targetSdkVersion:) (\d+)', r'\1 28', yml)
        open(A_Y_P, 'w', encoding='utf-8', errors='ignore').write(update_yml)

        print(f"\n{C.lb}[ {C.pr}targetSdkVersion {C.lb}] {C.c}28 {C.g}➸❥ apktool.yml\n")