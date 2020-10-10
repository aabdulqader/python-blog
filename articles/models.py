from django.db import models
class Article(models.Model):
    title =models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    image = models.ImageField(default='default.png', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    '''
    def snippet(self):
        return self.body[:150]
    '''
class Contact(models.Model):
    slno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=50)
    sub = models.CharField(max_length=300)
    message = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.sub
    


