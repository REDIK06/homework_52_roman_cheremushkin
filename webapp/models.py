from django.db import models

class Task(models.Model):
    status_choices = [
        ('new', 'Новая'),
        ('in_progress', 'В процессе'),
        ('done', 'Сделано'),
    ]

    description = models.TextField(max_length=500, null=False, blank=False, verbose_name="Описание")
    status = models.CharField(max_length=20, choices=status_choices, default='new', verbose_name="Статус")
    date_completion = models.DateField(null=True, blank=True, verbose_name="Дата выполнения")

    def __str__(self):
        return f'{self.id}.{self.description}'

    class Meta:
        db_table = 'tasks'
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
