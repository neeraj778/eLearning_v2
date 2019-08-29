# Generated by Django 2.1.4 on 2019-08-02 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_registration', '0002_auto_20190801_1726'),
    ]

    operations = [
        migrations.CreateModel(
            name='courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=64)),
                ('course_id', models.CharField(max_length=64)),
                ('course_description', models.CharField(max_length=1024)),
                ('course_fee', models.IntegerField(null=True)),
            ],
        ),
    ]