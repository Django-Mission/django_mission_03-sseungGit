# Generated by Django 4.0.4 on 2022-05-10 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('support', '0017_alter_answer_editor_alter_faq_editor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faq',
            name='faq',
            field=models.CharField(max_length=30, verbose_name='제목'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='title',
            field=models.CharField(max_length=30, verbose_name='제목'),
        ),
    ]
