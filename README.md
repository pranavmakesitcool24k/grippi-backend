# Campaign Analytics Dashboard - Backend

This is the FastAPI backend for the Campaign Analytics Dashboard. It exposes REST API endpoints backed by a SQLite database for managing campaign data.

## Features

- `GET /campaigns`: Returns a list of campaigns, optionally filtered by status
- Simple SQLite database integration
- CORS enabled for frontend communication

## Setup

1. Clone the repository

```
git clone https://github.com/pranavmakesitcool24k/grippi-backend.git
cd grippi-backend
```

2. Create and activate Python virtual environment (optional but recommended)

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run the app locally

```
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Access API at `http://localhost:8000/campaigns`

## Deployment on Railway

- Link your GitHub repository in Railway.
- Set the start command to:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

- Railway automatically provides the `$PORT` environment variable.
- Deploy and get the public URL.
- Use this URL in the frontend environment variable `NEXT_PUBLIC_BACKEND_URL`.

## Database

SQLite database file: `campaigns.db`

Make sure the database file is included/deployed properly or setup migrations for production.

## License

This project is licensed under the MIT License.
```

***

To download, copy each content into a plain text file named `README.md` in your respective frontend and backend project folders. If you want, I can generate those as uploadable files. Just ask!
