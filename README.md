# Hiyab's Cafe App 

<img width="1536" height="1024" alt="hiyab" src="https://github.com/user-attachments/assets/1333c042-61fb-4188-95ff-fb774a029eff" />

# Project Background 

This projects is done as part of my assignment as a Generation Data engineer trainee. It is a fully fuctioning command-line interface (CLI) application for a fictious pop up cafe built using python. User data entries are persisted, and error handling was implemented to prevent data loss and ensure user input is validated, thereby, improivng user experience.

# Client Requirement

The following are the core features based on client requirement.

User must be able to 
- view, create, update or delete a product, courier, order, customer dictionary.

- view orders by status.

- load and save user data entries persistently to a database

Progress made each week to build client's MVP (Minimum Viable Product) and finally, the end product in week 6.

<a href="https://github.com/hiyab-t/hiyab-mini-project/tree/91f6cc25cd68b275dd222d0358ea72c3c5f99b15/mini_project/week_1">week_1</a>

- User is able to view, create, update and delete products.

<a href="https://github.com/hiyab-t/hiyab-mini-project/tree/91f6cc25cd68b275dd222d0358ea72c3c5f99b15/mini_project/week_2">week_2</a>

- User is able to view, create, update and delete products and orders.

<a href="https://github.com/hiyab-t/hiyab-mini-project/tree/91f6cc25cd68b275dd222d0358ea72c3c5f99b15/mini_project/week_3">week_3</a>

- User is able to view, create, update and delete products, orders, and couriers.
- User data entries are persisted to a .txt file format.

<a href="https://github.com/hiyab-t/hiyab-mini-project/tree/91f6cc25cd68b275dd222d0358ea72c3c5f99b15/mini_project/week_4">week_4</a>

- User is able to view, create, update and delete products, orders and couriers dictionary.
- User data entries are persisted to a .csv file format.

<a href="https://github.com/hiyab-t/hiyab-mini-project/tree/91f6cc25cd68b275dd222d0358ea72c3c5f99b15/mini_project/week_5">week_5</a>

- User is able to view, create, update and delete products, orders and couriers dictionary. 
- User data entries for products and couriers are persisted to database.
- User data entries for orders is persisted to .csv format.

<a href="https://github.com/hiyab-t/hiyab-mini-project/tree/91f6cc25cd68b275dd222d0358ea72c3c5f99b15/mini_project/week_6">week_6</a>

- User is able to view, create, update and delete products, orders and couriers dictionary.
- User data entries for products, orders and couriers are persisted to database.


# How to Run the App

1. **Clone the Repository**
```bash
   git clone https://github.com/hiyab-t/hiyab-mini-project.git
   cd hiyab-mini-project
```

2. **Set Up a Virtual Environment**

python3 -m venv .venv       # On macOS/Linux
py -m venv .venv            # On Windows
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows

3. **Install Dependencies**

pip install -r requrements.txt

4. **Start Postgres with Docker**
```bash
    docker compose up -d
```
This will start:
- postres (database container)
- adminer (a web-based database client at http://localhost:8080)

Note: you will need to download and open docker desktop.

5. **Run the App**

```bash
    python3 -m week_<week number>.source.app<week number> #On macOS/Linux 
    py -m week_<week number>.source.app<week number> #On Windows
    
    #ie. python3 -m week_4.source.app4
```
# How to run any unit tests
```bash
    pytest -v
```

# Reflections




