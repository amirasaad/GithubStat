# Github Stat

REST microservice that list the languages used by the 100 trending public repos on GitHub.

[![Build Status](https://travis-ci.com/amirasaad/GithubStat.svg?branch=main)](https://travis-ci.com/amirasaad/GithubStat)
## Quick Start

To run locally simply cd into the root of repo and run following commands:

```bash
docker build -tag github-stat:latest
```
To run the server on port e.g. 8000
```bash
docker run -p 8000:8000 -it github-stat:latest uvicorn src.main:app --host 0.0.0.0 --port 8000
```

## API


`GET /language`
Endpoint to list the languages used by the 100 trending public repos on GitHub in last 30 days.

```bash
curl http://localhost:8000/languages/
```

### Testing

A postman `Github.postman_collection.json` collection is provided you can run by newman after running up the server

```bash
npm install -g newman
newman run Github.postman_collection.json
```

And also unit testing by pytest

```bash
docker exec -it github-stat:latest pytest
```
