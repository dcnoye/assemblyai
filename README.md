# Assignment:
```c
  AssemblyAI Interview Project : "Webhook-as-a-Service"
```

### Setting up a development environment

We assume that you have `git` and `virtualenv` installed.

```bash
    # Clone the code repository 
    git clone https://github.com/dcnoye/AssemblyAI.git

    # Create & activate the virtual environment
    python3 -m venv venv36
    source venv36/bin/activate

    # Install required Python packages
    cd AssemblyAI
    pip install -r requirements.txt

    #Initailize the database
    flask shell
```
```python
    >>> from app import db
    >>> db.create_all()
    >>> exit()
```

### Starting the server via commandline:

We assume that you have redis setup
```bash
    rq worker high
    python wsgi.py
```

### Starting the server via docker-compose:
```
    docker-compose build
    docker-compose up -d 
```

### API Endpoints


Will return the status of an id
```bash
    GET /api/v1/hooks/<id>
```

Will return a list of all items with status
```bash
    GET /api/v1/hooks
```

New item to webhook
```bash
    POST /api/v1/hooks
```

***Examples & testing:***
```bash

curl -X GET https://AssemblyAI.noye.org/api/v1/hooks/52d0cae3-45c5-439f-ab81-2205f52a821c

curl -X GET https://AssemblyAI.noye.org/api/v1/hooks

curl -X POST \
  -H 'X:process' -H 'content-type:application/json' \
  -d '{"url":"https://rest.coinapi.io/v1/assets","headers":{"X-CoinAPI-Key": "65AC7BFD-177F-49E6-9BD6-0E93C098782B"}}'  http://localhost:5000/api/v1/hooks
```



