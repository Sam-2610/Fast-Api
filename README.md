# Backend clone  of a social media app using FastAPI

#### This API  has 4 routes

## 1) Post route

#### This route is responsible for creating posts, deleting posts, updating posts, and checking posts

## 2) Users route

#### This route is about creating users and searching users by ID

## 3) Auth route

#### This route is about the login system

## 4) Vote route

 #### This route handles the likes/vote system and includes code for upvoting or downvoting. There is no logic for downvoting

# How to run locally
First, clone this repo using the following command
````

git clone https://github.com/Sanjeev-Thiyagarajan/fastapi-course.git

````
then 
````

cd fastapi-course

````

Then install FastAPI using the all flag like 

````

pip install fastapi[all]

````

Then go to this repo folder on your local computer and run the following command
````

uvicorn main: app --reload

````

Then you can use the following link to use the  API

````

http://127.0.0.1:8000/docs 

````

## After running this API, you need a database in Postgres 
Create a database in Postgres, then create a file named .env and write the following things in your files and o

````
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = passward_that_you_set
DATABASE_NAME = name_of_database
DATABASE_USERNAME = User_name
SECRET_KEY = 09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7 
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 60(base)

````
### Note: SECRET_KEY in this example is just a pseudo key. You need to get a key for yourself, and you can get the SECRET_KEY  from FastAPI documentation
 

