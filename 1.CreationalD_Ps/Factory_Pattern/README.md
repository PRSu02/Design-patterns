# 🚗 Vehicle Factory Design Pattern (Python)

## 📌 Overview

This project demonstrates the **Factory Design Pattern** using a simple **Vehicle example (Car & Bike)**.

The factory pattern helps in **creating objects without exposing the creation logic** to the client.

---

## 📁 Project Structure

```
vehicle_factory/
│
├── vehicle.py        # Abstract base class
├── car.py            # Car implementation
├── bike.py           # Bike implementation
├── factory.py        # Factory class
└── main.py           # Client code
```

---

## 🧠 Concept

### 🔹 What is Factory Pattern?

* A **Creational Design Pattern**
* Creates objects **based on input**
* Hides object creation logic from client

👉 Instead of:

```
Car()
Bike()
```

👉 We use:

```
VehicleFactory.get_vehicle("car")
```

---

## ⚙️ Components

### 1. `Vehicle` (Abstract Class)

* Defines a common interface
* Contains abstract method `drive()`

---

### 2. `Car` and `Bike` (Concrete Classes)

* Implement `Vehicle`
* Provide their own `drive()` behavior

---

### 3. `VehicleFactory`

* Decides which object to create
* Centralized object creation logic

---

### 4. `Client (main.py)`

* Calls factory
* Uses object without knowing its creation logic

---

## 🔄 Flow

1. Client requests object → `"car"`
2. Factory processes request
3. Factory returns `Car()` object
4. Client calls `drive()`

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧾 Sample Output

```
Driving a Car 🚗
Riding a Bike 🏍️
```

---

## ✅ Advantages

* Loose coupling
* Clean code
* Easy to extend
* Centralized object creation

---

## ❌ Without Factory (Problem)

```python
if type == "car":
    vehicle = Car()
elif type == "bike":
    vehicle = Bike()
```

👉 Problems:

* Repeated logic
* Hard to maintain
* Not scalable

---

## ➕ Adding New Vehicle (e.g., Truck)

Steps:

1. Create `truck.py`
2. Add condition in factory:

```python
elif vehicle_type == "truck":
    return Truck()
```

👉 No change in client code ✅

---

## 🎯 Key Takeaway

> **Factory Pattern = "Give input → Get object (without knowing how it's created)"**

---

## 💡 Real-World Use Cases

* Payment systems (UPI / Card / Wallet)
* Notification systems (Email / SMS / Push)
* Logging frameworks
* Database connections

---

## 👨‍💻 Author

Priyangshu

---

## ⭐ If you like this project

Give it a ⭐ and keep building 🚀
