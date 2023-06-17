from django.db import models

class Client(models.Model):
    """
        Modelo del cliente con los campos solicitados
    """
    fullname = models.CharField('Nombre Completo',max_length=100)
    id_number = models.BigIntegerField('Número de documento', default=0)
    email = models.CharField(max_length=100)
    birthdate = models.DateField('Fecha de nacimiento', null=True)
    is_active = models.BooleanField(default = True) 
    date_joined= models.DateField('fecha de registro', auto_now_add= True)
    date_update = models.DateTimeField('fecha de actualizacion', auto_now= True)

    class Meta: 
        """Meta definition for Client."""

        verbose_name = 'Client'
        verbose_name_plural = 'Clients'

    def __str__(self):
        """Unicode representation of Client."""
        return self.fullname