# Generated by Django 4.0.2 on 2022-02-12 15:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("demo", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name="milestonecomment",
            name="milestone",
        ),
        migrations.DeleteModel(
            name="IssueComment",
        ),
        migrations.DeleteModel(
            name="MilestoneComment",
        ),
        migrations.AddField(
            model_name="issue",
            name="tags",
            field=models.ManyToManyField(
                related_name="issues", related_query_name="issue", to="demo.Tag"
            ),
        ),
    ]
