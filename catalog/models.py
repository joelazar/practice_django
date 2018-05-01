from django.db import models


class Presentation(models.Model):
    presentation_id = models.CharField(max_length=36, unique=True)
    picture = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField('createdAt')
    creator = models.CharField(max_length=50)

    readonlyfields = ('presentation_id', 'created_at', 'creator',)

    def __str__(self):
        return '%s %s' % (self.presentation_id, self.title)
