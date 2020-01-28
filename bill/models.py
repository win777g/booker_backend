from django.db import models

# Create your models here.
class Bill(models.Model):

    value = models.CharField(max_length=120,blank=True, null=True, default=None)
    # вывод одного поля
    def __str__(self):
        return "Сумма %s " % (self.id )
    class Meta:
        verbose_name = 'Сумма'
        verbose_name_plural = 'Сумма'

    # def save(self, *args, **kwargs):
    #
    #      super(Order, self).save(*args, **kwargs)
