# Generated by Django 4.0.4 on 2022-05-10 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0013_alter_answer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='faq_category',
            field=models.IntegerField(choices=[(1, '주문/배송'), (2, '결제/환불'), (3, '취소/반품/교환'), (4, '멤버십'), (5, '기타')], verbose_name='카테고리'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='phone_num',
            field=models.IntegerField(help_text="'-'은 빼고 입력해주세요.", max_length=13, verbose_name='전화번호'),
        ),
    ]
