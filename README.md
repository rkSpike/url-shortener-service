# Url Shortener service (EltexSoft test) 

### Installation:

```
pipenv install
python manage.py migrate
python manage.py runserver
```

### Allowed methods

```
# Redirect by short url
http://127.0.0.1:8000/<short_id>

# List of all urls from host url
# Allowed for creator(IP)
GET api/stats/

# List of visits by <short_id>
# Allowed for creator(IP)
GET stats/<short_id>

# Create short url
POST url/ | params: url

# Delete short url
# Allowed for creator(IP)
DELETE url/<short_id>
```