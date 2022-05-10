# Generated by Django 4.0.4 on 2022-05-09 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0003_alter_answer_writer'),
    ]

    operations = [
        migrations.AddField(
            model_name='inquiry',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='작성일'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inquiry',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='수정일'),
        ),
        migrations.AddField(
            model_name='inquiry',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Inquiry_작성자', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='faq',
            name='faq',
            field=models.TextField(verbose_name='제목'),
        ),
    ]
