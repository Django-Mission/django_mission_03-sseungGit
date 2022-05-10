# Generated by Django 4.0.4 on 2022-05-10 08:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0016_alter_faq_options_alter_inquiry_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_editor', to=settings.AUTH_USER_MODEL, verbose_name='수정자'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Faq_editor', to=settings.AUTH_USER_MODEL, verbose_name='수정자'),
        ),
    ]
