from .C_M import CM; C = CM()
from .Files_Check import __version__


Tag = f"\n{C.r}————|———————|————{C.g}•❀ {C.rkj}Tag {C.g}❀•{C.r}————|———————|————\n"
EX = f"{C.pr}\n   |\n   ╰{C.r}┈{C.rkj}➢ {C.g}ApkPatcher -i Your_Apk_Path.apk {C.rkj}"
Info = f"{C.lb}[ {C.y}INFO {C.lb}] {C.c}"


class CustomArgumentParser(C.argparse.ArgumentParser):
    # ---------------- Error Handling ----------------
    def error(self, message):
        suggestion = ""
        for action in self._actions:
            if action.option_strings and any(option in message for option in action.option_strings):
                if action.dest == 'input':
                    suggestion = f'\n{C.lb}[ {C.y}FYI ! {C.lb}] {C.g}Make Sure There Is "No Extra Space" In The Folder/Apk Name In The Input Text. If Yes, Then Remove Extra Space & Correct It By Renaming It.\n\n\n{Info}With Your Certificate Flag: {C.rkj}-c {C.pr}( Input Your pem/crt/cert Path ){EX}-c {C.y}certificate.cert\n\n\n{Info}If you are using an Emulator in PC Then Use Flag: {C.rkj}-e{EX}-c {C.y}certificate.cert {C.rkj}-e\n'
                elif action.dest == 'Merge':
                    suggestion = f'\n{Info}Only Merge Apk\n\n\n{Info}Merge Extension {C.y}( .apks/.xapk/.apkm )\n\n\n{C.lb}[ {C.y}Ex. {C.lb}] {C.g}ApkPatcher {C.rkj}-m {C.g}Your_Apk_Path.apks\n'
                break

        exit(f'\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} {message}\n\n{suggestion}')

    # ---------------- Print Help ----------------
    def print_help(self):
        super().print_help()
        print(f"\n{Info} ApkPatcher Default Patch is VPN & SSL Bypass, Show Other Patch Flags List with: {C.g}ApkPatcher -O{C.c}\n")

    # ---------------- Other Patch ----------------
    def Other_Patch(self):
        print(f"""\n{C.lb}[ {C.pr}* {C.lb}] {C.c}Other Patch Flags Help ( Keep Sequence in Mind )

 <Flags>                 {C.g}─•❀•❀ {C.c}Info Patch {C.g}❀•❀•─{C.rkj}

  -A, {C.c}--AES_Logs         {C.y}➸ {C.g}AES Logs Inject{C.rkj}
  -D, {C.c}--Android_ID       {C.y}➸ {C.g}Hook Android ID for One Device Login Bypass{C.rkj}
  -f, {C.c}--Flutter          {C.y}➸ {C.g}Flutter SSL Bypass{C.rkj}
  -p, {C.c}--Pairip           {C.y}➸ {C.g}Pairip CERT SSL Bypass (No Sign){C.rkj}
  -P, {C.c}--Purchase         {C.y}➸ {C.g}Purchase/Paid/Price{C.rkj}
  -r, {C.c}--Random_Info      {C.y}➸ {C.g}Fake Device Info{C.rkj}
  -rmads, {C.c}--Remove_Ads   {C.y}➸ {C.g}Bypass Ads{C.rkj}
  -rmsc, {C.c}--Remove_SC     {C.y}➸ {C.g}Bypass Screenshot Restriction{C.rkj}
  -rmu, {C.c}--Remove_USB     {C.y}➸ {C.g}Bypass USB Debugging Permission{C.rkj}
  -pkg, {C.c}--Spoof_PKG      {C.y}➸ {C.g}Spoof Package Detection{C.rkj}
  -skip {C.c}[Skip_Patch ...] {C.y}➸ {C.g}Skip Specific Patches (e.g. getAcceptedIssuers){C.rkj}
  -s, {C.c}--AES_S            {C.y}➸ {C.g}Do U Want Separate AES.smali Dex{C.rkj}
  -x, {C.c}--Hook_CoreX       {C.y}➸ {C.g}Hook CoreX Flag: {C.rkj}-p -x {C.pr}( Only For [ arm64 ] )""")
        user_input = input(f"\n\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Do See Example\n{C.g}  |\n  └──── {C.r}~ y / Exit to Enter {C.g}$ : {C.y}")

        if user_input.lower() == "y":
            print(f"""\n{Tag.replace("Tag", "AES Logs Inject")}

{Info}AES MT Logs Inject Flag: {C.rkj}-A{EX}-A\n\n\n{Info}Do U Want Separate AES.smali Dex Use Flag: {C.rkj}-A -s{EX}-A -s

{Tag.replace("Tag", "Hook Android ID")}

{Info}Hook Android ID For One Device Login Bypass Use Flag: {C.rkj}-D {C.pr}( Input Your Original 16 Digit Android ID ){EX}-D {C.y}7e9f51f096bd5c83

{Tag.replace("Tag", "isFlutter / isPairip")}

{Info}If Apk is Flutter Then Use Additional Flag: {C.rkj}-f{EX}-f {C.y}-c certificate.cert\n\n\n{Info}If Apk is Pairip Then Use Additional Flag: {C.rkj}-p {C.pr}( Without Sign Apk Use Only in VM / Multi_App ){EX}-p {C.y}-c certificate.cert\n\n\n{Info}If Apk is Pairip Then Hook CoreX Use Additional Flag: {C.rkj}-p -x {C.pr}( Install Directly Only For [ arm64 ] ){EX}-p -x {C.y}-c certificate.cert

{Tag.replace("Tag", "Spoof PKG / Device Info")}

{Info}Spoof Package Detection Flag: {C.rkj}-pkg {C.pr}( Dex / Manifest / Res ){EX}-pkg\n\n\n{Info}Fake Device Info Flag: {C.rkj}-r{EX}-r\n\n\n{Info}With Your Android ID Flag: {C.rkj}-r -D {C.pr}( Input Your Custom 16 Digit Android ID ){EX}-r -D {C.y}7e9f51f096bd5c83

{Tag.replace("Tag", "Bypass Ads / SC / USB")}

{Info}Bypass Ads Flag: {C.rkj}-rmads{EX}-rmads\n\n\n{Info}Bypass Screenshot Restriction Flag: {C.rkj}-rmsc{EX}-rmsc\n\n\n{Info}Bypass USB Debugging Permission Flag: {C.rkj}-rmu{EX}-rmu

{Tag.replace("Tag", "isPurchase / Skip Patch")}

{Info}Purchase / Paid / Price Flag: {C.rkj}-P{EX}-P\n\n\n{Info}Skip Patch Flag: {C.rkj}-skip{EX}-skip {C.y}getAcceptedIssuers\n""")
        else:return


# ---------------- Parse Arguments ----------------
def parse_arguments():
    args = C.sys.argv[1:]
    if '-O' in args: exit(CustomArgumentParser().Other_Patch())
    parser = CustomArgumentParser(description=f'{C.c}ApkPatcher v{__version__}') if any(arg.startswith('-') for arg in args) else C.argparse.ArgumentParser(description=f'{C.c}ApkPatcher v{__version__}')

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-i', dest='input', help=f'{C.y}➸{C.g} Input APK Path...{C.c}')
    group.add_argument('-m', dest='Merge', help=f'{C.y}➸{C.g} Anti-Split ( Only Merge Apk ){C.c}')
    group.add_argument('-C', dest='Credits_Instruction', action='store_true', help=f'{C.y}➸{C.g} Show Instructions & Credits{C.c}')

    additional = parser.add_argument_group(f'{C.rkj}[ * ] Additional Flags{C.c}')
    additional.add_argument('-a', '--APKEditor', action='store_true', help=f'{C.y}➸ {C.g}APKEditor ( Default APKTool ){C.c}')
    additional.add_argument('-e', '--For_Emulator', action='store_true', help=f'{C.y}➸{C.g} If using emulator on PC then use -e flag{C.c}')
    additional.add_argument('-c', dest='CA_Certificate', type=str, nargs='*', help=f"{C.y}➸{C.g} Input Your HttpCanary/Reqable/ProxyPin etc. Capture Apk's CA-Certificate{C.c}")

    # ---------------- Other Patch Flags ----------------
    parser.add_argument('-A', '--AES_Logs', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-D', '--Android_ID', type=str, help=C.argparse.SUPPRESS)
    parser.add_argument('-f', '--Flutter', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-p', '--Pairip', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-P', '--Purchase', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-r', '--Random_Info', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-rmads', '--Remove_Ads', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-rmsc', '--Remove_SC', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-rmu', '--Remove_USB', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-pkg', '--Spoof_PKG', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-skip', dest='Skip_Patch', nargs='*', help=C.argparse.SUPPRESS)
    parser.add_argument('-s', '--AES_S', action='store_true', help=C.argparse.SUPPRESS)
    parser.add_argument('-x', '--Hook_CoreX', action='store_true', help=C.argparse.SUPPRESS)

    Ext = ('.apk', '.apks', '.apkm', '.xapk')  
    fixed = []; start = None; Valid_Ext = False  

    for i, a in enumerate(args):  
        if a in ['-i', '-m', '-L', '-rm', '-r', '-C']:  
            start, fixed = i + 1, fixed + [a]  
        elif start and (a.endswith(Ext) or C.os.path.isdir(a)):  
            fixed, start = fixed + [' '.join(args[start:i+1])], None  
            Valid_Ext = True  
        elif not start:  
            fixed.append(a)  

    if not Valid_Ext and C.sys.argv[1:2] != ['-C']:
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Only Supported Extensions {C.g}{Ext}\n")

    print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Input Path {C.g}➸❥{C.y}", *fixed, f"{C.r}\n")

    return parser.parse_args(fixed)