from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('football', '0004_reply_thread'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='content',
            field=models.TextField(default='some contnet', max_length=500),
            preserve_default=False,
        ),
    ]
