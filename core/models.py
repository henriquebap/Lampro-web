from django.db import models

from stdimage.models import StdImageField

class Base(models.Model):
    criados = models.DateField('criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('anel.svg', 'Anel'),
        ('colar.svg', 'Colar'),
        ('brico.svg', 'Brinco'),
        ('envio.svg', 'Envio'),
    )
    servico = models.CharField('Serviço', max_length=100)
    descricao = models.TextField('Descrição', max_length=200)
    icone = models.CharField('Icone', max_length=9, choices=ICONE_CHOICES)

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico

