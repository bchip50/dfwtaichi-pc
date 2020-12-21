from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField


class User(AbstractUser):
    """Default user for dfwtaichi."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    gmail = models.EmailField(
        "GMail address",
        blank=True,
        max_length=200,
        help_text="GMail address, used for authentication.",
    )
    phone = PhoneField("home phone.", blank=True)
    cell = PhoneField(
        "cell phone", blank=True, help_text="Number used for text notifications"
    )
    bio = models.TextField("TaiChi biography.", blank=True)
    leaderFlag = models.BooleanField("User is a leader", default=False)
    sponsor = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        null=True,
        help_text="User who applied leader designation.",
    )

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
