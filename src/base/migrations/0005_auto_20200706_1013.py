# Generated by Django 2.2 on 2020-07-06 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_auto_20200706_1006'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuestionPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=1000)),
                ('tag', models.CharField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name='Date published')),
            ],
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]