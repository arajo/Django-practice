from django.db import models

# Create your models here.

class Fcuser(models.Model):
    username = models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    registered_dttm = models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    

    def __str__(self):
        return self.username   # Fcuser object라고 적힌 것을 변환
                                # Fcuser 클래스를 str으로 반환할 때, username을 반환하도록 함

    class Meta:
        db_table ='fastcampus_fcuser'
        verbose_name = '패스트캠퍼스 사용자'
        verbose_name_plural = '패스트캠퍼스 사용자'
