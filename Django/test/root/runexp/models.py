from django.db import models
from django.urls import reverse
from django.utils import timezone
import uuid

# Create your models here.
class Session(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=50, null=True, blank = True, unique = True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def get_absolute_url(self):
        return reverse('runexp:session',kwargs={'filename':self.filename})
    def __str__(self):
        return str(self.filename)

class Experiment(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    edit_date = models.DateTimeField(auto_now=True)
    session = models.ForeignKey(Session,on_delete=models.CASCADE)
    concentration = models.FloatField(default=0)
    result = models.FloatField(default=0)
    eid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    def get_absolute_url(self):
        return reverse('runexp:session',kwargs={'filename':self.session.filename})
    def __str__(self):
        return str(self.eid)