from django.db import models
from django.contrib.auth.models import User


TAG = (
    ('未設定', '未設定'),
    ('タスク', 'タスク'),
    ('ノート', 'ノート'),
    ('重要', '重要'),
    ('複数', '複数'),
    ('その他', 'その他'),
)

class Shelf(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    tag = models.CharField(
        max_length=100,
        choices = TAG,
        )
    
    user = models.ForeignKey("auth.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
