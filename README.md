
# ☕ Smart Cafe Ordering System (Extended Version)

## 📌 Project Overview

The **Smart Cafe Ordering System** is a console-based Python application developed for the **Software Construction and Development Lab**.
This project simulates a semi-realistic cafe management system with support for customers, staff, dynamic menu handling, and order processing.

---

## 🎯 Objectives

* Apply Object-Oriented Programming (OOP) concepts
* Implement modular programming structure
* Practice file handling and exception handling
* Simulate real-world ordering and billing system

---

## 🚀 Features

### 🔹 Menu Management

* Add, remove, and update menu items
* Categorized menu (Drinks, Fast Food, Desserts)
* Dynamic loading from file

### 🔹 Order System

* Multiple items per order
* Quantity support
* Remove item from order
* Subtotal + Tax (5%) + Total calculation

### 🔹 Customer Features

* Unique Customer ID
* Multiple orders support
* Order history tracking

### 🔹 Staff/Admin Role

* Menu management functionality
* Implemented using inheritance

### 🔹 File Handling

* Save menu data in `menu.txt`
* Load menu on program start
* Basic data persistence

### 🔹 Billing System

* Formatted receipt generation
* Displays subtotal, tax, and total

### 🔹 Exception Handling

* Handles invalid input
* Prevents empty order checkout
* Handles file errors

### 🔹 Search & Filter

* Search items by name
* Filter items by category

---

## 🧱 OOP Concepts Used

* Classes and Objects
* Inheritance (Person → Customer, Staff)
* Composition (Order contains MenuItems)
* Encapsulation
* Modularity

---

## 📁 Project Structure

```
SmartCafe/
│
├── src/
│   ├── menu_item.py
│   ├── order.py
│   ├── person.py
│   ├── customer.py
│   ├── staff.py
│   ├── utils.py
│   └── main.py
│
├── data/
│   ├── menu.txt
│   └── orders.txt
│
├── README.md

```

---

## ▶️ How to Run

```bash
cd src
python main.py
```

---

## ⚙️ Requirements

* Python 3.x
* No external libraries required

---

## 📸 ScreenShots
## 1. Coding Structure
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/50747f6f-b34b-4d6b-935c-2fff8309e383" />

---

## 👨‍💻 Author

**Shujaat Ali**
Software Engineering – 5th Semester

---

## 📌 Final Note

This project demonstrates practical implementation of software development concepts including **OOP, modularity, file handling, and system design**, making it suitable for exam and viva evaluation.

                                                          ----Best Of Luck!----
