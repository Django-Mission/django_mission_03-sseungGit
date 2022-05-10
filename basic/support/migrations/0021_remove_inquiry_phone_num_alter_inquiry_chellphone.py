# Generated by Django 4.0.4 on 2022-05-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0020_inquiry_chellphone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inquiry',
            name='phone_num',
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='chellphone',
            field=models.CharField(help_text="'-'은 빼고 입력해주세요.", max_length=11, null=True, verbose_name='전화번호'),
        ),
    ]
