from django.db import models


class Url(models.Model):
    url = models.TextField()
    short_id = models.CharField(max_length=6)
    creator_ip = models.CharField(max_length=10)

    def __str__(self):
        return '<Creator {}:[{} -> {}]>'.format(
            self.creator_ip, self.url, self.short_id)


class Visit(models.Model):
    url = models.ForeignKey(Url, on_delete=models.CASCADE)
    visitor_ip = models.CharField(max_length=10)
    visit_time = models.DateTimeField(null=True, auto_now_add=True)

