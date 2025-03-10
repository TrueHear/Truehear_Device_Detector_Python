# PyInstaller Spec File
from PyInstaller.utils.hooks import collect_submodules

hidden_imports = collect_submodules("backend")
hidden_imports += collect_submodules("frontend")
hidden_imports += collect_submodules("utils")

a = Analysis(
    ["run.py"],  # Main entry point
    pathex=["."],
    hiddenimports=hidden_imports,
    datas=[("backend/data/database.json", "backend")],  # Ensure data.json is included
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
    console=True,  # Set to False if you don't want a console window
)
