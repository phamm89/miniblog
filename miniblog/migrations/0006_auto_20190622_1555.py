# Generated by Django 2.2.2 on 2019-06-22 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniblog', '0005_blogcomment_user_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogcomment',
            name='comment_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
