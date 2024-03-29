# Generated by Django 5.0.2 on 2024-03-03 02:58

import django.db.models.deletion
import uuid
from django.db import migrations, models

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=30, unique=True)),
                ('password_hash', models.TextField()),
                ('status', models.CharField(choices=[('student', 'Student'), ('instructor', 'Instructor')], default='student', max_length=20)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduspark.user')),
            ],
            options={
                'db_table': 'courses',
            },
        ),
        migrations.CreateModel(
            name='Assignment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('due_date', models.DateField()),
                ('max_points', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduspark.course')),
            ],
            options={
                'db_table': 'assignments',
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduspark.course')),
            ],
            options={
                'db_table': 'modules',
            },
        ),
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('order', models.IntegerField()),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduspark.module')),
            ],
            options={
                'db_table': 'lessons',
            },
        ),
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduspark.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduspark.user')),
            ],
            options={
                'db_table': 'enrollments',
            },
        ),
    ]
