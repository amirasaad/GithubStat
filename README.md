# Github Stat

REST microservice that list the languages used by the 100 trending public repos on GitHub.

# Usage

To run locally simply cd into the root of repo and run following commands:

```bash
pip install -r requirements/local.txt
uvicorn src.api:app --reload
```

Or using docker

```bash
docker build -t github-stat .
docker run -d --name github-stat -p 80:80 github-stat
```

# API


`GET /language`
Endpoint to list the languages used by the 100 trending public repos on GitHub in last 30 days.

```bash
curl http://localhost:8000/languages/
```

# Testing

A postman `Github.postman_collection.json` collection is provided you can run by newmap after running up the server

```bash
npm install -g newman
newman run Github.postman_collection.json
```
