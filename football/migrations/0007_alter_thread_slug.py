from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('football', '0006_thread_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thread',
            name='slug',
            field=models.SlugField(unique=True),
        ),
    ]
