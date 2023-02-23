from django.db import models

# Create your models here.
class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    menu = models.ForeignKey('menu', on_delete=models.CASCADE, blank=False, null=False, default=1)

    def children(self):
        return self.menuitem_set.all()
    
    def __str__(self):
        return self.name

    @staticmethod
    def get_parents(menu_item):
        if menu_item.parent:
            return MenuItem.get_parents(menu_item.parent) + [menu_item.parent.id]
        else:
            return []