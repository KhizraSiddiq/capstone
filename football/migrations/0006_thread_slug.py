from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('football', '0005_thread_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='slug',
            field=models.SlugField(null=True),
        ),
    ]
