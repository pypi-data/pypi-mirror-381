from .C_M import CM; C = CM()
from .Files_Check import FileCheck;

F = FileCheck(); F.Set_Path(); F.isEmulator()
C_Line = f"{C.r}{'_' * 61}"


# ---------------- Decompile APK ----------------
def Decompile_Apk(apk_path, decompile_dir, isEmulator, isAPKEditor, isAES):

    A_P = F.APKTool_Path_E if isEmulator else F.APKTool_Path
    AA = f"{'APKEditor' if isAPKEditor else 'APKTool'}"

    print(f"\n{C_Line}\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile APK with {AA}...")

    if isAPKEditor:
        cmd = ["java", "-jar", F.APKEditor_Path, "d", "-i", apk_path, "-o", decompile_dir, "-f", "-no-dex-debug", "-dex-lib", "jf"]

        print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} d -i {apk_path} -o {C.os.path.basename(decompile_dir)} -f -no-dex-debug -dex-lib jf\n\n{C_Line}{C.g}\n")

    else:
        cmd = ["java", "-jar", A_P, "d", "-f", "--only-main-classes"] + (["-b"] if isAES else []) + [apk_path, "-o", decompile_dir, "-p", decompile_dir]

        print(f"{C.g}  |\n  └──── {C.r}Decompiling ~{C.g}$ java -jar {C.os.path.basename(A_P)} d -f {apk_path} -o {C.os.path.basename(decompile_dir)}\n\n{C_Line}{C.g}\n")

    try:
        C.subprocess.run(cmd, check=True)
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Decompile Successful  {C.g}✔\n\n{C_Line}\n\n")

    except C.subprocess.CalledProcessError:
        C.shutil.rmtree(decompile_dir)
        print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Decompile APK Failed with {AA} ✘\n")

        if not isAPKEditor:
            print(f"{C_Line}\n\n\n{C.lb}[ {C.y}Suggest ! {C.lb}]{C.c} Try With APKEditor, Flag {C.g}-a\n     |\n     └──── {C.r}~ Ex. {C.g}$ {C.rkj}ApkPatcher -i {C.y}{apk_path} {C.g}-a\n")
        exit()


# ---------------- Recompile APK ----------------
def Recompile_Apk(decompile_dir, apk_path, build_dir, isEmulator, isAPKEditor):

    A_P = F.APKTool_Path_E if isEmulator else F.APKTool_Path
    AA = f"{'APKEditor' if isAPKEditor else 'APKTool'}"

    print(f"{C_Line}\n\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile APK with {AA}...")

    if isAPKEditor:
        cmd = ["java", "-jar", F.APKEditor_Path, "b", "-i", decompile_dir, "-o", build_dir, "-f", "-dex-lib", "jf"]

        print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(F.APKEditor_Path)} b -i {C.os.path.basename(decompile_dir)} -o {C.os.path.basename(build_dir)} -f -dex-lib jf\n\n{C_Line}{C.g}\n")

    else:
        cmd = ["java", "-jar", A_P, "b", "-f", decompile_dir, "-o", build_dir, "-p", decompile_dir]

        print(f"{C.g}  |\n  └──── {C.r}Recompiling ~{C.g}$ java -jar {C.os.path.basename(A_P)} b -f {C.os.path.basename(decompile_dir)} -o {C.os.path.basename(build_dir)}\n\n{C_Line}{C.g}\n")

    try:
        C.subprocess.run(cmd, check=True)
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Recompile Successful  {C.g}✔\n\n{C_Line}\n")

    except C.subprocess.CalledProcessError:
        C.shutil.rmtree(decompile_dir)
        print(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Recompile APK Failed with {AA}... ✘\n")

        if not isAPKEditor:
            print(f"{C_Line}\n\n\n{C.lb}[ {C.y}Suggest ! {C.lb}]{C.c} Try With APKEditor, Flag {C.rkj}-a\n     |\n     └──── {C.r}~ Ex. {C.g}$ {C.rkj}ApkPatcher -i {C.y}{apk_path} {C.rkj}-a\n")
        exit()

    if C.os.path.exists(build_dir):
        print(f"\n{C.lb}[ {C.c}APK Created {C.lb}] {C.g}➸❥ {C.y}{build_dir} {C.g}✔\n\n{C_Line}\n")

    C.shutil.rmtree(decompile_dir)


# ---------------- FixSigBlock ----------------
def FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir):

    C.os.rename(build_dir, rebuild_dir)
    sig_dir = decompile_dir.replace('_decompiled', '_SigBlock')

    for operation in ["d", "b"]:
        cmd = ["java", "-jar", F.APKEditor_Path, operation, "-t", "sig", "-i", (apk_path if operation == "d" else rebuild_dir), "-f", "-sig", sig_dir]

        if operation == "b":
            cmd.extend(["-o", build_dir])

        C.subprocess.run(cmd, check=True, text=True, capture_output=True)
    C.shutil.rmtree(sig_dir); C.os.remove(rebuild_dir)


# ---------------- Sign APK ----------------
def Sign_Apk(build_dir):

    cmd = ["java", "-jar", F.Sign_Jar, "--overwrite", "-a", build_dir]

    print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Signing APK...")
    print(f"{C.g}  |\n  └──── {C.r}Signing ~{C.g}$ java -jar {C.os.path.basename(F.Sign_Jar)} --overwrite -a {build_dir}\n\n{C_Line}{C.g}\n")

    try:
        C.subprocess.run(cmd, check=True)
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Sign Successful  {C.g}✔\n")

        idsig_file = build_dir + ".idsig"

        if C.os.path.exists(idsig_file):
            C.os.remove(idsig_file)

        print(f'{C_Line}\n\n')

    except C.subprocess.CalledProcessError:
        exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} Sign Failed ! ✘\n")