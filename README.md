# Plant_care_tracker
Team project for CFGdegree - Software Engineering (summer 2023)


╋╋╋┏┓╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋╋╋╋╋╋╋┏┓╋╋╋╋╋╋╋╋┏┓
╋╋╋┃┃╋╋╋╋╋┏┛┗┓╋╋╋╋╋╋╋╋╋╋╋╋┏┛┗┓╋╋╋╋╋╋╋┃┃
┏━━┫┃┏━━┳━╋┓┏┛┏━━┳━━┳━┳━━┓┗┓┏╋━┳━━┳━━┫┃┏┳━━┳━┓
┃┏┓┃┃┃┏┓┃┏┓┫┃╋┃┏━┫┏┓┃┏┫┃━┫╋┃┃┃┏┫┏┓┃┏━┫┗┛┫┃━┫┏┛
┃┗┛┃┗┫┏┓┃┃┃┃┗┓┃┗━┫┏┓┃┃┃┃━┫╋┃┗┫┃┃┏┓┃┗━┫┏┓┫┃━┫┃
┃┏━┻━┻┛┗┻┛┗┻━┛┗━━┻┛┗┻┛┗━━┛╋┗━┻┛┗┛┗┻━━┻┛┗┻━━┻┛     
┃┃            
┗┛


## About The Project
Plant care tracker is a website that allows users to care for their plants. 
It provides a platform to empower users with knowledge, tools, and resources to care for their plants.
 
User can sign up and log in to the plant care tracker web app, add plants they own to their collection and track the next care date. 
The next care date will be automatically populated based on user's input of the last care date.


## The Team

- Cynthia Karimi
- Emoefe Oweibo
- Heather Embleton
- Jaqueline Arcangelo
- Morta Antanaviciute

## Getting Started

1. Fork and clone the repo<br/>

In the terminal navigate to the directory where you want to clone the project<br/>

Use the `git clone` command and paste the clone HTTPS URL or SSH then press enter :

SSH
```shell
$ git clone git@github.com:username/Plant_care_tracker.git 
```

HTTPS
```shell
$ git clone https://github.com/username/Plant_care_tracker.git
```

2. On your local machine go inside of the *Plant_care_tracker* directory :

```shell
$ cd Plant_care_tracker
```

## Prerequisites
The project requires the following packages and requirements
- flask 
- requests 
- mysql-connector-python
- bcrypt 
- flask-login 
- python_version: 3.10

Run the following command in the terminal to install these packages and requirements:

```shell
$ pipenv install 
```

To activate this project's virtualenv, run the following command:
```shell
pipenv shell
```

## Database setup

1. Set up database

Navigate to `database/PlantsDB.sql` and run the script in MySQL workbench to set up the database

2. Config Database password 

Go to `database/config.py`, replace "password" with your own database password :
```shell
PASSWORD = "Your Database Password"
```

3. Run `json_data_handler.py` to add the plants data to the plant table in MySQL


## How to run the app

Make sure you are in the *Plant_Care_tracker* directory and run the following commands :


1. To run the server that renders the HTML webpages
```shell
$ python plant.py 
```
2. Sign up by registering an account on the web app<br/>


Thank you for using Plant Care Tracker to keep your plants growing and flourishing! 🪴