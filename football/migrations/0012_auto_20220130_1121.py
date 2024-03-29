from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('football', '0011_auto_20220123_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='poster',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_reply', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='thread',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reply', to='football.thread'),
        ),
        migrations.AlterField(
            model_name='thread',
            name='op',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='op_thread', to=settings.AUTH_USER_MODEL),
        ),
    ]
