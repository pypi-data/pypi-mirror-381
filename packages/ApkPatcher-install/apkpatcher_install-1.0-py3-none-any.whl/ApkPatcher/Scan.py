from .C_M import CM; C = CM();
from .Files_Check import FileCheck

F = FileCheck(); F.Set_Path();

Tag = f"\n{C.r}————|———————|————{C.g}•❀ {C.rkj}Tag {C.g}❀•{C.r}————|———————|————\n"
EX = f"{C.pr}\n   |\n   ╰{C.r}┈{C.rkj}➢ {C.g}ApkPatcher -i Your_Apk_Path.apk {C.rkj}"
Info = f"{C.lb}[ {C.y}INFO {C.lb}] {C.c}"


# ---------------- Scan APK ----------------
def Scan_Apk(apk_path, isFlutter, Flutter_lib, isPairip, Pairip_lib):

    print(f"\n{C.r}{'_' * 61}\n")

    Package_Name = ''

    if C.os.name == 'posix':
        # ---------------- Extract Package Name with AAPT ----------------
        Package_Name = C.subprocess.run(['aapt', 'dump', 'badging', apk_path], capture_output=True, text=True).stdout.split("package: name='")[1].split("'")[0]

        if Package_Name:
            print(f"\n{C.lb}[ {C.c}Package Name {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{Package_Name}{C.pr}'{C.g} ✔")


    # ---------------- Extract Package Name with APKEditor ----------------
    if not Package_Name:
        Package_Name = C.subprocess.run(["java", "-jar", F.APKEditor_Path, "info", "-package", "-i", apk_path], capture_output=True, text=True).stdout.split('"')[1]

        print(f"\n{C.lb}[ {C.c}Package Name {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{Package_Name}{C.pr}'{C.g} ✔")


    # ---------------- Check Flutter Protection ----------------
    if Flutter_lib:
        if Flutter_lib:
            def check_java_installed():
                try:
                    C.subprocess.run(['radare2', '-v'], capture_output=True, text=True)
                except (C.subprocess.CalledProcessError, FileNotFoundError):
                    if C.os.name == 'posix':
                        for pkg in ['radare2']:
                            try:

                                result = C.subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True)

                                if pkg not in result.stdout:
                                    print(f"\n{C.lb}[ {C.pr}Installing {C.lb}] {C.c}{pkg}...{C.g}\n")
                                    C.subprocess.check_call(['pkg', 'install', '-y', pkg])

                                    print(f"\n{C.lb}[ {C.pr}Installed {C.lb}] {C.c}{pkg} Successfully.{C.g} ✔\n")

                                    C.os.system('cls' if C.os.name == 'nt' else 'clear')

                            except (C.subprocess.CalledProcessError, Exception) as e:
                                exit(f"\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No Internet Connection. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Installation {C.rd}'{C.g}pkg install {pkg}{C.rd}' ✘\n")
                    else:
                        exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Radare2 is not installed on Your System. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Install Radare2 and Run Script Again in New CMD. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Verify Radare2 installation using {C.rd}"{C.g}radare2 -v{C.rd}" command in CMD')

            check_java_installed()

        FP = f"\n\n{C.lb}[ {C.c}Flutter Protection {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{', '.join(C.os.path.basename(lib) for lib in Flutter_lib)}{C.pr}'{C.g} ✔"

        if not isFlutter:
            exit(f"{FP}\n\n\n{C.lb}[ {C.y}WARN ! {C.lb}] {C.rd}This is Flutter APK, So For SSL Bypass , Use {C.g} -f  {C.rd}Flag:\n\n\n{Info}If APK is Flutter, Then Use Additional Flag: {C.rkj}-f{EX}-f {C.y}-c certificate.cert\n")

        else:
            if isFlutter:
                print(FP)


    # ---------------- Check Pairip Protection ----------------
    if Pairip_lib:
        PP = f"\n\n{C.lb}[ {C.c}Pairip Protection {C.lb}] {C.rkj}➸❥ {C.pr}'{C.g}{', '.join(C.os.path.basename(lib) for lib in Pairip_lib)}{C.pr}'{C.g} ✔"

        if not isPairip:
            exit(f"{PP}\n\n\n{C.lb}[ {C.y}WARN ! {C.lb}] {C.rd}This is Pairip APK, So For SSL Bypass, Use {C.g} -p {C.c} / {C.g} -p -x  {C.c}( <isCoreX> ) {C.rd}Flag:\n\n\n{Info}If APK is Pairip, Then Use Additional Flag: {C.rkj}-p {C.pr}( Without Sign APK Use Only in VM / Multi_App ){EX}-p {C.y}-c certificate.cert\n\n\n{Info}If APK is Pairip, Then Hook CoreX & Use Additional Flag: {C.rkj}-p -x {C.pr}( Install Directly Only For [ arm64 ] ){EX}-p -x {C.y}-c certificate.cert\n\n\n{Info}Note Both Method Not Stable, May be APK Crash {C.pr}( So Try Your Luck ) 😂\n")

        else:
            if isPairip:
                print(PP)

    return Package_Name