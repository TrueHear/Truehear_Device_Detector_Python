# **🚀 Building TrueHear Device Lister App (PyQt + Flask)**

## **📌 Steps to Build the App**

1️⃣ **Use `PyInstaller` to package the app**  
2️⃣ **Ensure Flask server runs correctly when the app starts**  
3️⃣ **Handle dependencies properly**  
4️⃣ **Generate a Windows `.exe` or Mac/Linux binary**  

---

## **1️⃣ Install Required Dependencies**

Before building, ensure all dependencies are installed:

```bash
pip install pyinstaller requests flask pyqt5 zeroconf
```

---

## **2️⃣ Prepare a Build Script**

To ensure both **Flask and PyQt UI** work properly in the packaged app, create a script that:
✅ **Starts the Flask server**  
✅ **Launches the PyQt UI**  
✅ **Closes Flask when the app exits**  

### **🔹 Create `run.py` (Main Entry Point)**

📍 This script **ensures Flask starts in the background** when the app runs.

```python
import sys
import atexit
from multiprocessing import Process
from backend.server import app  # Flask server
from frontend.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from utils.logger import setup_logger

logger = setup_logger()
server_process = None  # Global variable for Flask process

def run_server():
    """Runs Flask server in a separate process"""
    try:
        logger.info("Starting Flask Server Process...")
        app.run(port=5000, debug=False)
    except Exception as e:
        logger.critical(f"Flask Server Crashed: {e}")

def stop_server():
    """Stops Flask server process when app exits"""
    global server_process
    if server_process and server_process.is_alive():
        logger.info("Stopping Flask Server...")
        server_process.terminate()
        server_process.join()
        logger.info("Flask Server Stopped.")

if __name__ == "__main__":
    try:
        server_process = Process(target=run_server)
        server_process.start()
        atexit.register(stop_server)  # Ensure Flask stops on exit

        logger.info("Launching PyQt UI...")
        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        sys.exit(app.exec_())

    except Exception as e:
        logger.critical(f"Application Crashed: {e}")
        stop_server()
```

✅ **Flask starts in a separate process**  
✅ **Stops Flask when the app closes**  

---

## **3️⃣ Create a `PyInstaller` Build File**

📍 We will create a `spec` file for `PyInstaller`, ensuring everything is bundled correctly.

### **🔹 Create `build.spec`**

📌 Save this file as `build.spec` in the root project folder.

```python
# PyInstaller Spec File
from PyInstaller.utils.hooks import collect_submodules

hidden_imports = collect_submodules("backend")
hidden_imports += collect_submodules("frontend")
hidden_imports += collect_submodules("utils")

a = Analysis(
    ["run.py"],  # Main entry point
    pathex=["."],
    hiddenimports=hidden_imports,
    datas=[("backend/database.json", "backend")],  # Ensure data.json is included
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
```

✅ **Ensures backend & frontend modules are included**  
✅ **Includes `data.json` in the build**  
✅ **Creates an executable with everything bundled**  

---

## **4️⃣ Build the App Using `PyInstaller`**

📍 Run the following command to build the standalone `.exe` or binary:

```bash
pyinstaller --clean --noconfirm build.spec
```

This will generate:

- **On Windows:** `dist/TrueHearDeviceLister/TrueHearDeviceLister.exe`
- **On macOS/Linux:** `dist/TrueHearDeviceLister/TrueHearDeviceLister`

✅ **A single folder with everything included!**  

---

## **5️⃣ Test the Built Application**

After the build completes:

- Navigate to `dist/TrueHearDeviceLister/`
- Run the executable:

  ```bash
  ./TrueHearDeviceLister  # (Linux/Mac)
  TrueHearDeviceLister.exe  # (Windows)
  ```

---

## **🎯 Final Build Folder Structure**

```bash
dist/
└── TrueHearDeviceLister/
    ├── TrueHearDeviceLister.exe  # Executable file (Windows)
    ├── backend/
    │   ├── database.json  # Data persistence
    │   ├── server.py
    ├── frontend/
    │   ├── main_window.py
    ├── utils/
    │   ├── logger.py
```

---

## **🎯 Next Steps**

🔹 **Want a single `.exe` file instead of a folder?** Use:

```bash
pyinstaller --onefile build.spec
```

🔹 **Want an installer?** Use `NSIS` or `Inno Setup` to create a Windows installer.

---

### **🚀 Now Your TrueHear Device Lister is Fully Built & Ready to Distribute!**

Would you like to **add an auto-updater or deploy this on multiple systems?** 🚀
