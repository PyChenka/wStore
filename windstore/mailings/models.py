from django.db import models


class MailingList(models.Model):
    """Email подписчика рассылки на сайте"""
    email = models.EmailField()

    class Meta:
        db_table = 'mailings_list'
