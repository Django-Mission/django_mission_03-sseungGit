import email
from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
CATEGORY = (
        (1, '주문/배송'),
        (2, '결제/환불'),
        (3, '취소/반품/교환'),
        (4, '멤버십'),
        (5, '기타'),
    )

class Faq(models.Model):
    faq = models.CharField(max_length=30,verbose_name='제목')
    faq_category = models.IntegerField(choices=CATEGORY ,verbose_name='카테고리')
    answer = models.TextField(verbose_name='답변')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Faq_writer', verbose_name='작성자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True,  related_name='Faq_editor', verbose_name='수정자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '자주 묻는 질문'
        verbose_name_plural = '자주 묻는 질문'
        ordering = ('-created_at',)

class Inquiry(models.Model):
    title = models.CharField(max_length=30,verbose_name='제목')
    email = models.EmailField(max_length=128 ,verbose_name='사용자 이메일')
    is_email = models.BooleanField(default=False, verbose_name='이메일 수신')
    category = models.IntegerField(choices=CATEGORY,verbose_name='카테고리')
    chellphone = models.CharField(max_length=11, help_text="'-'은 빼고 입력해주세요.", null=True, verbose_name='전화번호')
    is_phone = models.BooleanField(default=False, verbose_name='문자 수신')
    content = models.TextField(verbose_name='내용')
    image = models.ImageField(verbose_name='이미지', null=True, blank=True)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='Inquiry_writer', verbose_name='작성자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        verbose_name = '1:1 문의'
        verbose_name_plural = '1:1 문의'
        ordering = ('-updated_at',)

class Answer(models.Model):
    inquiry = models.ForeignKey('inquiry', on_delete=models.CASCADE)
    content = models.TextField(verbose_name='내용')
    writer = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='answer_writer', verbose_name='작성자')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')
    editor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name='answer_editor', verbose_name='수정자')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')
