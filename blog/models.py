from django.db import models

STATUS = (
    (0,"Draft"),
    (1,"Publish"),
)
#Model for a blog post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['pub_date']

    def __str__(self):
        return self.title