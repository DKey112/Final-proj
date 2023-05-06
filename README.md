<h1 align="center">Graduation_Project 📝</h1>

<ul>
  <li>my graduation project.</li>

  <li>Is a blog site that allows users to share their thoughts and knowledge with others.</li>
</ul>

<img src="https://badges.frapsoft.com/os/v1/open-source.svg?v=103" >

<h3>Tech Stack</h3>

<ul>
  <li>Frontend: HTML/CSS/Bootstrap</li>
  <li>Backend: Django</li>
</ul>

## Quick Start

- Fork and Clone the repository using-
```

```
- Create a Branch- 
```
git checkout -b <branch_name>
```
- Create virtual environment-
```
python -m venv .venv
source .venv/bin/activate
```
- Headover to Project Directory- 
```
cd blogproject
```
- Install dependencies-
- This command will install all dependencies from requirements.txt
```
make install


```
- Сreate .env file with variables-
```
DEBUG=True

SECRET_KEY=[YOUR SECRET KEY]
```
- To use postgresql database you need to create 2 files-
- <a href="https://docs.djangoproject.com/en/4.2/ref/databases/#postgresql-notes">Django Docs</a>

create a file .pg_service.conf
```
[my_service]
host=localhost
user=USER
dbname=NAME
port=5432
```
and file .pgpass
```
localhost:5432:NAME:USER:PASSWORD
```
- Make migrations using-
```
make migrate
```
- Create a superuser-
```
make superuser
```
- Run server using-
```
make run
```
- Push Changes-
```
git add .
git commit -m "<your commit message>"
git push --set-upstream origin <branch_name>
```

## Useful Resources to Learn

- [Django Docs](https://docs.djangoproject.com/en/4.2/)
- [Bootstrap Docs](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Git and GitHub](https://www.digitalocean.com/community/tutorials/how-to-use-git-a-reference-guide) 
