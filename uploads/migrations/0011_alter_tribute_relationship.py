# Generated by Django 5.0.4 on 2024-05-02 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0010_imagepost_caption'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribute',
            name='relationship',
            field=models.CharField(blank=True, choices=[('', 'Select relationship status'), ('son', 'son'), ('brother', 'brother'), ('sister', 'sister'), ('husband', 'husband'), ('daughter', 'daughter'), ('son_inlaw', 'son inlaw'), ('daughter_inlaw', 'daughter inlaw'), ('grand_child', 'grand child'), ('sibling', 'sibling'), ('friends', 'friends'), ('family_friend', 'family friend'), ('friends_of_children', 'friends of children')], max_length=30, null=True),
        ),
    ]
