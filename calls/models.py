from django.db import models

"""  CLIENTE  """
class Client(models.Model):
  name = models.CharField(max_length=50, null=False, blank=False)
  address = models.CharField(max_length=60, null=False, blank=False)
  phone = models.CharField(max_length=9, null=False, blank=False)

  def __str__(self):
    return self.name



"""  SERVIÇO  """
class Service(models.Model):
  value = models.FloatField(null=False)
  description = models.CharField(max_length=30, null=False, blank=False)

  def __str__(self) -> str:
    return self.description


""" ATENDIMENTO """
class Call(models.Model):
  STATUS_CHOICES = (
    ('Pendente', 'Pendente'),
    ('Realizado', 'Realizado'),
    ('Cancelado', 'Cancelado'),
  )
  PAYMENT_CHOICES = (
    ('Débito', 'Débito'),
    ('Crédito', 'Crédito'),
    ('Em espécie', 'Em espécie'),
    ('PIX', 'PIX')
  )

  client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, related_name='order_client')
  services = models.ManyToManyField(Service)

  status = models.CharField(max_length=10, choices=STATUS_CHOICES, null=False, default='Pendente', auto_created='Pendente')
  payment = models.CharField(max_length=20, choices=PAYMENT_CHOICES) 

  service_date = models.DateTimeField(null=False, blank=False)
  order_registration_date = models.DateTimeField(auto_now_add=True, null=False)
