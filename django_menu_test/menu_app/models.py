from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    name = models.CharField(max_length=50, unique=True)
    url = models.CharField(max_length=100, blank=True, null=True, unique=True)
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        blank=True, null=True
    )
    menu = models.ForeignKey(
        'menu',
        on_delete=models.CASCADE,
        blank=False,
        null=False,
    )

    def __str__(self):
        return self.name

    @staticmethod
    def get_parents(child: dict, query: list[dict]) -> list:
        if child['parent_id']:
            parent = next(filter(
                lambda item: item['id'] == child['parent_id'],
                query
            ))
            return MenuItem.get_parents(parent, query) + [child['parent_id']]
        else:
            return []
