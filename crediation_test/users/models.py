from django.db import models

class User(models.Model):
        firstname = models.CharField(max_length=20)
        lastname = models.CharField(max_length=20)
        email = models.EmailField()
        id = models.UUIDField(primary_key=True)

        def __str__(self):
            return "({}) {}".format(self.id, self.__dict__)

