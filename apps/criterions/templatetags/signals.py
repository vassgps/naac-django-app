# code
from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from ..models import CriterionMaster


@receiver(post_save, sender=CriterionMaster)
def create_program_code(sender, instance, created, **kwargs):
    if created:
        criteria = str(instance.criterion)
        if criteria in ["c1_1_2", "c1_2_2", "c1_3_4", "c2_1_2", "c2_5_1", "c2_6_1", "c2_6_3"]:
            code = instance.program.code
            instance.text1 = code
            instance.save()

        elif criteria in ["c1_1_3", "c1_2_1"]:
            code = instance.paper.code
            instance.text1 = code
            instance.save()

# @receiver(post_save, sender=CriterionMaster)
# def create_paper(sender, instance, **kwargs):
#     instance.profile.save()
