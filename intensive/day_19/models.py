from django.db import models


class Workers(models.Model):
    """
    Рабочие
    """
    name = models.CharField('Рабочий', max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'workers'