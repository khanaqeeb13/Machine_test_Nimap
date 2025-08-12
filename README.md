# Machine_test_Nimap
The task is to design APIS for the machine test using any REST framework


HOW TO RUN MACHINE
1. Create an env
2. syntax to create env for windows python -m venv env
3. Activate the env with this syntax env\Scripts\activate
4. next run this command
5. pip install -r requirements.txt
6. Now let create a django project syntax are
7. django-admin startproject company_api
8. Next create the app syntax are
9. python manage.py startapp core

HOW TO RUN Db Design
1. First create a db for Postgres
2. DB name should be machine_test_db if you want you change the db name kindly change it in the setting.py file
3. I am leavin password section blank add yur DB password
4. Update the data of DATABASES section as per your need in setting.py file
5. After updating the data let migrate the model to the DB syntax are
6. python manage.py makemigrations
7. python manage.py migrate
8. After migrate let make the superadmin
9. python manage.py createsuperuser
10. It will ask the user name and password write what u want
11. Done creating your DB and Admin also is ready

How to run the code 
1. After completing the code
2. python manage.py runserver 8800
3. 8800 is a port number foru to run
4. with this you can run the code
5. Then open this url http://127.0.0.1:8800/api
6. it will take u to api page
7. There u login with your admin password and username that u have given when making the superadmin
8. when u done the login there will be 2 url
9. 1 is for client
10. 2 is for project
11. When u click on client there u can see the data of client and which project there are working
12. And in project section u can see how many project is there
13. 
