# Adminapp/Models.py
from django.db import models
from django.contrib.auth import get_user_model
import jsonfield

User = get_user_model()


class CriteriaIndex(models.Model):
    MAJOR_ID = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"))

    CRITERIA_ID = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"), ("6", "6"), ("7", "7"), ("8", "8"),
                   ("9", "9"), ("10", "10"), ("11", "11"), ("12", "12"), ("13", "13"), ("14", "14"), ("15", "15"),
                   ("16", "16"),
                   ("17", "17"), ("18", "18"), ("19", "19"), ("20", "20"), ("1A", "1A"), ("1B", "1B"), ("2A", "2A"),
                   ("2B", "2B"), ("2C", "2C"), ("2D", "2D"), ("2E", "2E"), ("2F", "2F"), ("3A", "3A"), ("3B", "3B"),
                   ("3C", "3C"), ("3D", "3D"), ("3E", "3E"), ("3F", "3F"), ("3G", "3G"), ("3H", "3H"),
                   ("7A", "7A"), ("7B", "7B"),("7C", "7C"), ("7D", "7D"),)

    USER_SCOPES = (("CLUB", "Clubs"), ("NAAC_COD", "Naac Cordinator"), ("DEPT_COD", "Department"),
                   ("TEACHER", "Teacher"))


class MajourCriteria(models.Model):
    id_name = models.CharField(max_length=8, choices=CriteriaIndex.MAJOR_ID, default="0", unique=True)
    main_title = models.CharField(max_length=150, null=True, blank=True)
    # main_description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return str(self.id_name)


class SubCriteria(models.Model):
    majour = models.ForeignKey('MajourCriteria', on_delete=models.DO_NOTHING, null=True, related_name="sub")
    sub = models.CharField(max_length=8, choices=CriteriaIndex.CRITERIA_ID, default="0")
    id_name = models.CharField(max_length=8, blank=True, null=True)
    sub_title = models.TextField(null=True, blank=True)
    sub_description = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.name = (str(self.majour) + "_" + str(self.sub))
        super(SubCriteria, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.id_name)


class FinalCriteria(models.Model):
    majour = models.ForeignKey('MajourCriteria', on_delete=models.DO_NOTHING, null=True, related_name="final")
    sub = models.ForeignKey('SubCriteria', on_delete=models.DO_NOTHING, null=True, related_name="final")
    id_name = models.CharField(max_length=8, choices=CriteriaIndex.CRITERIA_ID, default="0")
    criteria = models.CharField(max_length=20, null=True, blank=True, unique=True)
    final_title = models.TextField(null=True, blank=True, verbose_name="Question for Data Collection")
    final_description = models.TextField(null=True, blank=True, verbose_name="Criterion Description or Help text")
    criteria_id = models.CharField(max_length=20, null=True, unique=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(null=True,blank=True, default=True)

    class Meta:
        ordering = ("criteria",)

    def save(self, *args, **kwargs):
        self.criteria_id = "c" + (str(self.sub) + "_" + str(self.id_name))
        super(FinalCriteria, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.criteria_id)


# Upload Photos of each event
class EventUploader(models.Model):
    date = models.DateField(null=True)
    title = models.CharField(max_length=225, null=True, blank=True)
    tags = models.TextField(null=True, blank=True)
    department = models.ForeignKey('programs.Departments', on_delete=models.DO_NOTHING, null=True,
                                   related_name="event_uploads", blank=True)
    images = models.FileField(upload_to='event_uploads/', null=True, blank=True)
    files = models.FileField(upload_to='event_uploads/', null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return str(self.title)


class CriteriaManager(models.Model):
    criteria = models.CharField(max_length=15, null=True, unique=True)
    ADMIN = models.BooleanField(default=False, null=True, blank=True)
    STAFF = models.BooleanField(default=False, null=True, blank=True)
    NAAC_COD = models.BooleanField(default=False, null=True, blank=True)
    DEPT_COD = models.BooleanField(default=False, null=True, blank=True)
    TEACHER = models.BooleanField(default=False, null=True, blank=True)
    CLUB = models.BooleanField(default=False, null=True, blank=True)
    OTHER = models.BooleanField(default=False, null=True, blank=True)
    assigned_clubs = jsonfield.JSONField()
    ordering = models.FloatField(default=0)
    cr_index = models.IntegerField(null=True, default=0)
    is_active = models.BooleanField(null=True, default=False)
    is_enabled = models.BooleanField(null=True, default=True)

    def __str__(self):
        return str(self.criteria)


'''     
# Deleted Models in this version

# class MenuItems(models.Model):
#     criteria_id = models.OneToOneField('FinalCriteria', on_delete=models.DO_NOTHING, null=True, related_name="menu")
#     assigned_role = models.ManyToManyField('UserScopes', related_name="menu_roles", default="TEACHER")
#     assigned_clubs = models.ManyToManyField('programs.Clubs', related_name="assigned_clubs")
#     ordering = models.IntegerField(default=0)
#     is_active = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.criteria_id)

# class UserScopes(models.Model):
#     name = models.CharField(max_length=30, null=True)
#     role = models.CharField(max_length=40, null=True, blank=True)
#     is_active = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.name)
'''
