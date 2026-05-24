# ☕ Smart Cafe Ordering System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![OOP](https://img.shields.io/badge/OOP-Based-success?style=for-the-badge)
![Console App](https://img.shields.io/badge/Console-Application-orange?style=for-the-badge)
![File Handling](https://img.shields.io/badge/File-Handling-red?style=for-the-badge)

A complete **Python-based Smart Cafe Management System** developed using **Object-Oriented Programming (OOP)** concepts with advanced features such as billing, menu management, file handling, loyalty points, student discounts, and admin authentication.

</div>

---

# 📌 Project Overview

The **Smart Cafe Ordering System** is a console-based application designed to simulate a semi-realistic cafe management environment.

The system allows:
- Customers to browse menu items
- Place and manage orders
- Generate billing receipts
- Apply discounts
- Earn loyalty points

Additionally, the system provides:
- Admin panel for menu management
- File handling for data persistence
- Search and filter functionalities
- Exception handling for system robustness

This project demonstrates practical implementation of:
- Object-Oriented Programming
- Inheritance
- Composition
- File Handling
- Exception Handling
- Dynamic Data Management

---

# 🎯 Objectives

The main objectives of this project are:

- Implement Object-Oriented Programming concepts
- Create a modular and scalable application
- Simulate a real-world cafe ordering system
- Manage menu items dynamically
- Handle customer orders efficiently
- Store and retrieve data using files
- Improve user experience using interactive console UI

---

# 🚀 Features

# 👤 Customer Features

## ✅ View Dynamic Menu
Customers can view all available menu items with:
- Name
- Price
- Category
- Stock Availability

---

## ✅ Search Menu Items
Customers can search menu items using partial keywords.

### Example:
```txt
Input: bur
Output: Burger
```

---

## ✅ Filter by Category
Menu items can be filtered based on categories such as:
- Fast Food
- Drinks
- Desserts

---

## ✅ Add Items to Order
Customers can:
- Select menu items
- Enter quantity
- Add multiple items to cart

---

## ✅ Remove Items from Order
Customers can remove unwanted items before checkout.

---

## ✅ Billing System
The system automatically calculates:
- Subtotal
- Tax (5%)
- Final Total

### Formula Used

Total Calculation:

```math
Total = Subtotal + (0.05 × Subtotal)
```

---

## ✅ Student Discount System ⭐
Customers can receive a **10% student discount** during checkout.

### Discount Formula

```math
Discount = 0.10 × Total
```

---

## ✅ Loyalty Points System ⭐
Customers earn loyalty points based on their purchases.

### Rules:
- Every Rs.100 spent = 1 loyalty point

This feature simulates real-world customer reward systems.

---

## ✅ Receipt Generation
A detailed receipt is displayed after checkout including:
- Ordered Items
- Quantity
- Tax
- Discount
- Final Total

---

# 🔐 Admin Features

## ✅ Admin Login Authentication
The system includes a secure admin login system.

### Default Credentials

```txt
Username: admin
Password: 1234
```

---

## ✅ Add Menu Items
Admins can dynamically add new menu items.

### Example:
```txt
Name: Pizza
Price: 1200
Category: Fast Food
Stock: 10
```

---

## ✅ Remove Menu Items
Admins can remove existing items from the menu.

---

## ✅ View Updated Menu
Admins can view all updated menu items instantly.

---

# 💾 File Handling Features

## ✅ Menu Persistence
The menu is automatically stored in:

```txt
menu.txt
```

This ensures data remains saved even after restarting the program.

---

## ✅ Order Receipt Storage
All order receipts are stored in:

```txt
orders.txt
```

This helps maintain customer order records.

---

# ⚠️ Exception Handling

The project includes proper exception handling to prevent crashes.

Handled exceptions include:
- Empty order checkout
- Invalid menu selection
- Stock overflow
- File access errors
- Invalid user input

### Example

```python
raise Exception("Order is empty!")
```

---

# 🧠 OOP Concepts Implemented

| Concept | Description |
|---|---|
| Classes & Objects | Used for system entities |
| Inheritance | Customer & Staff inherit Person |
| Encapsulation | Data organized inside classes |
| Composition | Order contains MenuItems |
| Abstraction | Functions simplify complex operations |

---

# 🏗 Project Structure

```txt
SmartCafe/
│
├── main.py
├── README.md

---


## 🛠 Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main Programming Language |
| OOP | System Design |
| File Handling | Data Persistence |
| Exception Handling | Error Management |

---


## 📷 Sample Console Output

```txt
========== SMART CAFE SYSTEM ==========

1. View Menu
2. Search Item
3. Filter Category
4. Add Item to Order
5. Remove Item from Order
6. Checkout
7. Customer Details
8. Admin Panel
9. Exit
```

---

# 📋 Example Receipt

```txt
========== SMART CAFE ==========

Burger x2 = Rs.1000
Coffee x1 = Rs.300

-------------------------------
Subtotal: Rs.1300
Tax (5%): Rs.65
Student Discount: Rs.136.5
-------------------------------
Final Total: Rs.1228.5

Earned Loyalty Points: 12
================================
```

---

# 🔍 Search Feature Example

```txt
Enter item name: piz
```

### Output

```txt
Pizza | Rs.1200 | Fast Food | Stock: 5
```

---

# 🎨 Additional Premium Features

The project also includes several enhanced features:

✅ Student Discount System  
✅ Loyalty Points System  
✅ Admin Authentication  
✅ Dynamic Menu Management  
✅ File-Based Storage  
✅ Search & Filter System  
✅ Loading Animation  
✅ Stock Management  
✅ Receipt Saving System  

---

# 🚀 Future Improvements

The system can be upgraded further with:

- GUI Interface (Tkinter / PyQt)
- Database Integration (MySQL)
- Online Payment Gateway
- QR Ordering System
- Table Reservation System
- Delivery Tracking
- Mobile Application Version
- Cloud Database Support

---

# 🧪 How to Run

## Step 1
Install Python 3.x

---

## Step 2
Clone Repository

```bash
git clone https://github.com/yourusername/Smart

---

## Step 3
Run Program

```bash
python main.py
```

---

# 📚 Learning Outcomes

This project helps understand:
- Real-world OOP implementation
- Dynamic data structures
- File management in Python
- Error handling techniques
- Console-based application development


---

# 👨‍💻 Developed By

## Shujaat Ali

Software Engineering Student  
Python Developer | OOP Enthusiast

---

# 📄 License

This project is developed for educational purposes.

---

# ⭐ Support

If you like this project, give it a ⭐ on GitHub.
