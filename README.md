# CS411 Group Project

Contributors:

Kaelyn Shinbashi  (@kshinba)
Anton Njavro  (@njavro)
Zhitong Su  (@szt1112)
Danielle Wong (@daniellewyee)

Welcome to FinNews project for our CS411 class.
Project is based on Django.
It utilizes defualt SQLite database from Django, and 2 APIs for financial and news data.
For Financial data we use iexapis API, while for news data we use stocknewsapi API.
Our news API is currently limited to 500 free API calls (some of them already used). 

To start the project go to 'Project/demo/' directory.
From there run [$source venv/bin/activate] in order to activate venv.
Then go to Project/demo/finNews and run [$python3 manage.py runserver]. If some error due to corrupted database ocurrs, do the following:
1)delete db.sqlite3 and all migrations files
2)run python3 manage.py makemigrations
3)run python3 manage.py migrate


Enjoy your stay!
