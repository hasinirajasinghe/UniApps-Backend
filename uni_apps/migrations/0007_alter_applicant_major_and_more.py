# Generated by Django 4.1.1 on 2022-09-11 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_apps', '0006_alter_application_intended_start'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='major',
            field=models.CharField(choices=[('UNDC', 'Undecided'), ('CSCI', 'Computer Science'), ('CHEM', 'Chemistry'), ('ENGI', 'Engineering'), ('BIOL', 'Biology'), ('PHYS', 'Physics'), ('MATH', 'Mathematics'), ('ITEC', 'Information Technology'), ('BMAN', 'Business Management'), ('FIAC', 'Finance and Accounting'), ('EDUC', 'Education'), ('KNPT', 'Kinesiology and Physical Therapy'), ('ESCI', 'Environmental Science'), ('FOLA', 'Foreign Languages'), ('DANC', 'Dance'), ('MUSI', 'Music'), ('PRAR', 'Performing Arts'), ('AGSC', 'Agricultural Sciences'), ('CUAR', 'Culinary Arts'), ('FIPH', 'Film and Photography'), ('FDNU', 'Food and Nutrition')], default='UNDC', max_length=4),
        ),
        migrations.AlterField(
            model_name='application',
            name='intended_major',
            field=models.CharField(choices=[('UNDC', 'Undecided'), ('CSCI', 'Computer Science'), ('CHEM', 'Chemistry'), ('ENGI', 'Engineering'), ('BIOL', 'Biology'), ('PHYS', 'Physics'), ('MATH', 'Mathematics'), ('ITEC', 'Information Technology'), ('BMAN', 'Business Management'), ('FIAC', 'Finance and Accounting'), ('EDUC', 'Education'), ('KNPT', 'Kinesiology and Physical Therapy'), ('ESCI', 'Environmental Science'), ('FOLA', 'Foreign Languages'), ('DANC', 'Dance'), ('MUSI', 'Music'), ('PRAR', 'Performing Arts'), ('AGSC', 'Agricultural Sciences'), ('CUAR', 'Culinary Arts'), ('FIPH', 'Film and Photography'), ('FDNU', 'Food and Nutrition')], default='UNDC', max_length=4),
        ),
    ]
