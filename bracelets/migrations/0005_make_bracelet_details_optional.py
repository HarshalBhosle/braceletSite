from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bracelets', '0004_seed_demo_bracelets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bracelet',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='bracelet',
            name='material',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='bracelet',
            name='color',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bracelet',
            name='size',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='bracelet',
            name='stock',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
