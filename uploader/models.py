from django.db import models
from django.core.files.storage import default_storage
from django.db import connection
class Pictures(models.Model):
    path = models.TextField(primary_key=True)
    color = models.TextField()
    texture = models.TextField()
    image = models.FileField(upload_to='uploaded')

    def __unicode__(self):
        return str(self.path)

    class Meta:
        db_table = u'Pictures'
# Create your models here.
