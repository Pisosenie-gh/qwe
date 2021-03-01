
from django.db import models



class TopBack(models.Model):
    name = models.CharField('Name', max_length=120)
    description = models.CharField('описание', max_length=120, blank=True, null=True)
    email = models.EmailField('email', max_length=120, blank=True, null=True )
    phone = models.CharField('Telephone', max_length=11)
    document = models.FileField(upload_to='documents/', default=None)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'
