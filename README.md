# 📬 Bulk Email Sender using Python

This Python project allows users to send emails to **multiple recipients** efficiently through an SMTP server. It leverages Python's built-in `smtplib` and `email` libraries to handle authentication and message composition.

---

## 🚀 Features

- Send a single email to **multiple recipients**
- Securely login using your email and password
- Easily customize subject and body content
- Works with any SMTP-enabled email provider (e.g., Gmail)

---

## 🧰 Technologies Used

- `smtplib`: For connecting to the SMTP server and sending mail


---

## 📝 How It Works

1. The user provides their email and password (preferably app password for security).
2. A list of recipient email addresses is maintained in the code.
3. The script sends a single email to **all recipients** in one go.


Replace the sender's email and password in:

ob.login("your_email@example.com", "your_password")


