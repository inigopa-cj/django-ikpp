from django.db import models

# Create your models here.
class RRSS(models.Model):

    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Red Social", max_length=200)
    url = models.URLField(verbose_name="Enlace", max_length=200, null=True, blank=True)
    created = models.DateTimeField(verbose_name="Fecha de creación", auto_now_add=True)
    update = models.DateTimeField(verbose_name="Fecha de modificación", auto_now=True)

    class Meta:
        verbose_name = "enlace"
        verbose_name_plural = "enlaces"
        ordering = ['name']

    def __str__(self):
        return self.name
