from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('football', '0002_user_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='favorite',
        ),
    ]
