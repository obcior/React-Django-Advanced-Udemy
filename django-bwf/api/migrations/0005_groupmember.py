# Generated by Django 3.2.5 on 2021-08-09 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20210806_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='api.group')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members_of', to='api.group')),
            ],
            options={
                'unique_together': {('user', 'group')},
                'index_together': {('user', 'group')},
            },
        ),
    ]
