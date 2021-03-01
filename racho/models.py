from django.db import models



class FeedBack(models.Model):
    name = models.CharField('Name', max_length=120)
    email = models.EmailField('email', max_length=120, blank=True, null=True )
    description = models.CharField('описание', max_length=120, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма обратной связи'
        verbose_name_plural = 'Формы обратной связи'

