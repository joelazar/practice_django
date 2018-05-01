import json
from dateutil import parser

from django.contrib.auth.models import User
from django.db import IntegrityError

from catalog.models import Presentation


with open('db_seed.json') as datafile:
    data = json.load(datafile)

counter = 0
for element in data:

    uname = element['creator']['name'].lower().replace(" ", "_")
    if not User.objects.filter(username=uname).exists():
        user = User.objects.create_user(username=uname, password='password')
        user.is_superuser = False
        user.is_staff = False
        user.display_name = element['creator']['name']
        user.save()

    creation_date = parser.parse(element['createdAt'])

    item = Presentation(presentation_id=element['id'],
                        picture=element['picture'],
                        title=element['title'],
                        created_at=creation_date,
                        creator=element['creator']['name'])
    try:
        item.save()
    except IntegrityError:
        print("This item was already saved")

    counter += 1
    if counter % 50 == 0:
        print("%d. item imported" % counter)
