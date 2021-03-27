from django.db import models

# Create your models here.


class Todocompleteornot(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="band name")

    class Meta:
        verbose_name = 'Is completed or not?'

    def __str__(self):
        return self.name






class Todotasks(models.Model):

    taskname = models.CharField(max_length=100, null=False, verbose_name="Task")
    created = models.DateTimeField(null=False, verbose_name="Created")
    due_on = models.DateTimeField(null=False, verbose_name="Due on")
    owner = models.CharField(max_length=100, null=False, verbose_name="Owner")
    mark = models.BooleanField(default=False, verbose_name="Mark")
    group = models.ForeignKey(Todocompleteornot, on_delete=models.CASCADE, verbose_name="band name", related_name="Todos")

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

    def __str__(self):
        return self.name



