# Generated by Django 4.0.4 on 2022-05-10 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0014_alter_faq_faq_category_alter_inquiry_phone_num'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inquiry',
            name='phone_num',
            field=models.IntegerField(help_text="'-'은 빼고 입력해주세요.", verbose_name='전화번호'),
        ),
    ]