from django.db import models

class Origin(models.Model):
    id=models.CharField(max_length=16,unique=True,primary_key=True)
    brief = models.TextField()
    caused =models.TextField()
    spread =models.TextField()
    danger =models.TextField()

    def __str__(self):
        return self.id
