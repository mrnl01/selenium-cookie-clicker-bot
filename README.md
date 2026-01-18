# selenium-cookie-clicker-bot
# 🍪 Cookie Clicker Automation Bot (Selenium)

This project is a **basic automation bot for the Cookie Clicker game**, built using **Python and Selenium WebDriver**.  
The bot automatically clicks the main cookie and periodically purchases the most expensive affordable store item.

---

## 📌 Important Disclaimer

⚠️ **This project was created as part of an online course / tutorial.**  
It is **not an original idea**, and the core logic follows concepts taught during the course.

I have implemented, modified, and tested the code myself as a **learning exercise**.

---

## 🎯 Purpose of the Project

- To learn and practice **Selenium automation**
- To understand:
  - Explicit waits (`WebDriverWait`)
  - DOM element selection
  - Handling dynamic web pages
  - Basic automation logic & timing
- To get hands-on experience with **browser automation**

---

## ⚙️ What the Bot Does

- Opens Cookie Clicker in Microsoft Edge
- Selects **English** as the language
- Handles cookie consent (if present)
- Continuously clicks the main cookie
- Every 5 seconds:
  - Checks available store products
  - Buys the **most expensive affordable item**
- Automatically stops after **5 minutes**
- Prints the final cookie count

---

## 🐞 Known Limitations / Bugs

- The bot currently:
  - Buys **products only**, not upgrades
  - May break if the website UI changes
  - Uses basic error handling (`try/except`)
- There may be **minor bugs or edge cases** that are not fully handled

This project is **not production-ready** and is meant purely for learning.

---

## 🛠️ Tech Stack

- Python
- Selenium WebDriver
- Microsoft Edge
- WebDriverWait & Expected Conditions

---

## 🚀 How to Run

1. Install dependencies:
   ```bash
   pip install selenium
