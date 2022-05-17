from django.db import models



class Post(models.Model):
    image = models.ImageField(blank=False, null=False)
    title = models.CharField(max_length=255, blank=False, null=False)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.title