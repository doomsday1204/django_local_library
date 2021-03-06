# Generated by Django 3.2.4 on 2021-06-23 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_book_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='catalog.book'),
        ),
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('d', 'Maintenance'), ('o', 'On loan'), ('a', 'Available'), ('r', 'Reserved')], default='d', help_text='Book availability', max_length=1),
        ),
    ]
