# Generated by Django 4.1.3 on 2022-12-13 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='product',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='details',
        ),
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('other', 'Разное'), ('electronics', 'Электроника'), ('books', 'Книги'), ('stationery', 'Канцтовары')], default='other', max_length=50, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание товара'),
        ),
        migrations.AlterField(
            model_name='product',
            name='balance',
            field=models.PositiveIntegerField(default=1, verbose_name='Остаток'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Стоимость'),
        ),
    ]
