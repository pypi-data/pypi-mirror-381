from .C_M import CM; C = CM()
from .Files_Check import FileCheck

F = FileCheck(); F.Set_Path()


# ---------------- Check CoreX ----------------
def Check_CoreX(decompile_dir, isAPKTool):

    Lib_CoreX = []

    lib_paths = C.os.path.join(decompile_dir,
            *(
                ['lib', 'arm64-v8a'] if isAPKTool else ['root', 'lib', 'arm64-v8a']
            )
        )

    for arch in C.os.listdir(lib_paths):
        for root, _, files in C.os.walk(C.os.path.join(lib_paths, arch)):
            for target_file in ['lib_Pairip_CoreX.so', 'libFirebaseCppApp.so']:
                if target_file in files:
                    Lib_CoreX.append(f"{C.g}{target_file} ➸❥ {C.rkk}{arch}")

    if Lib_CoreX:
        print(f"\n\n{C.lb}[ {C.y}Info {C.lb}] {C.c}Already Added {C.rkj}➸❥ {f' {C.rkj}& '.join(Lib_CoreX)}{C.c} {C.g}✔")

        return True
    return False


# ---------------- HooK CoreX ----------------
def Hook_Core(apk_path, decompile_dir, isAPKTool, Package_Name):

    with C.zipfile.ZipFile(apk_path, 'r') as zf:
        base_apk = "base.apk" if "base.apk" in zf.namelist() else f"{Package_Name}.apk"

    try:
        if C.os.name == 'nt' and C.shutil.which("7z"):
            C.subprocess.run(["7z", "e", apk_path, base_apk, "-y"], text=True, capture_output=True)

            with C.zipfile.ZipFile(apk_path) as zf:
                zf.extract(base_apk)

        else:
            if C.shutil.which("unzip"):
                C.subprocess.run(["unzip", "-o", apk_path, base_apk], text=True, capture_output=True)

                with C.zipfile.ZipFile(apk_path) as zf:
                    zf.extract(base_apk)

        print(f'\n{C.lb}[ {C.c}Dump {C.lb}] {C.g}➸❥ {C.rkj}{base_apk}\n')

        Dump_Apk = "libFirebaseCppApp.so"
        C.os.rename(base_apk, Dump_Apk)

        lib_paths = C.os.path.join(decompile_dir,
            *(
                ['lib', 'arm64-v8a'] if isAPKTool else ['root', 'lib', 'arm64-v8a']
            )
        )

        print(f"\n{C.lb}[ {C.c}Arch {C.lb}] {C.g}➸❥ arm64-v8a\n")

        C.shutil.move(Dump_Apk, lib_paths); C.shutil.copy(F.Pairip_CoreX, lib_paths);

        print(f'\n{C.lb}[ {C.c}HooK {C.lb}] {C.g}➸❥ {C.rkj}libFirebaseCppApp.so {C.g}✔\n\n{C.lb}[ {C.c}HooK {C.lb}] {C.g}➸❥ {C.rkj}lib_Pairip_CoreX.so {C.g}✔\n')

        return True

    except Exception as e:
        print(f"\n{C.lb}[ {C.rd}Hook_Core Error ! {C.lb}] {C.rd}{e} ✘")