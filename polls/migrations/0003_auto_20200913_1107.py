# Generated by Django 3.1.1 on 2020-09-13 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='pub_date',
            field=models.DateTimeField(default='sample', verbose_name='date published'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment_text',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
