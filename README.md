# Social Media API (FastAPI backend)

A backend API for a social media app, built with **FastAPI** and **PostgreSQL**. Users can sign up, log in with a JWT token, create and manage posts, and vote (like) on posts. Interactive API docs are generated automatically at `/docs`.

## Tech stack
- **Language:** Python
- **Framework:** FastAPI, served with Uvicorn
- **Database:** PostgreSQL (psycopg2), SQLAlchemy ORM, Alembic migrations
- **Authentication:** JWT access tokens (python-jose), password hashing with bcrypt (passlib)
- **Validation and settings:** Pydantic, pydantic-settings (reads the `.env` file)
- **Testing:** pytest

## API routes
| Route group | What it does |
|---|---|
| **Posts** | Create, read, update, and delete posts |
| **Users** | Create a user and look up a user by ID |
| **Auth** | Log in and receive a JWT access token |
| **Vote** | Like a post and remove your like |

Open `/docs` after starting the server to see every endpoint and try it out. Use the **Authorize** button there to log in and test the protected routes.

## How to run locally

**1. Clone the repo and create a virtual environment**
```bash
git clone https://github.com/Sam-2610/<your-repo-name>.git
cd <your-repo-name>
python -m venv venv
venv\Scripts\activate            # Windows (Mac/Linux: source venv/bin/activate)
pip install -r requirements.txt
```

**2. Create a PostgreSQL database**
Create an empty database (for example, with pgAdmin or `createdb`) and remember its name, user and password.

**3. Create a `.env` file** in the project folder:
```
DATABASE_HOSTNAME=localhost
DATABASE_PORT=5432
DATABASE_PASSWORD=your_database_password
DATABASE_NAME=your_database_name
DATABASE_USERNAME=your_database_user
SECRET_KEY=your-secret-key
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```
Generate your own `SECRET_KEY` with:
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```
Never commit your real `.env` file. It is listed in `.gitignore`.

**4. Create the tables** (skip this if your app creates them on startup)
```bash
alembic upgrade head
```

**5. Start the server**
```bash
uvicorn app. main: app --reload
```
If your `main.py` is in the project root and not in an `app` folder, use `uvicorn main: app --reload` instead.

**6. Open the docs:** http://127.0.0.1:8000/docs

## Tests
```bash
pytest
```

## Credits
Based on the FastAPI course by Sanjeev Thiyagarajan.
