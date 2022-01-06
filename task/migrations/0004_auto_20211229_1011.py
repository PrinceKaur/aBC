# Generated by Django 3.2.3 on 2021-12-29 04:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20211228_1017'),
    ]

    operations = [
        migrations.CreateModel(
            name='User1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_choice', models.CharField(choices=[('1', 'seller'), ('2', 'buyer')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='user2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.products')),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='user1',
            name='User1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.user2'),
        ),
    ]
