# определяет модель Note для работы  с дб
from django.db import models
from django.core.validators import MaxLengthValidator

class Note(models.Model):
    title = models.CharField(max_length=200,verbose_name='Заголовок'
                            , help_text='Введите заголовок заметки')
    content = models.TextField(validators=[MaxLengthValidator],
                                verbose_name='содержание',
                                help_text='введите содержание заметки')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Дата обновланиея')

    class Meta:
        verbose_name = 'Заметка'
        verbose_name_plural='Заметки'
        ordering = ['-created_at']

    def __str__(self):
        # возвращает строковое представления обьекта
        return self.title[:50]