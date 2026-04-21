
# ☕ Smart Cafe Ordering System (Extended Version)

## 📌 Project Overview

The **Smart Cafe Ordering System** is a console-based Python application developed for the **Software Construction and Development Lab**.
This project simulates a semi-realistic cafe management system with support for customers, staff, dynamic menu handling, and order processing.

Including:

         Customers can place orders
         Staff can manage menu items
         Orders are processed with billing
         Data is stored using file handling
         

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

## 2. Making an Order
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/374f8069-0272-45dd-8159-473a56dab0fb" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/2fbee74e-c283-4d2c-96c1-3f431489d6f6" />
<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/afb1e5c3-367b-4f0a-b29f-6943e1c26f13" />

---

## 👨‍💻 Author

**Shujaat Ali**
Software Engineering – 5th Semester

---

## 📌 Final Note

This project demonstrates practical implementation of software development concepts including **OOP, modularity, file handling, and system design**, making it suitable for exam and viva evaluation.

                                                          ----Best Of Luck!----
