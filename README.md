# Group Chat WebApp (Django)

This is a group chat web application created using the Python framework Django. Please note that this project is still under development.

## Functionality Highlights

- Only Admins can create rooms.
- All users can see every room and join any room to start interacting with group members in real-time.

## How to Run the App

1. Clone the project repository and navigate to the project directory.

2. Create a virtual environment (recommended):

virtualenv your_env_name

3. Activate your virtual environment:

.\your_env_name\Scripts\activate


4. Install all the required libraries:

pip freeze > requirement.txt
pip install -r requirement.txt


5. Setup the database (MySQL):
- Replace the database credentials in the Django settings with your database credentials.

6. Run the following commands:

python manage.py makemigrations
python manage.py migrate
python manage.py runserver

Now you can access the Group Chat WebApp by visiting the provided URL in your browser.

## Note
Please ensure that you have Python and MySQL installed on your system before running the application.
