from django.db import models

class Quest(models.Model):
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=500)
    pub_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.title
