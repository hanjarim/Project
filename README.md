# Network Complaints Ticketing System
![Homepage](./static/img/tickethomepage.png)
## Objectives
A project to track the network complaints submitted by Safaricom users. The tool will be useful to the Network Optimization Engineers to keep track of issues reported to them. 

## Installation

### Requirements
* Python3 
* Docker
* HTML
* CSS

#### Clone the project
```
git clone
cd folder
```
#### Create a virtual environment and install dependencies
This will install Django and the required dependencies
```
python3 -m venv /opt/ticket_env
source /opt/ticket_env/bin/activate
pip install -r requirements.txt
```

#### Run database migrations
To create the database models, run the commands in the terminal
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser (and follow instructions)
```
#### How to run the project
Once all the dependencies are installed, run the following command in the terminal
```
python manage.py runserver
```
Open your browser and visit 127.0.0.1:8000

## Technologies used
* Python/Django
* DBSqlite Database
* ChartJS
* HTML5
* Bootstrap5

## System Architecture
![Architecture](./static/img/arch.png)

## CI/CD Plan
![cicd](./static/img/cicd.png)

## System structure
![system](./static/img/system.png)

## Project contributors
* Moses Kubo
* Kelvin Kangwe
* Mark Waihenya
* TM2

