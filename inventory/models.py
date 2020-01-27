from django.db import models

class Client(models.Model):
    title = models.CharField(max_length=50, verbose_name='이름')
    call_number = models.CharField(max_length=13, verbose_name='전화번호')
    address = models.CharField(max_length=100, verbose_name='주소')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Product(models.Model):
    title = models.CharField(max_length=100,verbose_name="제품명")
    content = models.TextField(verbose_name="제품설명")
    price = models.PositiveIntegerField(verbose_name='가격')
    remains = models.PositiveIntegerField(verbose_name='남은 수량')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='거래처', related_name='product')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

