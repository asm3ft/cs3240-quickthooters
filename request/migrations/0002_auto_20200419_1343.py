# Generated by Django 3.0.2 on 2020-04-19 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='location',
            field=models.CharField(choices=[('Alderman Library', 'Alderman Library'), ('Clark Hall', 'Clark Hall'), ('Clemons Library', 'Clemons Library'), ('Rice Hall', 'Rice Hall'), ('Thorton Stacks', 'Thorton Stacks')], max_length=1000),
        ),
        migrations.AlterField(
            model_name='request',
            name='subject',
            field=models.CharField(choices=[('Accounting & Finance', 'Accounting & Finance'), ('Architecture', 'Architecture'), ('Arts & Humanities', 'Arts & Humanities'), ('Biological Science', 'Biological Science'), ('Chemical Engineering', 'Chemical Engineering'), ('Chemistry', 'Chemistry'), ('Computer Sience & Information Systems', 'Computer Sience & Information Systems'), ('Economics', 'Economics'), ('Electrical Engineering', 'Electrical Engineering'), ('Environmental Science', 'Environmental Science'), ('Geography', 'Geography'), ('History', 'History'), ('Law', 'Law'), ('Material Science', 'Material Science'), ('Mathematics', 'Mathematics'), ('Medecine', 'Medecine'), ('Modern Languages', 'Modern Languages'), ('Nursing', 'Nursing'), ('Philosophy', 'Philosophy'), ('Physics', 'Physics'), ('Psychology', 'Psychology'), ('Religion', 'Religion'), ('Sociology', 'Sociology'), ('Other', 'Other')], max_length=50),
        ),
    ]
