# 🏁 Formula 1 Race Ticket Booking System

A seamless, interactive web application built with Python and Streamlit that simulates an online ticket reservation platform for F1 Grand Prix races. Users can browse events, search for specific races, manage their shopping cart, calculate totals with discounts, and securely check out.

This project was developed as part of the **Week 1: Fundamentals Application** assignment.

---

## 🚀 Live Demo
You can access the live application here: 
🔗 [[I(https://shiny-space-waffle-r5jj5wjx7p9fwq44-8501.app.github.dev/#available-races-schedule)]

---

## ✨ Features & Team Contributions

Our team divided the workflow into 4 distinct roles to build a cohesive and functional application:

### 👤 Person 1: Database & Search (Browse & Search)
* **Responsibilities:** Built the core data architecture and search functionality.
* **Key Implementation:** * Designed a nested dictionary (`dict`) to store comprehensive event data (Race Name, Price, Location, Date, Time, and Available Seats).
  * Implemented `st.text_input()` to allow users to dynamically filter and search for races by city/name.

### 👤 Person 2: Cart Management (Cart & Quantity Control)
* **Responsibilities:** Developed the logic for handling interactive user selections.
* **Key Implementation:**
  * Utilized `st.session_state` to ensure the shopping cart persists across Streamlit page rerenders.
  * Integrated `st.number_input()` to allow users to modify ticket quantities (defaulting to 1) and added buttons to dynamically add or remove tickets from the cart.

### 👤 Person 3: Calculations & Discounts (Financial Engine)
* **Responsibilities:** Created the calculation engine for sub-totals and final bills.
* **Key Implementation:**
  * Wrote a custom function `calculate_total()` that maps cart items against the event database prices.
  * Integrated a `lambda` function to instantly apply promotional discount codes and compute the final VAT/tax additions.

### 👤 Person 4: Checkout & Confirmation (UI/UX & Finalization)
* **Responsibilities:** Structured the user journey finalization and receipt generation.
* **Key Implementation:**
  * Created the "Confirm Reservation" triggers using `st.button()`.
  * Utilized `st.success()` to deliver an interactive confirmation toast.
  * Formatted a clean receipt summary using `st.write()` and data layouts to display the final invoice.

---

## 🛠️ Programming Concepts Applied

To meet the project criteria, this application successfully integrates:
* **Data Types & Collections:** `str`, `int`, `float`, `bool`, along with a complex **Nested Dictionary** and **Lists**.
* **Control Flow:** Advanced `if / elif / else` conditional statements for search filtering and stock validation.
* **Loops:** `for` and `while` loops to render dynamic UI components and iterate through cart operations.
* **Functions:** Clean, custom functions with parameters and explicit `return` values alongside a functional `lambda` expression.
* **Interactive UI:** Native Streamlit inputs (`st.text_input`, `st.number_input`, `st.button`) for seamless user interactivity.

---

   Group Members
Person 1: [Rahaf Makhdoom  / GitHub [https://github.com/Rahafmak]]

Person 2: [Rana Aljuaid / GitHub [https://github.com/ranatsa9/] ] 

Person 3: [Maram Alzahrani / GitHub[https://github.com/Maramjamaan]]

Person 4: [Noura Alshowair  / GitHub [https://github.com/Noura-1237]]