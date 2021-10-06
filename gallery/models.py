from django.db import models

# Model for a gallery image. Uploaded images will be saved to media/images folder.

class Image(models.Model):
    title = models.TextField()
    pic = models.ImageField(upload_to='images/')

    def __str__(self):
        return self.title


