from django.db import models
from django.urls import reverse

class Employee(models.Model):
    eid=models.CharField(max_length=20)
    ename=models.CharField(max_length=100)
    eemail=models.CharField(max_length=400)
    econtact=models.CharField(max_length=100)

    class Meta:
        db_table='employee'

    def get_absolute_url_detail(self):
        return reverse("contact:detail", kwargs={"pk": self.pk})

    def get_absolute_url_update(self):
        return reverse("contact:update", kwargs={"pk": self.pk})

    def get_absolute_url_delete(self):
        return reverse("contact:delete", kwargs={"pk": self.pk})
