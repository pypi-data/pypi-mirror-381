from .C_M import CM; C = CM()


# ---------------- Smali Patch ----------------
def Smali_Patch(smali_folders, CoreX_Hook, isCoreX):

    target_files = [
        "SignatureCheck.smali",
        "LicenseClientV3.smali",
        "LicenseClient.smali",
        "Application.smali"
    ]

    if CoreX_Hook or isCoreX:
        target_files.append("VMRunner.smali")

    patterns = []

    if not (isCoreX and not CoreX_Hook):
        patterns.extend(
            [
                (
                    r'invoke-static \{[^\}]*\}, Lcom/pairip/SignatureCheck;->verifyIntegrity\(Landroid/content/Context;\)V',
                    r'#',
                    "VerifyIntegrity"
                ),
                (
                    r'(\.method [^(]*verifyIntegrity\(Landroid/content/Context;\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
                    r'\1\2',
                    "VerifyIntegrity"
                ),
                (
                    r'(\.method [^(]*verifySignatureMatches\(Ljava/lang/String;\)Z\s+.locals \d+\s+)[\s\S]*?(\s+return ([pv]\d+)\n.end method)',
                    r'\1const/4 \3, 0x1\2',
                    "verifySignatureMatches"
                ),
                (
                    r'(\.method [^(]*connectToLicensingService\(\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
                    r'\1\2',
                    "connectToLicensingService"
                ),
                (
                    r'(\.method [^(]*initializeLicenseCheck\(\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
                    r'\1\2',
                    "initializeLicenseCheck"
                ),
                (
                    r'(\.method [^(]*processResponse\(ILandroid/os/Bundle;\)V\s+.locals \d+)[\s\S]*?(\s+return-void\n.end method)',
                    r'\1\2',
                    "processResponse"
                )
            ]
        )

    # ---------------- loadLibrary ➢ '_Pairip_CoreX' ----------------
    if CoreX_Hook or isCoreX:

        patterns.append(
            (
                r'(\.method [^<]*<clinit>\(\)V\s+.locals \d+\n)',
                r'\1\tconst-string v0, "_Pairip_CoreX"\n\tinvoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V\n',
                f'CoreX_Hook ➸❥ {C.rkj}"lib_Pairip_CoreX.so"'
            )
        )

    Smali_Files = []
    for smali_folder in smali_folders:
        for root, _, files in C.os.walk(smali_folder):
            for file in files:
                if file in target_files:
                    Smali_Files.append(C.os.path.join(root, file))

    for pattern, replacement, description in patterns:
        for Smali_File in Smali_Files:
            try:
                if description.startswith("CoreX_Hook") and not Smali_File.endswith("VMRunner.smali"): continue

                content = open(Smali_File, 'r', encoding='utf-8', errors='ignore').read()
                new_content = C.re.sub(pattern, replacement, content)

                if new_content != content:
                    print(f"\n{C.lb}[ {C.c}Patch {C.lb}] {C.g}{description} {C.rkj}➸❥ {C.y}{C.os.path.basename(Smali_File)}")
                    print(f"{C.g}    |\n    └── {C.r}Pattern {C.g}➸❥ {C.pr}{pattern}")
                    open(Smali_File, 'w', encoding='utf-8', errors='ignore').write(new_content)

            except Exception as e:
                pass

    print(f"\n{C.r}{'_' * 61}\n")