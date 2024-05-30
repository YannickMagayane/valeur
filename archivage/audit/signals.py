from django.db.models.signals import pre_save, post_save, post_delete
from django.dispatch import receiver
from django.contrib.contenttypes.models import ContentType
from .models import LogEntry
from archive.models import ArchiveCategory,Archive,PhysicalDocument

def create_log_entry(instance, action_flag, change_message=''):
    LogEntry.objects.create(
        user=instance.user if hasattr(instance, 'user') else None,
        content_type=ContentType.objects.get_for_model(instance),
        object_id=instance.pk,
        object_repr=str(instance),
        action_flag=action_flag,
        change_message=change_message,
    )

@receiver(post_save, sender=ArchiveCategory)
def log_product_save(sender, instance, created, **kwargs):
    action_flag = 'create' if created else 'update'
    create_log_entry(instance, action_flag)

@receiver(post_delete, sender=ArchiveCategory)
def log_product_delete(sender, instance, **kwargs):
    create_log_entry(instance, 'delete')

@receiver(post_save, sender=ArchiveCategory)
def log_category_save(sender, instance, created, **kwargs):
    action_flag = 'create' if created else 'update'
    create_log_entry(instance, action_flag)

@receiver(post_delete, sender=Archive)
def log_category_delete(sender, instance, **kwargs):
    create_log_entry(instance, 'delete')

@receiver(post_save, sender=Archive)
def log_supermarket_save(sender, instance, created, **kwargs):
    action_flag = 'create' if created else 'update'
    create_log_entry(instance, action_flag)

@receiver(post_delete, sender=Archive)
def log_supermarket_delete(sender, instance, **kwargs):
    create_log_entry(instance, 'delete')


@receiver(post_delete, sender=PhysicalDocument)
def log_category_delete(sender, instance, **kwargs):
    create_log_entry(instance, 'delete')

@receiver(post_save, sender=PhysicalDocument)
def log_supermarket_save(sender, instance, created, **kwargs):
    action_flag = 'create' if created else 'update'
    create_log_entry(instance, action_flag)

@receiver(post_delete, sender=PhysicalDocument)
def log_supermarket_delete(sender, instance, **kwargs):
    create_log_entry(instance, 'delete')
