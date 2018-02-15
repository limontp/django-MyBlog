from django.db import models

class Series(models.Model):
    title = models.CharField(max_length=120)
    url = models.CharField(max_length=120, unique=True)

    description = models.TextField()

    def __str__(self):
        return self.title

class Post(models.Model):
    series = models.ForeignKey(Series, blank=True, null=True, on_delete=models.CASCADE)

    title = models.CharField(max_length=120, default='')
    content = models.TextField(default='')
    views = models.IntegerField(default=0)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

