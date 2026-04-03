# 🔒 Singleton Design Pattern (Python)

## 📌 Overview

This project demonstrates the **Singleton Design Pattern**, ensuring that a class has **only one instance** and provides a global access point.

---

## 📁 Project Structure

```
singleton_example/
│
├── singleton.py     # Core singleton logic
├── logger.py        # Example implementation
└── main.py          # Client code
```

---

## 🧠 Concept

### 🔹 What is Singleton Pattern?

* A **Creational Design Pattern**
* Ensures **only one object exists**
* Provides **global access**

---

## ⚙️ How It Works

* Uses a class variable `_instance`
* Overrides `__new__()` method
* Creates object only once
* Returns same instance always

---

## 🔄 Flow

1. First call → creates object
2. Next calls → return same object
3. All variables share same state

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧾 Output

```
Creating new instance...
LOG: First message
LOG: Second message
True
```

---

## ✅ Advantages

* Controlled access to instance
* Saves memory
* Avoids duplicate objects

---

## ❌ Disadvantages

* Hard to test (global state)
* Can hide dependencies
* Not thread-safe (basic version)

---

## 🔥 Real-World Examples

* Logger system
* Database connection
* Configuration manager
* Cache system

---

## 🎯 Key Takeaway

> **Singleton = "Only one object exists in the entire application."**

---

## 👨‍💻 Author

Priyangshu

---

## ⭐ Keep building

Small patterns → Big systems 🚀
