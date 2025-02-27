from django.db import models

# Create your models here.

# models.Model은 상속하는것임
# id는 autoincrement라서 장고에서는 자동생성 되므로 따로 넣어주지 않아도 된다.
# verbose_name은 필드네임
class Users(models.Model):
    name = models.CharField(max_length=50,verbose_name='name')
    email = models.CharField(max_length=100, verbose_name='email')
    age = models.IntegerField(verbose_name='age')

    # __str__ >> __~__는 클래스가 갖고잇는 내장함수 __str__는 toString이랑 같다 >> 출력만 하는것!
    def __str__(self):
       return self.name


    class Meta:
       db_table = 'users'