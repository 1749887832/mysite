from django.db import models


# Create your models here.
class Server(models.Model):
    id = models.AutoField(primary_key=True)
    # server
    server = models.CharField(max_length=128, null=True)


class Modular(models.Model):
    id = models.AutoField(primary_key=True)
    # modular_name
    modular_name = models.CharField(max_length=128, null=True)


class content(models.Model):
    id = models.AutoField(primary_key=True)
    # headers
    headers = models.CharField(max_length=256, null=True)
    # type
    type = models.CharField(max_length=128, null=True)
    # payload
    payload = models.CharField(max_length=1024, null=False)
    # modular_id
    modular_id = models.IntegerField(null=False)
