from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver

from .models import Post

# For counting posts related games 
@receiver(post_save, sender=Post)
def games_amount_post_save(sender, instance, created, *args, **kwargs):
    if created:
        instance.game.post_amount += 1
        instance.game.save()


@receiver(post_delete, sender=Post)
def games_amount_post_delete(sender, instance, *args, **kwargs):
    instance.game.post_amount -= 1
    instance.game.save()