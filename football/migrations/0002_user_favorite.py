from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('football', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='favorite',
            field=models.CharField(max_length=3, null=True),
        ),
    ]
