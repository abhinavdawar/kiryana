# kiryana
This is an application written in Django and Mysql Database with docker image file.

To run this application. First setup a virtual environment and install all the dependencies in requirements.txt file
-> pip install requirements.txt

Then setup the mysql database according to the app. And then to populate data into the database.
3 .json files are there. Just run the management command to enter the data into application.
-> python manage.py add_data category_config.json product_config.json item_config.json
