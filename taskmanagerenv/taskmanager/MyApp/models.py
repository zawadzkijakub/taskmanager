from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name


PRIORITY = (
    ('medium', 'medium'),
    ('high', 'high'),
    ('very high', 'very high'),
)


class Task(models.Model):
    name = models.CharField(max_length=128, verbose_name='name')
    categorie = models.ForeignKey(Categories, on_delete=models.CASCADE, verbose_name='categorie')
    date = models.DateTimeField(null=True)
    deadline = models.DateField(null=True)
    priority = models.CharField(choices=PRIORITY, max_length=128, null=True)
    create_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class MyMessage(models.Model):
    description = models.CharField(max_length=2048)
    fromwho = models.ForeignKey(User, on_delete=models.CASCADE, related_name='fromwho')
    towho = models.ForeignKey(User, on_delete=models.CASCADE, related_name='towho')


#class LogHistory(models.Model):
#    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='history_name')
#    log_history = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='log_history')

