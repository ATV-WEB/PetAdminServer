# PetAdminServer

A back-end for PetAdmin

## Setup Project

> On Windows:

```bash
py -m venv .venv
.venv/Scripts/activate
pip install -r requirements.txt
py manage.py migrate
py manage.py createsuperuser
py manage.py runserver
```

> On Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

after that you can acess <http://localhost:8000/api> and use normally
