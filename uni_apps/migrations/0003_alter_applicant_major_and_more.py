# Generated by Django 4.1 on 2022-09-05 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni_apps', '0002_alter_applicant_major_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicant',
            name='major',
            field=models.CharField(choices=[('CSCI', 'Computer Science'), ('CHEM', 'Chemistry'), ('ENGI', 'Engineering'), ('BIOL', 'Biology'), ('PHYS', 'Physics'), ('MATH', 'Mathematics'), ('ITEC', 'Information Technology'), ('BMAN', 'Business Management'), ('FIAC', 'Finance and Accounting'), ('EDUC', 'Education'), ('KNPT', 'Kinesiology and Physical Therapy'), ('ESCI', 'Environmental Science'), ('FOLA', 'Foreign Languages'), ('DANC', 'Dance'), ('MUSI', 'Music'), ('PRAR', 'Performing Arts'), ('AGSC', 'Agricultural Sciences'), ('CUAR', 'Culinary Arts'), ('FIPH', 'Film and Photography'), ('FDNU', 'Food and Nutrition'), ('UNDC', 'Undecided')], default='UNDC', max_length=4),
        ),
        migrations.AlterField(
            model_name='application',
            name='intended_major',
            field=models.CharField(choices=[('CSCI', 'Computer Science'), ('CHEM', 'Chemistry'), ('ENGI', 'Engineering'), ('BIOL', 'Biology'), ('PHYS', 'Physics'), ('MATH', 'Mathematics'), ('ITEC', 'Information Technology'), ('BMAN', 'Business Management'), ('FIAC', 'Finance and Accounting'), ('EDUC', 'Education'), ('KNPT', 'Kinesiology and Physical Therapy'), ('ESCI', 'Environmental Science'), ('FOLA', 'Foreign Languages'), ('DANC', 'Dance'), ('MUSI', 'Music'), ('PRAR', 'Performing Arts'), ('AGSC', 'Agricultural Sciences'), ('CUAR', 'Culinary Arts'), ('FIPH', 'Film and Photography'), ('FDNU', 'Food and Nutrition'), ('UNDC', 'Undecided')], default='UNDC', max_length=4),
        ),
    ]
