from .CRC import CRC_Fix
from .Scan import Scan_Apk
from .C_M import CM;  C = CM()
from .Flutter_SO import Flutter_SO
from .Smali_Patch import Smali_Patch
from .Argparse import parse_arguments
from .Instruction_Credit import instruction
from .CoreX import Check_CoreX, Hook_Core
from .Anti_Splits import Anti_Split, Check_Split
from .Files_Check import FileCheck, __version__
from .Extract import Extract_Smali, Logs_Injected
from .Fix_Dex import Scan_Application, Smali_Patcher, Replace_Strings
from .Decompile_Compile import Decompile_Apk, Recompile_Apk, FixSigBlock
from .Manifest_Patch import Patch_Manifest, Replace_Application, Encode_Manifest
from .Other_Patch import Application_Name, Translate_Smali_Name, Merge_Smali_Folders, UnMerge

def Clear():
    C.os.system('cls' if C.os.name == 'nt' else 'clear')
Clear()

# ---------------- Install Require Module ---------------
required_modules = ['requests', 'multiprocess']
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

# ---------------- Check Dependencies ----------------
def check_dependencies():
    try:
        C.subprocess.run(['java', '-version'], check=True, text=True, capture_output=True)
    except (C.subprocess.CalledProcessError, FileNotFoundError):
        if C.os.name == 'posix':
            install_package('openjdk-17')
        else:
            exit(f'\n\n{C.lb}[ {C.rd}Error ! {C.lb}]{C.rd} Java is not installed on Your System. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Install Java and run script again in new CMD. ✘\n\n{C.lb}[ {C.y}INFO ! {C.lb}]{C.rd} Verify Java installation using {C.rd}"{C.g}java --version{C.rd}" command in CMD')

    if C.os.name == 'posix': install_package('aapt')

# ---------------- Install Package ----------------
def install_package(pkg):
    try:
        result = C.subprocess.run(['pkg', 'list-installed'], capture_output=True, text=True, check=True)
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
b64 = """eJzVlc1KAzEQx8/NK3gZwl6FWvELL9YPcCnUUgsiPZRSFy02LVRzEHooKnpRqVTxJOJZ0IMXQcQXUPARtPXkxT6CSTbJJttW1Juz2/3I/zeTmcluF0DYQHaIDGSHxydHJmPRGOlc7F+z3y0seaVChXiWPkamt+TARIxkvMJauQJueaWYZ6NR7YtQJALUNwSmUeoEZomW0qVzMZQoyOkHjQS4k+XTyzThA7ocSMXdtJuC6eVUfHFRxevifxDSwewSG2cTwQoQOJWjYlCnznkIIzx2D4Lal0FLsd9DdpA8tSfRqZlpWnpQsj6HltPBxsZFtuJBitQBuVGRhL/ODBPhjFI4Sh0aDAoAKY3a6ar2qUcG2Q+VQLnJ6QwVCWeMTZyC9fD5KuuCDMBj2eHZPdPMRvBJIBQVyZUxQocgqakq1ezYCGzhYkps1N9lPq5y68+Bet4ivUX9SnSau9vwdnT5cXXe2j2GTnOvAZ939+2d/dZp4/2uDq+PZ/By8/Tw3EzwA7/n7w1q1U967rV+wvf7X9x+4WOhyOrBKEnmicdrkr2p2WrGK3mr1TzRRC3kvrCUnEuH/LU4m9/0/n2/Qv/L7fqB+WFo1w9F9TX1IRkhU9X1TUEUOVDe6NLTiVxmbmY+uZBzk7NuXHToCwiuFdA="""
print(f"{C.zlib.decompress(C.base64.b64decode(b64)).decode('utf-8').rstrip('\n')} | {C.lb}{Date}{C.r}")
print("————————|——————————————————|—————————————————|——————————————|————")


# ---------------- Target All Classes Folder ----------------
def Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex):
    smali_path = decompile_dir if isAPKTool or Fix_Dex else C.os.path.join(decompile_dir, "smali")
    prefix = "smali_classes" if isAPKTool or Fix_Dex else "classes"
    folders = sorted([f for f in C.os.listdir(smali_path) if f == "smali" or f.startswith(prefix)], key=lambda x: int(x.split(prefix)[-1]) if x.split(prefix)[-1].isdigit() else 0)
    
    return [C.os.path.join(smali_path, f) for f in folders]


# ---------------- Target Last Classes Folder ----------------
def L_S_C_F(decompile_dir, isAPKTool, Fix_Dex):
    smali_folders = Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex)
    return smali_folders[-1] if smali_folders else None


# ---------------- Execute Main Function ----------------
def RK_Techno_IND():
    args = parse_arguments()
    M_Skip=args.MergeSkip
    CoreX_Hook=args.Hook_CoreX; isCoreX=False
    Credit=args.Credits_Instruction; instruction(Credit)
    isAPKTool=args.ApkTool; Fix_Dex=args.Repair_Dex
    if isAPKTool or Fix_Dex: F.F_D_A()
    
    apk_path = args.input or args.Merge

    if not C.os.path.isfile(apk_path):
        exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd} APK file '{apk_path}' not found. ✘\n")

    apk_path = Anti_Split(apk_path, args.Merge, CoreX_Hook)

    # ---------------- Set All Paths Directory ----------------
    decompile_dir = C.os.path.join(C.os.path.expanduser("~"), f"{C.os.path.splitext(C.os.path.basename(apk_path))[0]}_decompiled")
    build_dir = C.os.path.abspath(C.os.path.join(C.os.path.dirname(apk_path), f"{C.os.path.splitext(C.os.path.basename(apk_path))[0]}_Pairip.apk"))
    rebuild_dir = build_dir.replace('_Pairip.apk', '_Patched.apk')
    manifest_path = C.os.path.join(decompile_dir, 'AndroidManifest.xml')
    d_manifest_path = C.os.path.join(decompile_dir, 'AndroidManifest_d.xml')
    mtd_path = "/sdcard/MT2/dictionary/"

    C_Line = f"{C.r}{'_' * 61}"
    Logo = f'\n🚩 {C.r}࿗ {C.rkj}Jai Shree Ram {C.r}࿗ 🚩\n     🛕🛕🙏🙏🙏🛕🛕\n'
    START = f'\n{C.lb}[{C.c}  Time Spent  {C.lb}] {C.g}︻デ═一 {C.y}'; END=f'{C.r} Seconds\n'

    if C.os.name == 'posix':
        C.subprocess.run(['termux-wake-lock'])
        print(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Acquiring Wake Lock...\r")

    start_time = C.time.time()

    # ---------------- Scan & Decompile APK ---------------
    Package_Name, License_Check, isFlutter = Scan_Apk(apk_path)

    if input and isFlutter:
        Flutter_SO(apk_path, isFlutter)

    Decompile_Apk(apk_path, decompile_dir, isAPKTool, Fix_Dex)

    # ---------------- Last Smali Folder & All Smali Folder ---------------
    L_S_F = L_S_C_F(decompile_dir, isAPKTool, Fix_Dex)
    smali_folders = Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex)

    # ---------------- Fix Dex Flag: -r ---------------
    if Fix_Dex:
        try:
            App_Name = Scan_Application(apk_path, manifest_path, d_manifest_path, Fix_Dex)
            if App_Name:
                Super_Value = Application_Name(L_S_F)
                print(f'\n{C.lb}[{C.c}  APPLICATION  {C.lb}] {C.g}︻デ═一 {Super_Value}  ✔\n')
                Replace_Application(manifest_path, d_manifest_path, Super_Value, App_Name, isAPKTool, Fix_Dex)
                Encode_Manifest(decompile_dir, manifest_path, d_manifest_path)
            else:
                C.os.remove(d_manifest_path)
                pass

            Smali_Patcher(smali_folders, L_S_F); build_dir = rebuild_dir
            Recompile_Apk(decompile_dir, Fix_Dex, build_dir, isFlutter)
            C.shutil.rmtree(decompile_dir)

            elapsed_time = C.time.time() - start_time

            print(START + f'{elapsed_time:.2f}' + END)
            print(Logo)

            if C.os.name == 'posix':
                C.subprocess.run(['termux-wake-unlock'])
                exit(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Releasing Wake Lock...\n")
            exit(0)

        except Exception as e:
            exit(f"\n{C.lb}[ {C.rd}Error ! {C.lb}] {C.rd}{e} ✘\n")

    # ---------------- Extract Target Smali & Logs Inject ---------------
    if not (CoreX_Hook or License_Check):
        Extract_Smali(decompile_dir, smali_folders, isAPKTool)

    L_S_F = L_S_C_F(decompile_dir, isAPKTool, Fix_Dex)

    if not (CoreX_Hook or License_Check):
        Logs_Injected(L_S_F)
        Super_Value = Application_Name(L_S_F)
        OR_App=f'\n{C.lb}[{C.c}  APPLICATION  {C.lb}] {C.g}︻デ═一 {Super_Value}  ✔\n'
        smali_folders = Find_Smali_Folders(decompile_dir, isAPKTool, Fix_Dex)

    # ---------------- Hook CoreX ---------------
    if CoreX_Hook and Check_CoreX(decompile_dir, isAPKTool):
        C.shutil.rmtree(decompile_dir);
        exit(0)

    Smali_Patch(smali_folders, CoreX_Hook, isCoreX)

    if CoreX_Hook or isCoreX:
        Hook_Core(args.input, decompile_dir, isAPKTool, Package_Name)

    if not isAPKTool:
        d_manifest_path = manifest_path

    # ---------------- Patch Manifest ---------------
    Patch_Manifest(decompile_dir, manifest_path, d_manifest_path, isAPKTool, L_S_F, CoreX_Hook, isFlutter, isCoreX)

    if isAPKTool:
        Encode_Manifest(decompile_dir, manifest_path, d_manifest_path)
    
    if not (CoreX_Hook or License_Check):
        # ---------------- Merge Smali ---------------
        if M_Skip:
            print(f"\n{C.lb}[ {C.y}INFO ! {C.lb}] {C.g} Skip Merge Last Dex {C.y}{C.os.path.basename(L_S_F)} {C.g} & Add Seprate (For Dex Redivision)\n")
            pass
        else:
            Merge_Smali_Folders(decompile_dir, isAPKTool, L_S_F)

        Translate_Smali = Translate_Smali_Name(C.os.path.basename(L_S_C_F(decompile_dir, isAPKTool, Fix_Dex)), isAPKTool) if L_S_C_F(decompile_dir, isAPKTool, Fix_Dex) else "No Smali classes folder found."

    # ---------------- Recompile APK ---------------
    Recompile_Apk(decompile_dir, isAPKTool, build_dir, isFlutter)

    if CoreX_Hook or License_Check:
        CRC_Fix(M_Skip, apk_path, build_dir, ["AndroidManifest.xml", ".dex"])
        C.shutil.rmtree(decompile_dir)

        print(f"{C_Line}\n\n" + START + f'{C.time.time() - start_time:.2f}' + END + f'\n{Logo}')

        if C.os.name == 'posix':
            C.subprocess.run(['termux-wake-unlock'])
            exit(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Releasing Wake Lock...\n")
        exit(0)

    # ---------------- CRCFix ---------------
    Final_Apk = CRC_Fix(M_Skip, apk_path, build_dir, ["AndroidManifest.xml", ".dex"])

    if isAPKTool:
        FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir)

    print(f'\n{C.lb}[{C.c}  Final APK  {C.lb}] {C.g}︻デ═一 {C.y} {Final_Apk}  {C.g}✔\n')

    elapsed_time = C.time.time() - start_time

    print(f"{C_Line}\n\n\n{C.lb}[{C.c}  Last Dex  {C.lb}] {C.g}︻デ═一 {C.pr}'{C.g}{C.os.path.basename(Translate_Smali)}{C.pr}' {C.y}( Translate with MT )  {C.g}✔\n")

    # ---------------- APPLICATION NAME ---------------
    print(OR_App)
    print(START + f'{elapsed_time:.2f}' + END + f"\n{C_Line}\n")

    if C.os.path.exists(mtd_path):
        mtd_files = [file for file in C.os.listdir(mtd_path) if file.startswith(Package_Name) and file.endswith('.mtd')]

        for mtd_file in mtd_files:
            C.os.remove(C.os.path.join(mtd_path, mtd_file))

    print(f'\n{C.lb}[ {C.y}INFO {C.lb}] {C.g} If U Want Repair Dex Without Translate, So Generate .mtd First & put the .mtd in the path of {C.y}"/sdcard/MT2/dictionary/"{C.g}, if .mtd available in target path then The Script will handle Automatically, So Press Enter 🤗🤗\n')

    while True:
        UnMerge_input = input(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Do U Want Repair Dex (Press Enter To Proceed or 'q' to exit or 'm' to More Info) | Hook If Apk Crash Then Try with 'x'\n{C.g}  |\n  └──── {C.r}~{C.g}$ : {C.y}").strip().lower()

        if UnMerge_input == 'q':
            C.shutil.rmtree(decompile_dir)

            print(f"\n{C_Line}\n\n\n{C.lb}[{C.y} INFO ! {C.lb}] {C.c} Now you have to manually Translate the Last Dex with MT & again input with -r Flag the Command {C.g}( Copy Below Command & Run After Translate Dex )\n{C.g}  |\n  └──── {C.r}~{C.g}${C.y}  RKPairip -i {build_dir} -r\n\n{C_Line}\n")

            break

        elif UnMerge_input == 'm':

            print(f'\n{C_Line}\n\n\n{C.lb}[{C.y} MORE INFO {C.lb}] {C.g} - To generate .mtd file, first install the {C.rkj}“{C.os.path.basename(apk_path)}”{C.g} in Multi App/Dual Space and save the .mtd in "/sdcard/MT2/dictionary/"\n\n{C.lb}[{C.y} NOTE {C.lb}] {C.g} - if u use root or VM so .mtd will save path of {C.y}"/data/data/{Package_Name}/dictionary/" {C.g}& then u just move .mtd file to path of {C.y}"/sdcard/MT2/dictionary/"\n\n{C.lb}[{C.y} FYI {C.lb}] {C.g} - Make sure you have generated a new .mtd before pressing enter as using the old .mtd may cause a apk crash\n\n{C.lb}[{C.y} INFO {C.lb}] {C.g} - The script will handle it automatically if the .mtd file exists in the target path.\n')

            continue

        elif UnMerge_input == 'x' and not (CoreX_Hook or Check_CoreX(decompile_dir, isAPKTool) or Check_Split(args.input, isCoreX=True)):

            print(f"\n{C_Line}\n\n\n{C.lb}[{C.y} Info {C.lb}] {C.c}Hook lib_Pairip_CoreX.so & loadLibrary in VMRunner Class.{C.g}\n    |\n    └──── {C.r}~{C.g}${C.y} This Hook Work in Some Apk Like Flutter/Unity & Try on Crash Apk.{C.g}\n    |\n    └──── {C.r}~{C.g}${C.y} Note Some Time This Apk Working Directly with Sign When Directly Working Hook Then why need Bypass Pairip, because u can also modify dex in Apk.{C.g}\n    |\n    └──── {C.r}~{C.g}${C.y} Still U want Bypass Pairip then Dump '.mtd' & Press Enter ( for mtd dump Use  Multi_App cuz Storage Permission not added in Apk )\n\n{C_Line}\n")
            
            Smali_Patch(smali_folders, CoreX_Hook, isCoreX=True)
            Patch_Manifest(decompile_dir, manifest_path, d_manifest_path, isAPKTool, L_S_F, CoreX_Hook, isFlutter, isCoreX=True)
            Hook_Core(args.input, decompile_dir, isAPKTool, Package_Name)
            Recompile_Apk(decompile_dir, isAPKTool, build_dir, isFlutter)

            # ---------------- CRCFix ---------------
            CRC_Fix(M_Skip, apk_path, build_dir, ["AndroidManifest.xml", ".dex"])

            if isAPKTool:
                FixSigBlock(decompile_dir, apk_path, build_dir, rebuild_dir)
            continue

        else:
            print(f"\n{C_Line}")

            if UnMerge:
                mtd_files = None

                while True:
                    if C.os.path.exists(mtd_path):
                        mtd_files = [file for file in C.os.listdir(mtd_path) if file.startswith(Package_Name) and file.endswith('.mtd')]

                        if not mtd_files:
                            print(f"\n\n{C.lb}[{C.y} Warn ! {C.lb}] {C.rd} No {C.g}{Package_Name}..... .mtd {C.g}file found in {C.y}{mtd_path}\n")

                        else:
                            if not M_Skip: UnMerge()

                            mtd_file = max(mtd_files, key=lambda file: C.os.path.getmtime(C.os.path.join(mtd_path, file)))

                            print(f"\n{C.lb}[{C.y} INFO ! {C.lb}] {C.c}Founded {C.g}➸❥ {mtd_file} ✔\n\n{C_Line}\n")

                            break

                    else:
                        print(f"\n\n{C.lb}[{C.y} Warn ! {C.lb}] {C.rd} No such directory found: {C.y}{mtd_path}\n")
                    user_input = input(f"\n{C.lb}[{C.y} Input {C.lb}] {C.c}If You Want To Retry, Press Enter & Exit To Script {C.pr}'q' : {C.y}")

                    if user_input.lower() == 'q':
                        break

                # ---------------- Restore Strings ---------------
                if mtd_files:
                    fix_time = C.time.time()
                    Smali_Patcher(smali_folders, L_S_F)
                    Replace_Strings(L_S_F, C.os.path.join(mtd_path, mtd_file))

                    if not M_Skip:
                        Merge_Smali_Folders(decompile_dir, isAPKTool, L_S_F)

                    App_Name = Scan_Application(apk_path, manifest_path, d_manifest_path, isAPKTool)
                    print(OR_App)

                    Replace_Application(manifest_path, d_manifest_path, Super_Value, App_Name, isAPKTool, Fix_Dex)

                    if isAPKTool:
                        Encode_Manifest(decompile_dir, manifest_path, d_manifest_path)

                    Recompile_Apk(decompile_dir, isAPKTool, build_dir, isFlutter)
                    C.shutil.rmtree(decompile_dir)

                    elapsed_time = C.time.time() - fix_time

                    print(START + f'{elapsed_time:.2f}' + END)

                    break

                else:
                    C.shutil.rmtree(decompile_dir)

                    print(f"\n{C_Line}\n\n\n{C.lb}[{C.y} INFO ! {C.lb}] {C.rd} No Valid .mtd File Found. ✘\n\n\n{C.lb}[{C.y} INFO ! {C.lb}] {C.c} Now you have to manually Translate the Last Dex with MT & again input with -r Flag the Command {C.g}( Copy Below Command & Run After Translate Dex )\n{C.g}  |\n  └──── {C.r}~{C.g}${C.y}  RKPairip -i {build_dir} -r\n\n{C_Line}\n")

                    break

    print(Logo)
    if C.os.name == 'posix':
        C.subprocess.run(['termux-wake-unlock'])
        exit(f"\n{C.lb}[ {C.pr}* {C.lb}] {C.c} Releasing Wake Lock...\n")
    exit(0)