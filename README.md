unzip the file
install MongoDB community on your platform (Windows/Linux)
create .env file with
MONGO_URI = "mongodb://localhost:27017"
DATABASE_NAME = "ae_db"
SECRET_KEY = "91657b6bd77093b119f6a9130d92832fb90a8bff1b8833737b9a067462076a55"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10080
 and to run server:
 uvicorn app.main:app --reload

Loading a New Database:
Ensure that MongoDB is running on your system.
Use the mongorestore command to load the dump into a new database:
php
Copy code
mongorestore --db <new_database_name> <dump_directory>/<your_database_name>
Replace <new_database_name> with the name of the new database you want to create and <dump_directory>/<your_database_name> with the path to the dump directory containing the dump files for your original database.
Example:
Let's say you want to create a dump of a database named mydatabase and load it into a new database named newdatabase. Here are the commands you would use:

Creating a Dump:
css
Copy code
mongodump --db mydatabase --out /path/to/dump/directory
Loading into a New Database:
css
Copy code
mongorestore --db newdatabase /path/to/dump/directory/mydatabase
Replace /path/to/dump/directory with the actual path where you want to store your dump files.

