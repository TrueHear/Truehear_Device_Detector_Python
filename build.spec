# PyInstaller Spec File
from PyInstaller.utils.hooks import collect_submodules

hidden_imports = collect_submodules("backend")
hidden_imports += collect_submodules("frontend")
hidden_imports += collect_submodules("utils")
hidden_imports += collect_submodules("zeroconf")  # <-- Add this line

a = Analysis(
    ["run.py"],
    pathex=["."],
    hiddenimports=hidden_imports,
    datas=[("backend/data/database.json", "backend")],
    binaries=[],
    noarchive=False,
)

pyz = PYZ(a.pure)
exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    name="TrueHearDeviceLister",
    debug=False,
    strip=False,
    upx=True,
    console=True,
)
