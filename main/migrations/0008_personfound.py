# Generated by Django 2.1.2 on 2018-10-23 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_prediction'),
    ]

    operations = [
        migrations.CreateModel(
            name='PersonFound',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(upload_to='found/')),
                ('uploaded_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
