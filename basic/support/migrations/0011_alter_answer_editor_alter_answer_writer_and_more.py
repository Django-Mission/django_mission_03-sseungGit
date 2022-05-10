# Generated by Django 4.0.4 on 2022-05-10 07:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('support', '0010_alter_inquiry_writer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_editor', to=settings.AUTH_USER_MODEL, verbose_name='수정자'),
        ),
        migrations.AlterField(
            model_name='answer',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answer_writer', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='editor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Faq_editor', to=settings.AUTH_USER_MODEL, verbose_name='수정자'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Faq_writer', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
        migrations.AlterField(
            model_name='inquiry',
            name='writer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Inquiry_writer', to=settings.AUTH_USER_MODEL, verbose_name='작성자'),
        ),
    ]
