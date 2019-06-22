# Generated by Django 2.2.2 on 2019-06-22 01:56

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('summary', models.TextField(help_text='Enter a brief summary of the blog entry', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Blogger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('bio', models.CharField(help_text='Tell us about yourself', max_length=1000, null=True)),
            ],
            options={
                'ordering': ['last_name', 'first_name'],
            },
        ),
        migrations.CreateModel(
            name='BlogInstance',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for this particular blog entry across whole blog', primary_key=True, serialize=False)),
                ('imprint', models.CharField(max_length=200)),
                ('blog_entry_date', models.DateField(blank=True, null=True)),
                ('blog_entry', models.TextField(help_text='Start your blog entry here', max_length=5000, null=True)),
                ('blog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniblog.Blog')),
            ],
            options={
                'ordering': ['blog_entry_date'],
            },
        ),
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID for the comments.', primary_key=True, serialize=False)),
                ('comment', models.TextField(max_length=200)),
                ('comment_date', models.DateField(auto_now=True, null=True)),
                ('blog_entry', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniblog.BlogInstance')),
            ],
            options={
                'ordering': ['comment_date'],
            },
        ),
        migrations.AddField(
            model_name='blog',
            name='blogger',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='miniblog.Blogger'),
        ),
    ]
