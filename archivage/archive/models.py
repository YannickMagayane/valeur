from django.db import models
from auditlog.registry import auditlog
import uuid
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from audit.models import LogEntry



class ArchiveCategory(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

auditlog.register(ArchiveCategory)

class PhysicalDocument(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

auditlog.register(PhysicalDocument)

class Archive(models.Model):
    code = models.CharField(max_length=50,blank=True)
    category = models.ForeignKey(ArchiveCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    nom_propietaire = models.CharField(max_length=255)
    adresse = models.CharField(max_length=255)
    document = models.FileField(upload_to='documents/')
    scanned_date = models.DateField(auto_now_add=True)
    date_registered = models.DateField(auto_now_add=True)
    physical_document = models.ForeignKey(PhysicalDocument, on_delete=models.CASCADE)
    _deleted_by = None  # Champ non persistant pour stocker l'utilisateur

    @property
    
    
    @property
    def year(self):
        return self.date_registered.year

    def __str__(self):
        return self.code

    def save(self, *args, **kwargs):
        if self.code == "":
            self.code = str(uuid.uuid4()).replace('-', '').upper()[:10]
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self._deleted_by = kwargs.pop('user', None)
        super().delete(*args, **kwargs)
        
auditlog.register(Archive)




@receiver(post_delete, sender=Archive)
def log_archive_deletion(sender, instance, **kwargs):
    user = instance._deleted_by
    if user:
        content_type = ContentType.objects.get_for_model(instance)
        LogEntry.objects.create(
            user=user,
            content_type=content_type,
            object_id=instance.pk,
            object_repr=str(instance),
            action_flag='delete',
            change_message='Archive deleted'
        )