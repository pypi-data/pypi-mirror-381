from .CRC import CRC_Fix
from .Scan import Scan_Apk
from .C_M import CM; C = CM()
from .Anti_Splits import Anti_Split
from .AES import Copy_AES_Smali
from .Smali_Patch import Smali_Patch
from .Argparse import parse_arguments
from .Ads_Patch import Ads_Smali_Patch
from .Instruction_Credit import instruction
from .Spoof_Patch import Patch_Random_Info
from .Cert_Net_Config import Write_Net_Config
from .Files_Check import FileCheck, __version__
from .Flutter_SSL_Patch import Patch_Flutter_SSL
from .Pairip_CoreX import Check_CoreX, Hook_Core
from .Manifest_Patch import Fix_Manifest, Patch_Manifest, Permission_Manifest
from .Decompile_Compile import Decompile_Apk, Recompile_Apk, FixSigBlock, Sign_Apk


def Clear():
    C.os.system('cls' if C.os.name == 'nt' else 'clear')
Clear()


# ---------------- Install Require Module ---------------
required_modules = ['requests', 'r2pipe', 'asn1crypto', 'multiprocess']
for module in required_modules:
    try:
        __import__(module)
    except ImportError:
        print(f"{C.lb}[ {C.pr}Installing {C.lb}] {C.c}{module} module...{C.g}\n")
        try:
            C.subprocess.check_call([C.sys.executable, "-m", "pip", "install", module])
            print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} {module} Installed Successfully.{C.g} ✔\n")
            Clear()
        except (C.subprocess.CalledProcessError, Exception):
            exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No Internet Connection. ✘\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Internet Connection is Required to Install {C.rd}'{C.g}pip install {module}{C.rd}' ✘\n")


# ---------------- Check Dependencies ---------------
def check_dependencies():
    try:
        C.subprocess.run(['java', '-version'], stdout=C.subprocess.PIPE, stderr=C.subprocess.PIPE, check=True, text=True)
    except (C.subprocess.CalledProcessError, FileNotFoundError):
        if C.os.name == 'posix':
            install_package('openjdk-17')
        else:
            exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Java is not installed on Your System. ✘\n\n{C.lb}[ {C.y}Ex ! {C.lb}] {C.rd} Install Java & Run Script Again in New CMD. ✘\n\n{C.lb}[ {C.y}Ex ! {C.lb}] {C.rd} Verify Java installation using {C.rd}"{C.g}java --version{C.rd}" command in CMD')

    if C.os.name == 'posix': install_package('aapt')


# ---------------- Install Package ---------------
def install_package(pkg):
    try:
        result = C.subprocess.run(['pkg', 'list-installed'], stdout=C.subprocess.PIPE, stderr=C.subprocess.PIPE, text=True)
        if pkg not in result.stdout:
            print(f"{C.lb}[ {C.pr}Installing {C.lb}] {C.c}{pkg}...{C.g}\n")
            C.subprocess.check_call(['pkg', 'install', '-y', pkg])
            print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} {pkg} Installed Successfully.{C.g} ✔\n")
            Clear()
    except (C.subprocess.CalledProcessError, Exception) as e:
        exit(f"\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No Internet Connection. ✘\n\n{C.lb}[ {C.rd}INFO {C.lb}]{C.rd} Internet Connection is Required to Installation {C.rd}'{C.g}pkg install {pkg}{C.rd}' ✘\n")

check_dependencies()

F = FileCheck(); F.Set_Path(); F.F_D()

Date = C.datetime.now().strftime('%d/%m/%y')
print(f"{C.rkj}{f'v{__version__}':>22}")

# Logo ( 🙏 )
b64 = """eJzVlc9LAkEUx8/Ov9DlMXgNzLAfeMlUSAQLETx4ELGlJEehnEPgQSrqUlFYdIroHNShixDRP1DQn1DaqUv+Cc3MzszOrFtUt96u+2O+n/fmvTe7LoCwsdIEGStNzsRj8WgkSoYXe9fsdwtFp15tEsfSp8n8phyYjZKCU11tNCHTWK5V2GhE+yIUCgF1DYFplIY9s0RLGdG56EsU5PTjRgLcyfIJMk1IQNcDiaUsLCUKyYV0XoUL4H8QErNLbJxNBCtA4FSOikGdOufBj/DYAQS1L72WYreH7CB5ak+iUzPTtHSvZH32LWcYGxsX2Yp7KdIwyI2KJNx1ZpgIZ5TCURqm3qAAkNKona5qn3pkkP1QCZSbnM5QkXDG2MQpWA+fq7IuyAA8lh2e3TPNbASfBHxRkVwZI7QPkpqqUs2OjcAWLqbERv0j5uIqt685UM9bKFjUb8Swu7MFr4eX71fn/Z1jGHZ3j+CjdzfY3uufHr31OvDycAbPN4/3T90sP/B7/uKgfuckcG9/JXy//8XtFz4WiqweTJFchTi8Jtmbtq0WnLqzsl4hmmj73BeLuXTe56/FVKXl/Pt++f6XB51988Mw6ByI6tvqQxIjc+trLUHUONDYGNHz2XIhnVzILZYzuVQmITr0CawgFWQ="""
print(f"{C.zlib.decompress(C.base64.b64decode(b64)).decode('utf-8').rstrip('\n')} | {C.lb}{Date}{C.r}")
print("————————|——————————————————|—————————————————|——————————————|————")


# ---------------- Target All Classes Folder ---------------
def Find_Smali_Folders(decompile_dir, isAPKEditor):

    smali_path = C.os.path.join(decompile_dir, "smali") if isAPKEditor else decompile_dir
    prefix = "classes" if isAPKEditor else "smali_classes"

    folders = sorted([f for f in C.os.listdir(smali_path) if f == "smali" or f.startswith(prefix)], key=lambda x: int(x.split(prefix)[-1]) if x.split(prefix)[-1].isdigit() else 0)
    
    return [C.os.path.join(smali_path, f) for f in folders]


# ---------------- Execute Main Function ---------------
def RK_Techno_IND():
    args = parse_arguments()
    isCoreX = args.Hook_CoreX
    instruction(args.Credits_Instruction)
    isFlutter = args.Flutter; isPairip = args.Pairip
    Skip_Patch = args.Skip_Patch if args.Skip_Patch else []
    isAPKEditor = args.APKEditor; isEmulator = args.For_Emulator
    if isEmulator: F.isEmulator(); F.F_D_A()
    
    apk_path = args.input or args.Merge

    if not C.os.path.isfile(apk_path):
        exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} APK file '{apk_path}' not found. ✘\n\n\n{C.lb}[ {C.y}FYI ! {C.lb}] {C.g}Make Sure There Is 'No Extra Space' In The Folder/Apk Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.\n")
    
    if args.CA_Certificate:
        isCert =[Cert for Cert in args.CA_Certificate if not C.os.path.isfile(Cert)]
        if isCert:
            exit(f"\n{C.rd}Not exist: {', '.join(isCert)}\n")

    apk_path = Anti_Split(apk_path, args.Merge, isCoreX)

    # ---------------- Set All Paths Directory ----------------
    decompile_dir = C.os.path.join(C.os.path.expanduser("~"), f"{C.os.path.splitext(C.os.path.basename(apk_path))[0]}_decompiled")
    build_dir = C.os.path.abspath(C.os.path.join(C.os.path.dirname(apk_path), f"{C.os.path.splitext(C.os.path.basename(apk_path))[0]}_Patched.apk"))
    rebuild_dir = build_dir.replace('_Patched.apk', '_Patch.apk')
    manifest_path = C.os.path.join(decompile_dir, 'AndroidManifest.xml')

    if C.os.name == 'posix':
        C.subprocess.run(['termux-wake-lock'])
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Acquiring Wake Lock...\r")

    # ---------------- Check Flutter / Pairip Protection ---------------
    Flutter_lib = []; Pairip_lib = []

    with C.zipfile.ZipFile(apk_path, 'r') as zip_ref:
        for item in zip_ref.infolist():
            if item.filename.startswith('lib/'):
                if item.filename.endswith('libflutter.so'):
                    Flutter_lib.append(item.filename)
                elif item.filename.endswith('libpairipcore.so'):
                    Pairip_lib.append(item.filename)

    start_time = C.time.time()

    # ---------------- Scan & Decompile APK ---------------
    Package_Name = Scan_Apk(apk_path, isFlutter, Flutter_lib, isPairip, Pairip_lib)
    Decompile_Apk(apk_path, decompile_dir, isEmulator, isAPKEditor, args.AES_Logs)
    smali_folders = Find_Smali_Folders(decompile_dir, isAPKEditor)

    # ---------------- AES Logs Inject ----------------
    if args.AES_Logs:
        Copy_AES_Smali(decompile_dir, smali_folders, manifest_path, args.AES_S, isAPKEditor)
        Permission_Manifest(decompile_dir, manifest_path, isAPKEditor)

    # ---------------- Remove Ads ----------------
    if args.Remove_Ads:
        Ads_Smali_Patch(smali_folders)

    # ---------------- Fake / Spoof Device Info ----------------
    if args.Random_Info:
        Patch_Random_Info(smali_folders, args.Android_ID)

    if args.AES_Logs or args.Remove_Ads or args.Random_Info:
        Fix_Manifest(manifest_path, smali_folders, args.Spoof_PKG)
    else:
        if isFlutter and Flutter_lib:
            Patch_Flutter_SSL(decompile_dir, isAPKEditor)

        # ---------------- Smali Patching / Hook CoreX ----------------
        if isCoreX and isPairip and Pairip_lib and Check_CoreX(decompile_dir, isAPKEditor):
            C.shutil.rmtree(decompile_dir)
            exit(0)

        Smali_Patch(decompile_dir, smali_folders, isAPKEditor, args.CA_Certificate, args.Android_ID, isPairip, Pairip_lib, args.Spoof_PKG, args.Purchase, args.Remove_SC, Skip_Patch, args.Remove_USB, isCoreX)

        if isCoreX and isPairip and Pairip_lib:
            Hook_Core(args.input, decompile_dir, isAPKEditor, Package_Name)

        # ---------------- Patch Manifest & Write Network Config ----------------
        Fix_Manifest(manifest_path, smali_folders, args.Spoof_PKG)
        Patch_Manifest(decompile_dir, manifest_path)
        Write_Net_Config(decompile_dir, isAPKEditor, args.CA_Certificate)

    # ---------------- Recompile APK ----------------
    Recompile_Apk(decompile_dir, apk_path, build_dir, isEmulator, isAPKEditor)

    # ---------------- Fix CRC / Sign APK ----------------
    if not isCoreX and isPairip and Pairip_lib:
    
        if not isAPKEditor:
            FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir);

        CRC_Fix(apk_path, build_dir, ["AndroidManifest.xml", ".dex"])

    else:
        Sign_Apk(build_dir)

    if C.os.path.exists(build_dir):
        print(f'{C.lb}[{C.c}  Final APK  {C.lb}] {C.g}︻デ═一 {C.y} {build_dir}  {C.g}✔')

    print(f"\n{C.r}{'_' * 61}\n")
    if not isCoreX and isPairip and Pairip_lib:
        print(f'\n{C.lb}[{C.y} FYI ! {C.lb}] {C.c}This is Pairip Apk So U Install {C.g}( Keep Apk Without Sign ) {C.c}in VM / Multi_App\n')

    elapsed_time = C.time.time() - start_time

    print(f'\n{C.lb}[{C.c}  Time Spent  {C.lb}] {C.g}︻デ═一 {C.y}{elapsed_time:.2f} {C.r}Seconds {C.g}✔\n')
    print(f'\n🚩 {C.r}࿗ {C.rkj}Jai Shree Ram {C.r}࿗ 🚩\n     🛕🛕🙏🙏🙏🛕🛕\n')

    if C.os.name == 'posix':
        C.subprocess.run(['termux-wake-unlock'])
        exit(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Releasing Wake Lock...\n")
    exit(0)