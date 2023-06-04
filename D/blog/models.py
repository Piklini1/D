from django.db import models

class Post(models.Model):
    '''post'''
    title = models.CharField('textname', max_length=200)
    description = models.TextField('text')
    author = models.CharField('nikname', max_length=25)
    date = models.DateField('data')
    img = models.ImageField('image', upload_to='image/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

class Comments(models.Model):
    '''Com'''
    name = models.CharField('nikname', max_length=25)
    text_comments = models.TextField('text comm', max_length=1000)
    post = models.ForeignKey(Post, verbose_name='Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'post comm'
        verbose_name_plural = 'posts comm'