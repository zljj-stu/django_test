# Generated by Django 4.2 on 2023-05-14 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0003_alter_peopleinfo_options_peopleinfo_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookinfo',
            old_name='pub_name',
            new_name='pub_date',
        ),
    ]