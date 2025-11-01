from django.db import models
from django.contrib.auth.models import User


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

