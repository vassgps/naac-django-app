# Generated by Django 3.2 on 2021-10-28 02:03

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CriteriaIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='CriteriaManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criteria', models.CharField(max_length=15, null=True, unique=True)),
                ('ADMIN', models.BooleanField(blank=True, default=False, null=True)),
                ('STAFF', models.BooleanField(blank=True, default=False, null=True)),
                ('NAAC_COD', models.BooleanField(blank=True, default=False, null=True)),
                ('DEPT_COD', models.BooleanField(blank=True, default=False, null=True)),
                ('TEACHER', models.BooleanField(blank=True, default=False, null=True)),
                ('CLUB', models.BooleanField(blank=True, default=False, null=True)),
                ('OTHER', models.BooleanField(blank=True, default=False, null=True)),
                ('assigned_clubs', jsonfield.fields.JSONField(default=dict)),
                ('ordering', models.FloatField(default=0)),
                ('cr_index', models.IntegerField(default=0, null=True)),
                ('is_active', models.BooleanField(default=False, null=True)),
                ('is_enabled', models.BooleanField(default=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventUploader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('title', models.CharField(blank=True, max_length=225, null=True)),
                ('tags', models.TextField(blank=True, null=True)),
                ('images', models.FileField(blank=True, null=True, upload_to='event_uploads/')),
                ('files', models.FileField(blank=True, null=True, upload_to='event_uploads/')),
                ('status', models.BooleanField(blank=True, default=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MajourCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7')], default='0', max_length=8, unique=True)),
                ('main_title', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SubCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('2C', '2C'), ('2D', '2D'), ('2E', '2E'), ('2F', '2F'), ('3A', '3A'), ('3B', '3B'), ('3C', '3C'), ('3D', '3D'), ('3E', '3E'), ('3F', '3F'), ('3G', '3G'), ('3H', '3H')], default='0', max_length=8)),
                ('id_name', models.CharField(blank=True, max_length=8, null=True)),
                ('sub_title', models.TextField(blank=True, null=True)),
                ('sub_description', models.TextField(blank=True, null=True)),
                ('majour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='sub', to='adminapp.majourcriteria')),
            ],
        ),
        migrations.CreateModel(
            name='FinalCriteria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_name', models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12'), ('13', '13'), ('14', '14'), ('15', '15'), ('16', '16'), ('17', '17'), ('18', '18'), ('19', '19'), ('20', '20'), ('1A', '1A'), ('1B', '1B'), ('2A', '2A'), ('2B', '2B'), ('2C', '2C'), ('2D', '2D'), ('2E', '2E'), ('2F', '2F'), ('3A', '3A'), ('3B', '3B'), ('3C', '3C'), ('3D', '3D'), ('3E', '3E'), ('3F', '3F'), ('3G', '3G'), ('3H', '3H')], default='0', max_length=8)),
                ('criteria', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('final_title', models.TextField(blank=True, null=True)),
                ('final_description', models.TextField(blank=True, null=True)),
                ('criteria_id', models.CharField(blank=True, max_length=20, null=True, unique=True)),
                ('keywords', models.TextField(blank=True, null=True)),
                ('is_active', models.BooleanField(blank=True, default=True, null=True)),
                ('majour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='final', to='adminapp.majourcriteria')),
                ('sub', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='final', to='adminapp.subcriteria')),
            ],
            options={
                'ordering': ('criteria',),
            },
        ),
    ]