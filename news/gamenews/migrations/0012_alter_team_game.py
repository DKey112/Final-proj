# Generated by Django 4.1.5 on 2023-05-29 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("gamenews", "0011_alter_post_post_pic"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="game",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="gamenews.game",
                verbose_name="Discipline ",
            ),
        ),
    ]
