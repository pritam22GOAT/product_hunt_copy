from django.db import models
from django.contrib.auth.models import User 
from django.db.models import CharField
# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length = 30)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total = models.IntegerField(default=1)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:60]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b , %e , %Y')


