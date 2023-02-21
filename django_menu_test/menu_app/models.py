from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def children(self):
        return self.menu_set.all()
    
    def __str__(self):
        return self.name