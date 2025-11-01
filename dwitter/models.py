from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save # 1 "after save" signal
from django.dispatch import receiver
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )
# Profile model extends Django's built-in User model to support social features.
# Each Profile is linked to one User via a one-to-one relationship.
# The 'follows' field allows a Profile to follow other Profiles, enabling user-to-user connections.
# - "self" means the model relates to other instances of itself (Profile → Profile).
# - related_name="followed_by" lets us query who follows a given Profile.
# - symmetrical=False makes the relationship one-way (A can follow B without B following A).
# - blank=True allows a Profile to exist without following anyone initially.

    # Customize how Profile objects are displayed (especially in admin)
    def __str__(self):
        return self.user.username  # Show the username instead of "Profile object (1)"
    
@receiver(post_save, sender=User) #Hey Django, whenever a User is saved (created or updated), run this function right after.
def create_profile(sender, instance, created, **kwargs):
    if created:
        # Create a new Profile instance linked to the newly created User.
        user_profile = Profile(user=instance)
        
        # Save the Profile to the database so it gets an ID and can be referenced.
        user_profile.save()
        
        # Add the user's own profile to their follows list so they can see their own dweets.
        user_profile.follows.add(instance.profile)
        
        # Save again to persist the self-follow relationship.
        user_profile.save()
  