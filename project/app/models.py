from django.db import models


class Refbook(models.Model):
    code = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=300)
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.code)

class RefbookVersion(models.Model):
    refbook = models.ForeignKey(Refbook, on_delete=models.CASCADE)
    version = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return str(self.refbook) + ' ' + str(self.version)


class RefbookElement(models.Model):
    refbook_version = models.ForeignKey(RefbookVersion, on_delete=models.CASCADE)
    code = models.CharField(max_length=100)
    value = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return str(self.refbook_version) + ' ' + str(self.code)