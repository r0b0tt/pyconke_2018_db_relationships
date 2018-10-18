#Pycon KE 2018
### "Ditching" Foreign Keys for Actual Database Relationships source code.

[Link to Slides](https://docs.google.com/presentation/d/1vg2MD-CYHdXNJmaZQhR9Tawy7Jz6KnpwKF7pS4IsVSk/edit?usp=sharing)

----
To run this code:
1. Clone the repository to your computer.
2. Create a python3 virtual environment.
3. Activate the environment and run:
``pip install -r requirements.txt``
4. Run migrations: ``python manage.py migrate``
5. Create superuser: ``python manage.py createsuperuser``
6. Run the application: ``python manage.py runserver``
7. Login into the admin account using the credentials for the superuser through this link:
``127.0.0.1:8000/admin/``