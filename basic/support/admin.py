from django.forms import TextInput, Textarea
from django.db import models
from django.contrib import admin
from .models import Faq, Inquiry, Answer

@admin.register(Faq)
class FaqModelAdmin(admin.ModelAdmin):
    list_display = ('faq','faq_category','updated_at')
    list_filter = ('faq_category',)
    search_fields = ('faq',)
    search_help_text = '질문을 입력해주세요.'
    fields = ('faq', 'faq_category', 'answer', ('writer', 'editor'))

class CommentInline(admin.TabularInline):
    model = Answer
    max_num = 1
    verbose_name = '답변'

@admin.register(Inquiry)
class InquiryModelAdmin(admin.ModelAdmin):
    list_display = ('title','category','created_at','writer')
    list_filter = ('category',)
    search_fields = ('title','email','chellphone')
    search_help_text = '질문제목, 이메일, 전화번호로 검색이 가능합니다.'
    fields = ('title', 'category', ('email','is_email'), ('chellphone', 'is_phone'),
                'content','image','writer')
    inlines = [CommentInline]