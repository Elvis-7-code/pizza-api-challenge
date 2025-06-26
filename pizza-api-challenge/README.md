# **Pizza Rest API Challenge







> ** A simple Flask API** for managing restaurants, pizzas and the relationship between them using **Flask**.[]

---

## **Requirements**
For this project, I was required to :
 
  -Create a Flask API backend.
  -Define at least three models and their relationships(`Restaurant`, `Pizza`, `Restaurantpizza`).
  -Set up migration and validation. 
  -Implement the required API routes.

  ---

  ## **Setup**

  ###**Pre-Requisites**###

  These are the requirements:
   -A working operating system: **(Windows 10+, Linux 3.8+ or MacOS x 10.7+)**
   -Python version: 3.12+
   -Pipenv
   -A Postman account(optional but recommended): [Download](https://www.postman.com)
   -RAM: **2GB minimum**, **4GB recommended**(for smother development)
   -Free Disk Space: **1GB minimum**, **2GB recommended**

  ---

  ##**Procedure**

  1. Cloning this repository:
     ```bash
     git clone https://github.com/Elvis-7-Code/pizza-api-challenge
     ```

     2. Navigate to the project directory:
     ``` bash
     cd restaurant_challenge
     ```

     3. Install dependencies:
     ``` bash
     pipenv install
     ```
     4. Activating the python environment:
     ```bash
     pipenv shell
     ```
     5.Run Migrations and Seed Data
     > - Run `flask db init` **only once**, and only if the `migrations/` folder does not already exist.
     ```bash
     flask db init
     flask db migrate -m "Initial"
     flask db upgrade
     python server/seed.py
     ```
     6. Start the server
       
       **Option 1 - Run directly with python:**
       ```bash
       python server/app.py
       ```
       **Option 2 - use `flask run`(recommended for development):**
       **Linux/macOS**
       ```bash
       export FLASK_APP=server/app.py
       export FLASK_ENV=development
       flask run 
       ``
       **Windows CMD**
       ```bash
       set FLASK_APP=server/app
       set FLASK_ENV=development
       flask run
       ```

       **Windows PowerShell**
       ```bash
       $env:FLASK_APP = "server/app.py"
       $env:FLASK_ENV = "development"
       flask run 
       ```
       The app will now be running at:
       ```bash
       https://127.0.0.1:5555
       ```

       ---

       ## **Project Structure**
       ```markdown
       ```

       ##**Tech Stack**
       -Python 3.12
       -Flask
       -SQlAlchemy
       -Flask-Migrate
       -Faker(for data seeding)
       SQLite(develoment DB)
       -Postman(testing)
       