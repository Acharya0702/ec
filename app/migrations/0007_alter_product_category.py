# Generated by Django 4.2.5 on 2023-10-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0006_wishlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.CharField(
                choices=[
                    ("SV", "SUV"),
                    ("HB", "Hatchback"),
                    ("SD", "Sedan"),
                    ("MV", "MUV"),
                    ("LX", "Luxury"),
                ],
                max_length=2,
            ),
        ),
    ]
