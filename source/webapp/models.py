from django.db import models

class Status(models.Model):
    status_name = models.CharField(max_length=20, verbose_name='Status_name')

    def __str__(self):
        return self.status_name


class Type(models.Model):
    type_name = models.CharField(max_length=20, verbose_name='Type_name')

    def __str__(self):
        return self.type_name

class Task(models.Model):
    summary = models.CharField(max_length=100, verbose_name="Summary")
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name="Description")
    status = models.ForeignKey(Status, related_name='statuses', on_delete=models.PROTECT, verbose_name='Status')
    type = models.ForeignKey(Type, related_name='types', on_delete=models.PROTECT, verbose_name='Type')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created date')

    def __str__(self):
        return self.summary