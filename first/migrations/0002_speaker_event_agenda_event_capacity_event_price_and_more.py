# Generated by Django 5.1.4 on 2025-04-12 10:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Speaker",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("title", models.CharField(max_length=100)),
                ("company", models.CharField(max_length=100)),
                ("bio", models.TextField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="speakers/"),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="agenda",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="capacity",
            field=models.IntegerField(default=100),
        ),
        migrations.AddField(
            model_name="event",
            name="price",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="event",
            name="what_you_will_learn",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name="EventRegistration",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("company", models.CharField(max_length=100)),
                ("job_title", models.CharField(max_length=100)),
                ("registration_date", models.DateTimeField(auto_now_add=True)),
                (
                    "event",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="registrations",
                        to="core.event",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="event",
            name="speakers",
            field=models.ManyToManyField(
                blank=True, related_name="events", to="core.speaker"
            ),
        ),
    ]
