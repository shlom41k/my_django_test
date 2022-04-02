# Generated by Django 4.0.2 on 2022-02-18 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(help_text='Input question', max_length=500, verbose_name='Question')),
                ('answer', models.CharField(help_text='Input correct answer', max_length=100, verbose_name='Answer')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(help_text='Input answer', max_length=100, verbose_name='Answer')),
                ('question', models.ForeignKey(help_text='Input question', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='questions.questions', verbose_name='Question')),
            ],
        ),
    ]
