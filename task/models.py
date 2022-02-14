from django.db import models

class Task(models.Model):
    name = models.CharField(max_length = 100, verbose_name="ФИО")
    cat = models.CharField(max_length=100,verbose_name="Курстун аталышы" )
    task_num = models.DecimalField(max_digits=5, decimal_places=0, verbose_name="Канчанчы сабак?" )
    media = models.FileField(upload_to='task/%Y/%m/%d/', verbose_name='Тапшырманын',  blank=True)

    def __str__(self):
        return self.cat

    class Meta:
        verbose_name = 'Тапшырма'
        verbose_name_plural = 'Тапшырмалар'
        ordering = ['cat']
        


