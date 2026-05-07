# 🏭 Abstract Factory Design Pattern (Python)

## 📌 Overview

This project demonstrates the **Abstract Factory Pattern**, used to create **families of related objects** without specifying their concrete classes.

---

## 📁 Project Structure

```bash
abstract_factory/
│
├── button.py
├── checkbox.py
├── factory.py
├── main.py
└── Abstract_Pattern.png  📊
```

**Visual Diagram:** See [ABSTRACT_FACTORY_DIAGRAM.md](./ABSTRACT_FACTORY_DIAGRAM.md) for UML class diagram (Mermaid - render in VSCode preview and export PNG).

---



## 🧠 Concept

### 🔹 What is Abstract Factory?

* A **Creational Design Pattern**
* Creates **related objects together**
* Ensures consistency across products

---

## ⚙️ Components

### 1. Product Interfaces

* `Button`
* `Checkbox`

---

### 2. Concrete Products

* WindowsButton, MacButton
* WindowsCheckbox, MacCheckbox

---

### 3. Abstract Factory

* `GUIFactory`
* Defines methods:

  * create_button()
  * create_checkbox()

---

### 4. Concrete Factories

* WindowsFactory
* MacFactory

---

## 🔄 Flow

1. Client selects factory (Windows/Mac)
2. Factory creates related objects
3. Client uses them without knowing classes

---

## ▶️ How to Run

```bash
python main.py
```

---

## 🧾 Output

```
Windows UI:
Render Windows Button
Render Windows Checkbox

Mac UI:
Render Mac Button
Render Mac Checkbox
```

---

## ✅ Advantages

* Ensures product consistency
* Loose coupling
* Easy to switch families

---

## ❌ Disadvantages

* More classes → more complexity
* Hard to extend new product types

---

## 🔥 Real-World Examples

* UI frameworks (Windows/Mac themes)
* Cross-platform apps
* Game engines (different environments)

---

## 🎯 Key Takeaway

> **Abstract Factory = "Create families of related objects together"**

---

## 👨‍💻 Author

Priyangshu

---

## ⭐ Keep building

Design patterns → clean architecture 🚀

---

## 🆚 Factory Pattern vs Abstract Factory Pattern

| Feature                | Factory Pattern                             | Abstract Factory Pattern                           |
|------------------------|---------------------------------------------|----------------------------------------------------|
| **Purpose**            | Creates **one type** of object              | Creates **families of related** objects            |
| **Number of products** | Single product                              | Multiple related products                          |
| **Method count**       | One factory method                          | Multiple factory methods                           |
| **Complexity**         | Simpler                                     | More complex                                       |
| **Use case**           | One object, subclass decides the type       | Consistent sets of related objects together        |
| **Example**            | `ShapeFactory.create("circle")`             | `GUIFactory.create_button()` + `create_checkbox()` |

### 🔑 In Short

> **Factory Pattern** → *"Create one object, let subclasses decide which class."*
>
> **Abstract Factory Pattern** → *"Create a whole family of related objects that work together."*

Use **Factory** when you have a single product hierarchy.
Use **Abstract Factory** when your products come in **groups/families** that must stay consistent (e.g., Windows UI components should always look Windows-like together).
