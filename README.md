# **Task**

Build APIs with no frontend for a Bakery Management Application as follows:

Bakery Shop 
ADMIN should have the capability to:

Register and Login

Add Ingredients like Milk, Eggs etc

Create Product from list of ingredients

Get detail of Product (ingredients with quantity percentage, cost price, selling price etc)

Manage inventory

View monthly Profit/Sales report

Customer or buyer should have the capability to:

Register and Login

Get list of available products

Place order and get bill

See order history

Evaluation Criteria
Database schema

API structure

Code organisation and quality

Documentation (Tell us how to use your application and APIs - sharing POSTMAN collection is preferred)

Use of Git in development process (src code must be hosted on Github with meaningful commit messages, branch names etc)

Bonus
Include a test case in the application

Use Docker for app env setup

Host application on a cloud hosting platform like Heroku

Add feature for viewing popular or hot selling product (product with maximum sales)

Add feature for personalized ordering of product list for customer

Add feature to enable admins to add discounting rules

Tech Stack
Django (using Django Rest Framework for designing APIs is preferred)

Postgres / SQLite / MySQL

## **Tech Stack**
Django

PostgreSQL

RestFramework

## **PROJECT SETUP**

**Database Setup**

postgres=# CREATE USER bakeryadmin WITH PASSWORD 'bakeryadmin';
CREATE ROLE
postgres=# ALTER USER bakeryadmin CREATEDB;
ALTER ROLE

createdb bakerymanagement

**Project Interpreter**
Python 3.8

Using a virtual environment is recommended

**Install requirements**
pip3 install -r requirements.txt

**Django Setup**

In your project directory use the following commands

python3 manage.py migrate

python3 manage.py runserver

**API collections**

Postman collection link: https://www.getpostman.com/collections/3fcaeeb1194cfab42db8