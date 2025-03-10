# **TrueHear Device Lister**  

*A High-Performance Network Audio Device Discovery Tool*  

<!-- ![TrueHear Logo](https://yourlogo.com/logo.png) *(Replace with actual logo URL)*   -->

---

## **📌 Overview**  

The **TrueHear Device Lister** is an advanced **network audio device discovery tool** that scans for **output devices** over the local network using the **Zeroconf/mDNS protocol**. Built with **Flask (Backend)** and **PyQt (Frontend)**, it provides a **real-time, user-friendly interface** for listing available devices.

🔹 **Industry-grade audio device detection**  
🔹 **Asynchronous scanning with non-blocking UI**  
🔹 **Custom service name input for flexible discovery**  
🔹 **Seamless Flask-PyQt integration**  
🔹 **Automatic server shutdown upon exit**  

---

## **🛠️ Features**  

### ✅ **Fast & Reliable Network Device Scanning**  

- Uses **Zeroconf/mDNS** to detect devices in real-time.  
- Supports **custom service name input** for greater flexibility.  
- Defaults to `_smart_ip._tcp.local.` if no service name is provided.  

### ✅ **Modern, User-Friendly UI**  

- Clean and minimal **PyQt-based UI**.  
- **Threaded scanning** ensures smooth, non-blocking interaction.  
- Displays a **scanning message** while searching for devices.  
- Provides **detailed device information** including:
  - Service Name  
  - IP Addresses  
  - Port Number  
  - Device Properties  

### ✅ **Seamless Flask Backend Integration**  

- Runs a **Flask API** in the background.  
- **Automatic Flask shutdown** when the app is closed.  
- Uses **multiprocessing** to ensure a **responsive application**.  

### ✅ **Robust Logging & Error Handling**  

- Uses **industry-standard logging practices** to track errors.  
- **Gracefully handles** network issues and invalid service names.  

---

## **📂 Project Structure**  

```bash
truehear-device-lister/
│── backend/             # Flask Backend (API)
│   ├── __init__.py      # Flask app initialization
│   ├── routes.py        # API Routes
│   ├── server.py        # Server entry point
│── frontend/            # PyQt UI Application
│   ├── ui_components.py # UI elements (modular)
│   ├── main_window.py   # UI logic
│── utils/               # Utility Functions
│   ├── logger.py        # Logging utility
│   ├── device_scanner.py # Zeroconf device scanner
│── main.py              # Application entry point
│── requirements.txt     # Dependencies
│── README.md            # Documentation
```

---

## **🚀 Installation & Setup**

### **🔹 Prerequisites**

- Python **3.8+**
- `pip` (Python package manager)

### **🔹 Step 1: Clone the Repository**

```bash
git clone https://github.com/your-org/truehear-device-lister.git
cd truehear-device-lister
```

### **🔹 Step 2: Install Dependencies**

```bash
pip install -r requirements.txt
```

### **🔹 Step 3: Run the Application**

```bash
python main.py
```

This will:
✅ Start the **Flask API** in the background.  
✅ Launch the **PyQt UI**.  
✅ Scan and display **available output devices**.  

---

## **🔧 Usage**

1️⃣ **Launch the application** using `python main.py`.  
2️⃣ **Enter a service name** (optional) or leave it blank to use `_smart_ip._tcp.local.`.  
3️⃣ Click **"Get Output Devices"** to start scanning.  
4️⃣ Wait for the scanning process to complete.  
5️⃣ View the **list of discovered devices** along with their details.  

💡 **Tip:** If no devices are found, ensure that the devices are **on the same network** and support **Zeroconf/mDNS discovery**.

---

## **🛠️ Configuration**

Modify the **default service name** in `device_scanner.py`:

```python
DEFAULT_SERVICE = "_smart_ip._tcp.local."
```

or set it dynamically via the **UI input field**.

---

## **📖 API Endpoints**

The Flask API provides network-scanning functionality:

### 🔹 **`GET /scan`**  

**Description:** Scans for available output devices over the network.  
**Response Format:**

```json
{
    "devices": [
        {
            "service_name": "Speaker-123",
            "ip": "192.168.1.10",
            "port": 8080,
            "properties": {
                "model": "TrueHear Pro",
                "version": "2.1"
            }
        }
    ]
}
```

---

## **🛡️ Security & Error Handling**

✅ **Prevents crashes** with `try-except` blocks.  
✅ **Fails gracefully** if **Zeroconf is not available** or **network issues occur**.  
✅ **Logs all events** to `app.log` for debugging.  

---

## **🔍 Troubleshooting**

### ❌ **Flask Server Doesn’t Start**

🔹 **Check if another process is using port 5000:**  

```bash
netstat -an | grep 5000  # For Linux/Mac
netstat -ano | findstr :5000  # For Windows
```

🔹 If port 5000 is busy, **change the port** in `server.py`:

```python
app.run(port=5050)
```

### ❌ **No Devices Found**

✔️ Ensure devices **support Zeroconf/mDNS discovery**.  
✔️ Try using a **different service name**.  
✔️ Check **firewall settings** on your machine.  

---

## **📜 License**

© 2024 **TrueHear Inc.** – All rights reserved.  
Distributed under the **MIT License**.

---

## **🧑‍💻 Contributors**

- **Sameer Karn** – Lead Developer  
- **TrueHear Team** – Backend & UI Development  

Want to contribute? Fork the repo and submit a **Pull Request**! 🚀  

---

## **📞 Contact & Support**

📧 **Support:** <truehearteam@gmail.com>  
<!-- 🌐 **Website:** [www.truehear.com](https://www.truehear.com)  
🐦 **Twitter:** [@TrueHear](https://twitter.com/TrueHear)   -->

---

### **🚀 Ready to Scan Your Devices?**

Run:

```bash
python main.py
```

🎧 **Discover TrueHear-compatible devices today!** 🚀
