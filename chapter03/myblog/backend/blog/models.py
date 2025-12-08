from django.db import models


class BaseTimeStampModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Blog(BaseTimeStampModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey("author.Author", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
