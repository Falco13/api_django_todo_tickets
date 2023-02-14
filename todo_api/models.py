from django.db import models
from django.contrib.auth.models import User


def image_directory_path(instance, filename):
    file_path = 'images/{author_username}/{img_title}-{filename}'.format(
        author_username=str(instance.creator.username),
        img_title=str(instance.img_title),
        filename=filename,
    )
    return file_path


class Todo(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    status = models.ForeignKey('Status', on_delete=models.PROTECT, related_name='todo_status')
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='todo_author')
    assigned_to = models.ManyToManyField(User, blank=True, related_name='todo_assigned_to')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ManyToManyField('Image', blank=True)

    def __str__(self):
        return f'Todo: {self.title}, from: {self.author}'


class Image(models.Model):
    img = models.ImageField(upload_to=image_directory_path)
    img_title = models.CharField(max_length=55)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.img}] with title [{self.img_title}], from [{self.creator}]'


class Status(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'status'
        verbose_name_plural = 'statuses'

    def __str__(self):
        return f'Status: {self.title}'


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE, related_name='todo_comments')
    parent = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='children')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment {self.text} for {self.todo} from {self.author}'
