🔐 Django Password Manager

A secure, user-authenticated password manager built with Django and PostgreSQL. Users can register, log in, store encrypted credentials, and view them on a personalized dashboard. Designed for simplicity, security, and extensibility.
🚀 Features

   🔑 User registration with auto-login

   🔓 Custom password policy (no restrictions on length or complexity)

   🔐 AES-based credential encryption

   📋 Dashboard with decrypted password display

   ➕ Add new credentials via secure form

   🔒 Logout flow with redirect to login/register

   🛠 Admin panel for superuser management



🧱 Tech Stack
Layer	Tool/Library
Backend	Django (Python)
Database	PostgreSQL
Encryption	AES + Fernet
Frontend	Django templates
Auth	Django built-in auth
📦 Installation Guide
🐍 1. Install Python



1. Download Python 3.10+ from python.org/downloads
   ✅ During installation, check “Add Python to PATH”

   Verify installation:
   python --version
   pip --version
   
   If PATH isn’t set properly, manually add:
   C:\Users\vbox\AppData\Local\Programs\Python\Python310\
   C:\Users\vbox\AppData\Local\Programs\Python\Python310\Scripts\

*** Add Python to your PATH envrironment variable!  Google it! ***



🧰 2. Install Git

   Download Git from git-scm.com
   Accept defaults during installation

   Verify:
   git --version
   
   Set your identity:
   git config --global user.name "Your Name"
   git config --global user.email "your-email@example.com"



📁 3. Clone the Repository
   git clone https://github.com/mickeymouseandgoofey/password_manager.git
   cd password_manager



🧪 4. Set Up Virtual Environment
   python -m venv venv
   venv\Scripts\activate  # On Windows


📦 5. Install Dependencies (within venv):
   pip install -r requirements.txt


🗄️ 6. Install PostgreSQL:
This project uses PostgreSQL as its database backend.
✅ Steps:

   Download from postgresql.org/downloads
   During setup:

   Set a password for the postgres superuser
   Leave port as 5432
   Install pgAdmin (optional)
   Verify PostgreSQL is running via services.msc

*** Note - you should find the location of the installation (usually C: programs\postrgress) and find the BIN folder.  Copy that file path and add to your PATH evnronment variable!  (Google it!)

🛠 Create DB and User

In pgAdmin or psql, type the commands:
   mysql -u root -p

   CREATE DATABASE 'your_custom_db_name';
   
   CREATE USER 'your_postgres_user WITH PASSWORD' 'your_postgres_password';
   
   GRANT ALL PRIVILEGES ON DATABASE 'your_custom_db_name' TO 'your_postgres_user';
   
   GRANT ALL ON SCHEMA public TO 'your_postgres_user';
   
   ALTER DATABASE 'your_db_name' OWNER TO 'your_postgres_user';
   
   ALTER SCHEMA public OWNER TO 'your_postgres_user';
   
   GRANT USAGE, CREATE ON SCHEMA public TO 'your_postgres_user';



🔐 7. Set Environment Variables

Create a .env file in the project root (same directory you find manage.py):
Open up notepad++ or your favorite text editor.  Copy and past the following with customized keys/names/passwords. Name the file .env (no extension).
   SECRET_KEY=your-django-secret-key
   FERNET_KEY=your-generated-fernet-key
   DB_NAME=same as in step 6.
   DB_USER=same as in step 6. 
   DB_PASSWORD=same as in step 6. 
   DB_HOST=localhost
   DB_PORT=5432


To generate a Secret key:
Type pyton in your command prompt and paste the following:
   from django.core.management.utils import get_random_secret_key
   print(get_random_secret_key())
**Copy the output and paste it into your .env file:


To generate a Fernet key:
Type python in your command prompt and paste the following:
   from cryptography.fernet import Fernet
   print(Fernet.generate_key().decode())
**Copy the output and paste it into your .env file:




⚙️ 8. Run Migrations
python manage.py migrate

** if it doesn't work, go back to step 6 and ask copilot for help :)



👤 9. Create Superuser (Optional)
python manage.py createsuperuser



🚀 10. Start the Server
python manage.py runserver



🔐 Encryption Logic

Passwords are encrypted before saving using a custom AES-based utility:
   cred.password_encrypted = encrypt_password(form.cleaned_data['password_plain'])

*Decryption happens on dashboard view:*

   cred.decrypted_password = decrypt_password(cred.password_encrypted)




🧑‍💻 User Flow

   Visit /vault/register/ → create account

   Auto-login → redirected to /vault/dashboard/

   Add credentials via /vault/addcredential/

   View decrypted credentials on dashboard

   Logout → redirected to login/register


   

📂 File Structure
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

