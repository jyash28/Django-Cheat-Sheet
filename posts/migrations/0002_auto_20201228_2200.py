# Generated by Django 2.2.1 on 2020-12-28 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['-created_at'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='posts',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AddField(
            model_name='posts',
            name='thumbnail',
            field=models.FileField(null=True, upload_to='posts/'),
        ),
    ]
