# Ecommerce POC for Sauer Websites

***Setup Development on Linux Environment (Ubuntu)***

**Run the following commands:**
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install libpq-dev
4. sudo apt-get install postgresql postgresql-contrib
5. sudo -i -u postgres
6. psql
7. CREATE DATABASE factory_pure_poc;
8. ALTER USER postgres WITH PASSWORD 'password found in .env';
9. pip install -r requirements.txt
10. Place .env file under "ecommerce_poc/ecommerce_poc/.env"
11. Ensure you are on "main" branch
12. From root directory: python -m venv venv
13. source venv/bin/activate
14. One directory level above root directory: sudo chmod -R 777 ecommerce-poc
15. python manage.py createsuperuser
16. python manage.py migrate
17. python manage.py (for all scripts that set up test data for all products (in the actual PostgreSQL db), stripe products, and stripe prices)
18. python manage.py (add features, manuals and docs, overview, and specifications to existing products)
19. curl -s https://packages.stripe.dev/api/security/keypair/stripe-cli-gpg/public | gpg --dearmor | sudo tee /usr/share/keyrings/stripe.gpg
20. echo "deb [signed-by=/usr/share/keyrings/stripe.gpg] https://packages.stripe.dev/stripe-cli-debian-local stable main" | sudo tee -a /etc/apt/sources.list.d/stripe.list
21. sudo apt update
22. sudo apt install stripe
23. stripe login
24. stripe listen --forward-to http://localhost:8000/send_receipt/
25. python manage.py runserver 0.0.0.0:8000
26. Find eth0 ip from command "ifconfig" then from host machine you can connect

**oAuth Integration:**

1. Under: venv/lib/python3.10/site-packages/social_core/backends/auth0.py, you will need to remove the line: email: "payload["email"]" from the Auth0OAuth2 Class's return statement.

**TODO/TOADD:**
1. Full oAuth integration
2. SSO integration
3. Headless CMS
4. Kubernetes integration
5. Write Unit Tests
6. Write Integration Tests
7. Build out CICD Pipeline
8. Multiple service integration, where syncing between systems is needed
9. Modularize code, breaking down functions into smaller functions
10. Modularize project structure to have a Django application serve one purpose, i.e., an application for OAuth integration
