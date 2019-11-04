from django.db import models
from django.urls import reverse

class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    eemail=models.CharField(max_length=400)
    econtact=models.CharField(max_length=100)

    class Meta:
        db_table='employee'

    def get_absolute_url(self):
        return reverse("createcrud:detail",kwargs={"id":self.id})
