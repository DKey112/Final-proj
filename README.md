<h1 align="center">Diploma Project📝</h1>

<ul>
  Hi <img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/>, I'm Denis and this is my 
   diploma project.
</ul>

<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

<h3>The goal of the project</h3>
  The main goal of the project is to develop an app with information about cybersport.

<h3>Built With</h3>

<ul>
  <h4>Frontend:</h4>
  <li>HTML</li>
  <li>CSS</li>
  <li>Bootstrap</li>
  <h4>Backend:</h4>
  <li>Django</li>
</ul>

## Start

- Download project or clone repository
```
https://github.com/DKey112/Graduational_project.git
```
- Create virtual environment in Linux system-
```
python3 -m venv .venv
source .venv/bin/activate
```
- Create virtual environment in Wimdows system-
```
python -m venv .venv
.venv\Scripts\activate
```
- In Linux system install all dependencies from requirements.txt
```
make install
```
- In Windows system install all dependecies from requirements.txt
```
pip install -r requirements.txt
```
- We need to create a postgresql database  -
- <a href="https://www.postgresql.org/docs/current/sql-createdatabase.html">How to create database</a>
- <a href="https://docs.djangoproject.com/en/4.2/ref/databases/">How to connect database</a>

- We need to make migrations-
```
 python manage.py makemigrations
 python manage.py migrate
```
- Need to create a superuser-
```
 python manage.py createsuperuser
```
- Need to run server using-
```
python manage.py runserver
```


## Used resources

- [Django Docs](https://docs.djangoproject.com/en/4.2/)
- [PostgreSQL](https://www.postgresql.org/docs/current/sql-createdatabase.html)
- [Metanit](metanit.com)
- [Git and GitHub](https://www.digitalocean.com/community/tutorials/how-to-use-git-a-reference-guide) 
