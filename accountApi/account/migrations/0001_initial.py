# Generated by Django 3.2.13 on 2022-05-13 09:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('type', models.CharField(default=None, max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]