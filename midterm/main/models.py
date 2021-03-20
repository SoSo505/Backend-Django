from django.db import models

# Create your models here.
class BookJournalBase(models.Model):
    name = models.CharField(max_length=100, null=False, verbose_name="name")
    price = models.IntegerField(verbose_name="price")
    description = models.CharField(max_length=250, null=False, verbose_name="Due on")
    created_at = models.DateTimeField(null=False, verbose_name="Created")

    class Meta:
        verbose_name = 'bookJournalbase'

        def __str__(self):
            return self.name


class Book(models.Model):

    num_pages = models.IntegerField(verbose_name="price")
    genre = models.CharField(max_length=100, null=False, verbose_name="genre")
    groupforbook = models.ManyToManyField(BookJournalBase, on_delete=models.RESTRICT(), verbose_name="band name", related_name="group")

    class Meta:
        verbose_name = 'book'

        def __str__(self):
            return self.name


class Journal(models.Model):

    bullet = models.BooleanField(default=False, verbose_name="Bullet")
    food = models.BooleanField(default=False, verbose_name="Food")
    travel = models.BooleanField(default=False, verbose_name="Travel")
    sport = models.BooleanField(default=False, verbose_name="Sport")

    bookjournalbase = models.ForeignKey(BookJournalBase, on_delete=models.CASCADE, verbose_name="band_name", related_name="group")

    class Meta:
        verbose_name = 'journal'
        verbose_name_plural = 'journals'

        def __str__(self):
            return self.name
