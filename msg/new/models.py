from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
import datetime
# Create your models here.
class Info(models.Model):
    user_name = models.CharField(max_length=200)
    message = models.CharField(max_length=2000)
    date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.user_name

    def get_absolute_url(self):
        return reverse("info_list",kwargs={'pk':self.pk})
