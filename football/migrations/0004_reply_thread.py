from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    dependencies = [
        ('football', '0003_remove_user_favorite'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thread',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=50)),
                ('forum', models.CharField(choices=[('ARS', 'Arsenal'), ('AST', 'Aston Villa'), ('CHE', 'Chelsea'), ('EVE', 'Everton'), ('LIV', 'Liverpool'), ('MCI', 'Man City'), ('MUN', 'Man United'), ('NEW', 'Newcastle'), ('NOR', 'Norwich'), ('TOT', 'Tottenham'), ('WOL', 'Wolverhampton'), ('BUR', 'Burnley'), ('LEI', 'Leicester City'), ('SOU', 'Southampton'), ('LEE', 'Leeds United'), ('WAT', 'Watford'), ('CRY', 'Crystal Palace'), ('BHA', 'Brighton Hove'), ('BRE', 'Brentford'), ('WHU', 'West Ham'), ('GEN', 'general')], max_length=20)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('op', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='op', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=500)),
                ('time', models.DateTimeField(auto_now_add=True)),
                ('downvote', models.ManyToManyField(related_name='downvote', to=settings.AUTH_USER_MODEL)),
                ('poster', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='poster', to=settings.AUTH_USER_MODEL)),
                ('thread', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='thread', to='football.thread')),
                ('upvote', models.ManyToManyField(related_name='upvote', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
