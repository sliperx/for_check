# Generated by Django 4.1.3 on 2023-05-23 06:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0042_alter_incomecash_categories_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='moneybox',
            old_name='box_target',
            new_name='target',
        ),
        migrations.RemoveField(
            model_name='moneybox',
            name='box_sum',
        ),
        migrations.AddField(
            model_name='moneybox',
            name='date_record',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата создания записи'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moneybox',
            name='sum',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=19, verbose_name='Сумма'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moneybox',
            name='categories',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='api.categories', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='moneybox',
            name='date',
            field=models.DateField(verbose_name='Дата записи'),
        ),
    ]