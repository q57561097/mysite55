#coding:utf-8
from django.db import models

class Yonghu(models.Model):
    username=models.CharField('用户名',max_length=100,null=False)
    password=models.CharField('密码',max_length=100,null=False)
    email=models.EmailField('邮箱',null=False)
    last_login = models.DateTimeField(blank=True,null=True)


    def __str__(self):
        return self.name
