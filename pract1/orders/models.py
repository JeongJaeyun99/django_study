from django.db import models

from book.models import Books
from users.models import Users


# Create your models here.

# models.Model은 상속하는것임
# id는 autoincrement라서 장고에서는 자동생성 되므로 따로 넣어주지 않아도 된다.
# verbose_name은 필드네임
class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE,verbose_name='user_id')
    book = models.ForeignKey(Books,on_delete=models.CASCADE,verbose_name='book_id')
    address = models.CharField(max_length=100,verbose_name='address')
    price = models.IntegerField(verbose_name="price")

    # __str__ >> __~__는 클래스가 갖고잇는 내장함수 __str__는 toString이랑 같다 >> 출력만 하는것!
    def __str__(self):
       return f"Order : {self.user.name} -> {self.book.title}"


    class Meta:
       db_table = 'orders'