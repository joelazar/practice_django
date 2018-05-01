# Short documentation

I've implemented the described API service and also a web application beside it.

You can reach the web application on this url:
* <https://practice-django-joelazar.herokuapp.com/catalog/>

You can reach the api on this url:
* <https://practice-django-joelazar.herokuapp.com/api/presentation/>

The JSON seed file was first imported to the database by this [`small script`](import_db.py). The presentation owner users were created also to the database to by following this naming convention.
* name: Reid Dillard --> username: reid_dillard
* password: password (actually, every user password is password :) )

In my opinion the web application part is pretty self-evident, but let me share some example curl commands for the API usage.

Query all presentations:
```
$ curl https://practice-django-joelazar.herokuapp.com/api/presentation/
```

Query the next page of all presentations:
```
$ curl https://practice-django-joelazar.herokuapp.com/api/presentation/?limit=20&offset=20
```

Query a single presentation:
```
$ curl https://practice-django-joelazar.herokuapp.com/api/presentation/1/
```

Filter all presentations by given id (exact match):
```
$ curl https://practice-django-joelazar.herokuapp.com/api/presentation/?presentation_id=6defd952-b3e3-41a6-9672-aa80acace0fa
```

Filter all presentations by title (contain):
```
$ curl https://practice-django-joelazar.herokuapp.com/api/presentation/?title__contains=te
```

Sort all presentations in ascending order:
```
$ curl https://practice-django-joelazar.herokuapp.com/api/presentation/?order_by=created_at
```

Sort all presentations in descending order:
```
$ curl https://practice-django-joelazar.herokuapp.com/api/presentation/?order_by=-created_at
```

Change a presentation title:
```
$ curl -u "reid_dillard:password" -X PUT https://practice-django-joelazar.herokuapp.com/api/presentation/1/ -H "Content-Type: application/json" -d "{\"created_at\":\"2015-12-30T21:37:07\",\"creator\":\"Reid Dillard\",\"id\": 1, \"picture\":\"http://placehold.it/128x128\",\"resource_uri\":\"/api/presentation/1/\",\"title\":\"new title\"}"
```

Heroku config:
```
DEBUG:                 False
DISABLE_COLLECTSTATIC: 1
```
