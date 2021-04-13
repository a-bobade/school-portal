# School Portal
This is a School Management website.
# Project website

# Project Summary
The website displays students records. Records can be tracked, edited and deleted. \
It shows the results of students, the results can as well be uploaded.

# Running the Project
- To get this project up and running you should start by having Python installed on your computer. 

- Activate the virtual environment with:\
  venv\Scripts\activate

- Clone or download this repository and open it in your editor of choice. 

- Then install the project dependencies with:\
  pip install -r requirements.txt

- Import the studentdata.sql file

- You need to connect to a MySQL server to run this project.\
  Edit DATABASES configurations in studentdatabase/settings.py

- Make migrations with these commands:\
  python manage.py makemigrations\
  python manage.py migrate

- Now you can run the project with this command:\
  python manage.py runserver
