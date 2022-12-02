from django.db import models


class Contact(models.Model):
    """Сообщение в форме обратной связи на странице Contact"""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField()
    message = models.TextField()
    time_create = models.DateTimeField(auto_now_add=True)
    reply = models.BooleanField(default=False)

    class Meta:
        ordering = ['-time_create']

    def __str__(self):
        return self.email
