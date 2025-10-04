from.C_M import CM; C = CM()
from collections import defaultdict
from .Files_Check import FileCheck

F = FileCheck(); F.Set_Path()
C_Line = f"{C.r}{'_' * 61}"


# ---------------- Regex Scan ----------------
def R_S_F(smali_folders):
    for smali_folder in smali_folders:
        for root, _, files in C.os.walk(smali_folder):
            for file in files:
                file_path = C.os.path.join(root, file)
                yield file_path, open(file_path, 'r', encoding='utf-8', errors='ignore').read()


# ---------------- AES Logs Inject ----------------
def AES_Logs_Inject(decompile_dir, smali_folders):
    reg = C.re.compile(r'"AES/[^/]+/[^"]+"')
    Class_P = C.re.compile(r'\.class[^;]* (L[^;]+;)')
    Met_P = C.re.compile(r'\.method.*?\s([a-zA-Z0-9_<>\$]+)\((.*?)\)(.*)')
    Match_F, matched_files, total_files = defaultdict(list), [], 0

    for file_path, content in R_S_F(smali_folders):
        if "Ljavax/crypto/Cipher;->doFinal([B)[B" in content and "Ljavax/crypto/spec/SecretKeySpec;" in content and "Ljavax/crypto/spec/IvParameterSpec;" in content:

            Class_N = Class_P.search(content)[1]

            for block in content.split('.method')[1:]:

                if reg.search(block):
                    Met_M = Met_P.search(".method" + block.split('\n', 1)[0])

                    if Met_M:
                        total_files += 1
                        Met_Sig = f"{Met_M[1]}({Met_M[2]}){Met_M[3]}"
                        match = f"{Class_N}->{Met_Sig}"
                        Match_F[match].append(file_path)

                    print(f"\r{C.lb}[ {C.pr}Total Method Signature {C.lb}] {C.c} Found {C.g}➸❥ {C.pr}{total_files}", end='', flush=True)

    if total_files == 0:
        C.shutil.rmtree(decompile_dir)
        exit(f"{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} No Matching Patterns found ! ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}] {C.rd} Sorry Bro Your Bad Luck !, Not Working MT Logs Method in This Apk, Try Another Method.\n")

    print(f"  {C.g}✔\n\n", flush=True)

    for file_path, content in R_S_F(smali_folders):
        if any(match in content for match in Match_F):
            total_files += 1
            matched_files.append(file_path)
        print(f"\r{C.lb}[ {C.pr}* {C.lb}] {C.c} Find Target Smali {C.g}➸❥ {total_files}", end='', flush=True)
    print(f"  ✔", flush=True)
    print(f'\n{C_Line}\n')

    Inject_A = r"invoke-static (\{[pv]\d+\}), Ljavax/crypto/Cipher;->getInstance\(Ljava/lang/String;\)Ljavax/crypto/Cipher;[^>]*?move-result-object ([pv]\d+)"

    Inject_A_matches = defaultdict(list)

    for match, file_paths in Match_F.items():
        for file_path in file_paths:
            content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
            matches = list(C.re.finditer(Inject_A, content))

            if matches:
                Inject_A_matches[Inject_A].append(C.os.path.basename(file_path))

                updated_content = content

                for m in matches:
                    invoke_pv, result_pv = m[1], m[2]

                    if f"invoke-static {invoke_pv}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V" not in updated_content:
                        injected_lines = [
                            f"invoke-static {invoke_pv}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V",
                            f"invoke-static {invoke_pv}, Ljavax/crypto/Cipher;->getInstance(Ljava/lang/String;)Ljavax/crypto/Cipher;",
                            f"move-result-object {result_pv}",
                            f"invoke-static {{{result_pv}}}, LRK_TECHNO_INDIA/AES;->getInstance(Ljava/lang/Object;)V",
                        ]
                        match_text = m[0]
                        replacement_text = "\n    ".join(injected_lines)

                        if match_text in updated_content:
                            updated_content = updated_content.replace(match_text, replacement_text)

                open(file_path, 'w', encoding='utf-8', errors='ignore').write(updated_content)

    for pattern, file_paths in Inject_A_matches.items():
        print(f"\n{C.lb}[ {C.pr}Cipher {C.lb}] {C.c}Method Signature {C.g}➸❥ {C.rkj}{pattern}\n")
        for file_name in file_paths:
            print(f"{C.g}  |\n  └──── {C.r}~{C.g}$ {C.y}{file_name} {C.g}✔")
        print(f"\n{C.lb}[ {C.c}Pattern Applied {C.lb}] {C.g}➸❥ {C.pr}{len(file_paths)} {C.c}Time/Smali {C.g}✔\n\n{C_Line}\n")

    print(f'{C_Line}\n')

    for match in Match_F:
        regex = C.re.escape(match)
        matching_files, T_P = [], 0
            
        Inject_R = rf"invoke-static \{{(.*?)\}}, {regex}[^>]*?move-result-object ([pv]\d+)"

        for file_path in matched_files:
            content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()

            matches = list(C.re.finditer(Inject_R, content))

            if matches:
                T_P += 1
                matching_files.append(C.os.path.basename(file_path))

        if T_P > 0:
            print(f"\n{C.lb}[ {C.c}Method Signature {C.lb}] {C.g}➸❥ {C.rkj}{match}\n")
            for file_name in matching_files:
                print(f"{C.g}  |\n  └──── {C.r}~{C.g}$ {C.y}{C.os.path.basename(file_name)} {C.g}✔")
            print(f"\n{C.lb}[ {C.c}Pattern Applied {C.lb}] {C.g}➸❥ {C.pr}{len(matching_files)} {C.c}Time/Smali {C.g}✔\n\n{C_Line}\n")

            for file_path in matched_files:
                content = open(file_path, 'r', encoding='utf-8', errors='ignore').read()
                matches = list(C.re.finditer(Inject_R, content))

                if matches:
                    updated_content = content
                    for m in matches:
                        invoke_args, result_register = m[1], m[2]

                        invoke_args_list = invoke_args.split(", ")
                        param_count = len(invoke_args_list)

                        injected_lines = []
                        if param_count == 1:
                            injected_lines.append(f"invoke-static {{{invoke_args_list[0]}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V")
                            injected_lines.append(f"invoke-static {{{invoke_args}}}, {match}\n    move-result-object {result_register}")
                            injected_lines.append(f"invoke-static {{{result_register}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V")
                        elif param_count > 1:
                            for idx, param in enumerate(invoke_args_list, start=1):
                                injected_lines.append(f"invoke-static {{{param}}}, LRK_TECHNO_INDIA/AES;->b{idx}(Ljava/lang/Object;)V")
                            injected_lines.append(f"invoke-static {{}}, LRK_TECHNO_INDIA/AES;->b()V")
                            injected_lines.append(f"invoke-static {{{invoke_args}}}, {match}\n    move-result-object {result_register}")
                            injected_lines.append(f"invoke-static {{{result_register}}}, LRK_TECHNO_INDIA/AES;->a(Ljava/lang/Object;)V")

                        match_text = m[0]
                        replacement_text = "\n    ".join(injected_lines)

                        if match_text in updated_content:
                            updated_content = updated_content.replace(match_text, replacement_text)

                    open(file_path, 'w', encoding='utf-8', errors='ignore').write(updated_content)


# ---------------- Copy AES Smali ----------------
def Copy_AES_Smali(decompile_dir, smali_folders, manifest_path, isAES_MS, isAPKEditor):

    AES_Logs_Inject(decompile_dir, smali_folders)

    if isAES_MS:
        if isAPKEditor:
            decompile_dir = C.os.path.join(decompile_dir, "smali")

        prefix = "classes" if isAPKEditor else "smali_classes"

        L_S_C_F = C.os.path.join(decompile_dir, f"{prefix}{int(C.os.path.basename(smali_folders[-1])[len(prefix):]) + 1}")

        C.os.makedirs(L_S_C_F, exist_ok=True)
    else:
        L_S_C_F = smali_folders[-1]


    # ---------------- Copy AES.smali ----------------
    Target_Dest = C.os.path.join(L_S_C_F, 'RK_TECHNO_INDIA', 'AES.smali')
    C.os.makedirs(C.os.path.dirname(Target_Dest), exist_ok=True)
    C.shutil.copy(F.AES_Smali, Target_Dest)

    print(f"\n{C.lb}[ {C.c}Generate {C.lb}] {C.g}AES.smali {C.rkj}➸❥ {C.y}{C.os.path.relpath(Target_Dest, decompile_dir)}{C.g} ✔")


    # ---------------- Update Package Name ----------------
    PKG_Name = C.re.search(r'package="([^"]+)"', open(manifest_path, 'r', encoding='utf-8', errors='ignore').read())[1]
    content = open(Target_Dest, 'r', encoding='utf-8', errors='ignore').read()
    Update_PKG = content.replace('PACKAGENAME', PKG_Name)
    open(Target_Dest, 'w', encoding='utf-8', errors='ignore').write(Update_PKG)

    print(f"{C.g}     |\n     └── {C.r}Update Package Name ~{C.g}$ {C.rkj}➸❥ {C.pn}'{C.g}{PKG_Name}{C.pn}' {C.g}✔\n")