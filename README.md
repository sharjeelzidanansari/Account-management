# Account-management

# 🚀 Sharjeel's Terminal-Based Python Banking System

A complete beginner-friendly Python project simulating a secure banking system through terminal interface. The application allows users to **login using a PIN**, **deposit or withdraw money**, and **check their account balance**, all stored securely using a JSON file.

---

## 📁 Project Folder Name

 
---

## 💡 Features

- 🔐 **PIN-based login system** with limited attempts
- 💰 **Deposit** functionality with input validation
- 🏧 **Withdraw** with balance checks and confirmation
- 📊 **Balance Checker** showing current stored amount
- 📁 **Persistent Data Storage** using `balance.json`
- 📦 **Modular Python Code** for cleaner structure

---

## 🛠 Tech Stack

| Component         | Technology Used     |
|------------------|----------------------|
| Language          | Python 3.x           |
| Storage           | JSON file            |
| Interface         | CLI (Command Line)   |
| Dependencies      | No external libraries |
| Platform          | Cross-platform       |

---

## ⚙️ How to Setup & Run

### 🔽 Step-by-Step:

```bash
# Step 1: Clone this repository
git clone https://github.com/your-username/sharjeel.git
cd sharjeel

# Step 2: (Optional) Create a virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Step 3: Make sure balance.json is initialized
echo '{"balance": 5000}' > balance.json

# Step 4: Run the project
python main.py
