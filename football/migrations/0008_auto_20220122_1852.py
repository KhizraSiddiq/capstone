from django.conf import settings
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('football', '0007_alter_thread_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='thread',
            name='downvote',
            field=models.ManyToManyField(related_name='thread_downvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='thread',
            name='upvote',
            field=models.ManyToManyField(related_name='thread_upvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='downvote',
            field=models.ManyToManyField(related_name='reply_downvote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reply',
            name='upvote',
            field=models.ManyToManyField(related_name='reply_upvote', to=settings.AUTH_USER_MODEL),
        ),
    ]
