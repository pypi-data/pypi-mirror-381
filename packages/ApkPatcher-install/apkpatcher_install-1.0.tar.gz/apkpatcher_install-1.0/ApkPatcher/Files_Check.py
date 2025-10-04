from .C_M import CM; C = CM()

__version__ = 1.0


# ---------------- Set Path ----------------
run_dir = C.os.path.dirname(C.os.path.abspath(C.sys.argv[0]))
script_dir = C.os.path.dirname(C.os.path.abspath(__file__))


class FileCheck:
    # ---------------- Set Jar & Files Paths ----------------
    def Set_Path(self):
        self.APKEditor_Path = C.os.path.join(run_dir, "APKEditor.jar")
        self.APKTool_Path = C.os.path.join(run_dir, "APKTool_AP.jar")
        self.Sign_Jar = C.os.path.join(run_dir, "Uber-Apk-Signer.jar")
        self.AES_Smali = C.os.path.join(script_dir, "AES.smali")
        self.Pairip_CoreX = C.os.path.join(script_dir, "lib_Pairip_CoreX.so")


    def isEmulator(self):
        self.APKTool_Path_E = C.os.path.join(run_dir, "APKTool_OR.jar")


    # ---------------- SHA-256 CheckSum ----------------
    def Calculate_CheckSum(self, file_path):
        sha256_hash = C.hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except FileNotFoundError:
            return None


    # ---------------- Download Files ----------------    
    def Download_Files(self, Jar_Files):
        import requests
        downloaded_urls = set()
        for File_URL, File_Path, Expected_CheckSum in Jar_Files:
            File_Name = C.os.path.basename(File_Path)

            if C.os.path.exists(File_Path):
                if self.Calculate_CheckSum(File_Path) == Expected_CheckSum:
                    continue
                else:
                    print(f"{C.rd}[ {C.pr}File {C.rd}] {C.c}{File_Name} {C.rd}is Corrupt (Checksum Mismatch).\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Re-Downloading, Need Internet Connection.\n")
                    C.os.remove(File_Path)

            try:
                Version = C.re.findall(r'version = "([^"]+)"', requests.get("https://raw.githubusercontent.com/TechnoIndian/ApkPatcher/main/pyproject.toml").text)[0]

                if Version != str(__version__):
                    print(f"\n{C.lb}[ {C.y}Updating {C.lb}] {C.c} ApkPatcher ➸❥ {C.g}{Version}...\n\n")

                    cmd = (["pip", "install", "git+https://github.com/TechnoIndian/ApkPatcher.git"] if C.os.name == "nt" else "pip install --force-reinstall https://github.com/TechnoIndian/ApkPatcher/archive/refs/heads/main.zip")

                    C.subprocess.run(cmd, shell=isinstance(cmd, str), check=True)

                print(f'\n{C.lb}[ {C.pr}Downloading {C.lb}] {C.c}{File_Name}')

                with requests.get(File_URL, stream=True) as response:
                    if response.status_code == 200:
                        total_size = int(response.headers.get('content-length', 0))
                        with open(File_Path, 'wb') as f:
                            print(f'       |')
                            for data in response.iter_content(1024 * 64):
                                f.write(data)

                                print(f"\r       {C.r}╰┈ PS {C.rkj}➸❥ {C.g}{f.tell()/(1024*1024):.2f}/{total_size/(1024*1024):.2f} MB ({f.tell()/total_size*100:.1f}%)", end='', flush=True)

                        print(' ✔\n')

                    else:
                        exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Failed to download {C.y}{File_Name} {C.rd}Status Code: {response.status_code}\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Restart Script...\n')

            except requests.exceptions.RequestException:
                exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Got an error while Fetching {C.y}{File_Path}\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} No internet Connection\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Internet Connection is Required to Download {C.y}{File_Name}\n')


    # ---------------- Files Download Link ----------------
    def F_D(self):

        self.Download_Files(
            [
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKEditor.jar",
                    self.APKEditor_Path,
                    "71999a1f28cf6b457aff17c139436349cd6ea30d75a0f9cd52f07bd52e21897b"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar" if C.os.name == 'nt' else "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool_Modified.jar",

                    self.APKTool_Path,

                    "66cf4524a4a45a7f56567d08b2c9b6ec237bcdd78cee69fd4a59c8a0243aeafa" if C.os.name == 'nt' else "4bd618905d147f5b9235c583863d8c766045c4ac1f85713aa74b5766899d1214"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/Uber-Apk-Signer.jar",
                    self.Sign_Jar,
                    "e1299fd6fcf4da527dd53735b56127e8ea922a321128123b9c32d619bba1d835"
                ),
                (
                    "https://raw.githubusercontent.com/TechnoIndian/Objectlogger/refs/heads/main/AES.smali",
                    self.AES_Smali,
                    "09db8c8d1b08ec3a2680d2dc096db4aa8dd303e36d0e3c2357ef33226a5e5e52"
                ),
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/lib_Pairip_CoreX.so",
                    self.Pairip_CoreX,
                    "22a7954092001e7c87f0cacb7e2efb1772adbf598ecf73190e88d76edf6a7d2a"
                )
            ]
        )

        C.os.system('cls' if C.os.name == 'nt' else 'clear')


    # ---------------- Files Download isEmulator ----------------
    def F_D_A(self):

        self.Download_Files(
            [
                (
                    "https://github.com/TechnoIndian/Tools/releases/download/Tools/APKTool.jar",
                    self.APKTool_Path_E,
                    "66cf4524a4a45a7f56567d08b2c9b6ec237bcdd78cee69fd4a59c8a0243aeafa"
                )
            ]
        )