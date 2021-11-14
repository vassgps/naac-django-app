# Criterions/Models.py
from django.db import models
import jsonfield
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class AllStatus():
    STATUS = [("APPROVED", "Approved"), ("PENDING", "Pending"), ("REJECTED", "Rejected"),
              ("REVERTED", "Reverted"), ("OTHER", "Other"), ("VERIFIED", "Verified")]
    pass


class CriterionMaster(models.Model):
    date = models.DateField(null=True)
    department = models.ForeignKey('programs.Departments', on_delete=models.DO_NOTHING, null=True,
                                   related_name="crm_data", blank=True)
    program = models.ForeignKey('programs.Program', on_delete=models.DO_NOTHING, null=True, related_name="crm_data",
                                blank=True)  #
    paper = models.ForeignKey('programs.Subject', on_delete=models.DO_NOTHING, null=True, related_name="crm_data",
                              verbose_name="Course Name", blank=True)
    batch = models.ForeignKey('programs.Batch', on_delete=models.DO_NOTHING, null=True, related_name="crm_data",
                              verbose_name="Batch", blank=True)

    club = models.ForeignKey('programs.Clubs', on_delete=models.DO_NOTHING, null=True, related_name="crm_data",
                             verbose_name="Club", blank=True)
    criteria_manager = models.ForeignKey('adminapp.CriteriaManager', on_delete=models.DO_NOTHING, null=True,
                                         related_name="crm_data",
                                         verbose_name="Criteria Manager", blank=True)
    final_criteria = models.ForeignKey('adminapp.FinalCriteria', on_delete=models.DO_NOTHING, null=True,
                                       related_name="crm_data",
                                       verbose_name="Final Criteria", blank=True)
    criterion = models.CharField(max_length=20, null=True, blank=True)
    cr_index = models.CharField(max_length=20, null=True, blank=True)
    date2 = models.DateField(null=True, blank=True)
    date3 = models.DateField(null=True, blank=True)
    date4 = models.DateField(null=True, blank=True)
    date5 = models.DateField(null=True, blank=True)
    date6 = models.DateField(null=True, blank=True)
    url1 = models.URLField(null=True, blank=True)
    url2 = models.URLField(null=True, blank=True)
    file1 = models.FileField(upload_to='cr_file1/', null=True, blank=True)
    file2 = models.FileField(upload_to='cr_file1/', null=True, blank=True)
    file3 = models.FileField(upload_to='cr_file1/', null=True, blank=True)
    file4 = models.FileField(upload_to='cr_file1/', null=True, blank=True)
    file5 = models.FileField(upload_to='cr_file1/', null=True, blank=True)
    text1 = models.TextField(null=True, blank=True)
    text2 = models.TextField(null=True, blank=True)
    text3 = models.TextField(null=True, blank=True)
    text4 = models.TextField(null=True, blank=True)
    text5 = models.TextField(null=True, blank=True)
    text6 = models.TextField(null=True, blank=True)
    text7 = models.TextField(null=True, blank=True)
    text8 = models.TextField(null=True, blank=True)
    text9 = models.TextField(null=True, blank=True)
    text10 = models.TextField(null=True, blank=True)
    text11 = models.TextField(null=True, blank=True)
    text12 = models.TextField(null=True, blank=True)
    text13 = models.TextField(null=True, blank=True)
    text14 = models.TextField(null=True, blank=True)
    text15 = models.TextField(null=True, blank=True)
    text16 = models.TextField(null=True, blank=True)
    text17 = models.TextField(null=True, blank=True)
    text18 = models.TextField(null=True, blank=True)
    text19 = models.TextField(null=True, blank=True)
    text20 = models.TextField(null=True, blank=True)
    text21 = models.TextField(null=True, blank=True)
    text22 = models.TextField(null=True, blank=True)
    text23 = models.TextField(null=True, blank=True)
    text24 = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, null=True, blank=True, default="PENDING", choices=AllStatus.STATUS)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1, null=True, )
    is_active = models.BooleanField(default=False, null=True, blank=True)
    is_deleted = models.BooleanField(default=False, null=True, blank=True)
    jdoc = jsonfield.JSONField()

    def __str__(self):
        return str(self.criterion)
