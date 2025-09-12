# 🔐 Django Password Manager

A secure, user-authenticated password manager built with Django and PostgreSQL. Users can register, log in, store encrypted credentials, and view them on a personalized dashboard. Designed for simplicity, security, and extensibility.

---

## 🚀 Features

- 🔑 User registration with auto-login  
- 🔓 Custom password policy (no restrictions on length or complexity)  
- 🔐 AES-based credential encryption  
- 📋 Dashboard with decrypted password display  
- ➕ Add new credentials via secure form  
- 🔒 Logout flow with redirect to login/register  
- 🛠 Admin panel for superuser management

---

## 🧱 Tech Stack

| Layer         | Tool/Library         |
|--------------|----------------------|
| Backend      | Django (Python)      |
| Database     | PostgreSQL           |
| Encryption   | Custom AES logic     |
| Frontend     | Django templates     |
| Auth         | Django built-in auth |

---

## 📦 Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager

2. Create the virtual environment:
    python -m venv venv
    venv\Scripts\activate  # On Windows

3. Install dependencies:
   pip install -r requirements.txt

4. Configure PostgreSQL:
    Create a database and user
    Update settings.py with your DB credentials

5. Run Migrations:
  python manage.py migrate

6. Create Superuser (optional):
  python manage.py createsuperuser

7. Start the server:
   python manage.py runserver


🔐 Encryption Logic:
  Passwords are encrypted before saving using a custom AES-based utility:
  cred.password_encrypted = encrypt_password(form.cleaned_data['password_plain'])

Decryption happens on dashboard view:
  cred.decrypted_password = decrypt_password(cred.password_encrypted)

***Encryption keys are stored securely via environment variables.***



🧑‍💻 User Flow:

    Visit /vault/register/ → create account

    Auto-login → redirected to /vault/dashboard/

    Add credentials via /vault/addcredential/

    View decrypted credentials on dashboard

    Logout → redirected to login/register


📄 File Structure:
vault/
├── models.py
├── views.py
├── forms.py
├── utils.py
├── templates/
│   ├── vault/
│   │   ├── dashboard.html
│   │   └── addcredential.html
│   └── registration/
│       └── register.html




  
