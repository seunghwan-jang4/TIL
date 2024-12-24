from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField
    created_at = models.DateTimeField(auto_now_add=True) # 추가될 때
    updated_at = models.DateTimeField(auto_now=True) # 수정될 때 