# Ecommerce POC for Sauer Websites

*** Setup Development on Linux Environment (Ubuntu) ***

** Run the following commands: **
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install libpq-dev
4. sudo apt-get install postgresql postgresql-contrib
5. sudo -i -u postgres
6. psql
7. CREATE DATABASE factory_pure_poc;
8. ALTER USER postgres WITH PASSWORD 'password found in .env';
9. pip install -r requirements.txt
10. From root directory: python -m venv venv
11. source venv/bin/activate
12. One directory level above root directory: sudo chmod -R 777 ecommerce-poc
13. python manage.py createsuperuser
14. python manage.py migrate
15. python manage.py (for all scripts that set up test data for all products (in the actual PostgreSQL db), stripe products, and stripe prices)
16. python manage.py runserver 0.0.0.0:8000
17. Find eth0 ip from command "ifconfig" then from host machine you can connect
