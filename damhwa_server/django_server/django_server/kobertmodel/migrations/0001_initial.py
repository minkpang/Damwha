# Generated by Django 3.2.7 on 2021-10-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Emotion',
            fields=[
                ('fno', models.BigIntegerField(primary_key=True, serialize=False)),
                ('happy', models.FloatField(blank=True, db_column='Happy', null=True)),
                ('unstable', models.FloatField(blank=True, db_column='Unstable', null=True)),
                ('embarrass', models.FloatField(blank=True, null=True)),
                ('sad', models.FloatField(blank=True, null=True)),
                ('angry', models.FloatField(blank=True, null=True)),
                ('hurt', models.FloatField(blank=True, null=True)),
                ('emotion', models.TextField(blank=True, db_column='Emotion', null=True)),
            ],
            options={
                'db_table': 'emotion',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Feeling',
            fields=[
                ('feelingno', models.BigIntegerField(primary_key=True, serialize=False)),
                ('feelingname', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 'feeling',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Flower',
            fields=[
                ('fno', models.BigIntegerField(primary_key=True, serialize=False)),
                ('fnamekr', models.CharField(blank=True, db_column='fnameKR', max_length=40, null=True)),
                ('fnameen', models.CharField(blank=True, db_column='fnameEN', max_length=40, null=True)),
                ('fmonth', models.IntegerField(blank=True, null=True)),
                ('fday', models.IntegerField(blank=True, null=True)),
                ('flang', models.CharField(blank=True, max_length=100, null=True)),
                ('fcontents', models.CharField(blank=True, max_length=500, null=True)),
                ('fuse', models.CharField(blank=True, max_length=500, null=True)),
                ('fgrow', models.CharField(blank=True, max_length=500, null=True)),
                ('img1', models.CharField(blank=True, max_length=400, null=True)),
                ('img2', models.CharField(blank=True, max_length=400, null=True)),
                ('img3', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'db_table': 'flower',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='History',
            fields=[
                ('hno', models.BigIntegerField(primary_key=True, serialize=False)),
                ('htype', models.IntegerField(blank=True, null=True)),
                ('contents', models.CharField(blank=True, max_length=500, null=True)),
                ('to', models.CharField(blank=True, max_length=100, null=True)),
                ('regdate', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'history',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('userno', models.BigIntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=50)),
                ('username', models.CharField(blank=True, max_length=30, null=True)),
                ('profile', models.CharField(blank=True, max_length=400, null=True)),
                ('token', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
