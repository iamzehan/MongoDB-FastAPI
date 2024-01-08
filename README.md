## Here's the directory structure
___

```├── app
│   ├── __init__.py
│   ├── main.py
│   └── server
│       ├── app.py
│       ├── database.py
│       ├── models
│       └── routes
└── requirements.txt
```

### `main.py`
___
Responsible for running the app

### `server/`
___
Contains database schema and API routes

### `models/`
___
Contains files that define the structure of your database documents.
(This is a NoSQL Database so, there's no tabular schema)

### `routes/`
___
Basically handles all the requests
* GET
* POST
* PUT
* PATCH
* DELETE

### `app.py`
___
defines the urls (should've named it urls.py)

### `database.py`
___
Handles the connection with the database and as well as all the interactions between MongoDB server and the FastAPI server.