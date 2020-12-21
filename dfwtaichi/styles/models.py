from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django_lifecycle import (
    LifecycleModelMixin,
    hook,
    BEFORE_UPDATE,
    AFTER_UPDATE,
    BEFORE_SAVE,
)

from model_utils.models import TimeStampedModel

# Create your models here.


class Style(LifecycleModelMixin, TimeStampedModel):
    title = models.CharField(
        "Title for TaiChi Style",
        max_length=90,
        unique=True,
        null=False,
        help_text="Short title for each TaiChi Style",
    )
    slug = models.SlugField(
        verbose_name="Style address", unique=True, default="Auto-generated"
    )
    description = models.TextField(verbose_name="Description", blank=True)
    wikipedia = models.URLField(verbose_name="Wikipedia page.", blank=True)
    # coverphotos = models.ManyToManyField(to="resource.Resource", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    # resources = models.ManyToManyField(to="resource.Resource", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "style"
        verbose_name_plural = "styles"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("styles.views.detail", kwargs={"slug": self.slug})

    @hook(BEFORE_SAVE, when="title", has_changed=True)
    def build_slug(self):
        newslug = slugify(self.title)
        if self.slug != newslug:
            self.slug = newslug


class SeriesLeaders(models.Model):
    leader = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    series = models.ForeignKey(to="Series", on_delete=models.CASCADE)
    primary = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    since = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.series.title}:{self.leader.name}"


class SeriesMembers(models.Model):
    member = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    series = models.ForeignKey(to="Series", on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    last_meeting = models.DateField("Last meeting attended", null=True)
    paid_through = models.DateField("Paid up through", null=True)
    since = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.series.title}:{self.member.name}"


class Series(LifecycleModelMixin, TimeStampedModel):
    title = models.CharField(
        "Title for TaiChi Series",
        max_length=90,
        unique=True,
        null=False,
        help_text="Short title for each TaiChi Series",
    )
    slug = models.SlugField(
        verbose_name="Series address", unique=True, default="Auto-generated"
    )
    style = models.ForeignKey("Style", on_delete=models.CASCADE)
    description = models.TextField(verbose_name="Description", blank=True)
    VISIBILITY_CHOICES = (
        ("public", "Show to public"),
        ("private", "Do not show to public"),
    )
    visibility = models.CharField(
        max_length=8,
        choices=VISIBILITY_CHOICES,
        default="private",
        help_text="Control whether guests can see this series.",
    )
    # take_role = models.BooleanField("Should the leader take the role", default=False)
    MEMBERSHIP_CHOICES = (
        ("open", "Open to all"),
        ("invite", "Leader must approve request to join"),
        ("closed", "Leader must add members"),
    )
    membership = models.CharField(
        max_length=8,
        choices=MEMBERSHIP_CHOICES,
        default="closed",
        help_text="Control how members are added to this series.",
    )
    leaders = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        help_text="Leaders for the series. Can administer this series.",
        through="SeriesLeaders",
        related_name="leaders",
        through_fields=("series", "leader"),
    )
    take_roll = models.BooleanField("Allow leader to take roll", default=False)
    members = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        help_text="Members of the series.",
        through="SeriesMembers",
        related_name="members",
        through_fields=("series", "member"),
    )

    def __str__(self):
        return f"{self.style.title}: {self.title}"

    @hook(BEFORE_SAVE, when="title", has_changed=True)
    def build_slug(self):
        newslug = slugify(self.title)
        if self.slug != newslug:
            self.slug = newslug


class MeetingAttendees(models.Model):
    attendee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    meeting = models.ForeignKey(to="Meeting", on_delete=models.CASCADE)
    present = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.meeting.series.title} on {self.meeting.day:%m/%d/%Y}, {self.member.name}"


class Meeting(LifecycleModelMixin, TimeStampedModel):
    series = models.ForeignKey(
        "Series", on_delete=models.CASCADE, help_text="Series master for this meeting."
    )
    location = models.ForeignKey(
        "locations.Location",
        on_delete=models.SET_NULL,
        null=True,
        help_text="Building where the meeting is held. Leave empty for virtual meetings.",
    )
    room = models.TextField("Directions to meeting room or virtual link", blank=True)
    day = models.DateField("Date of meeting")
    start = models.TimeField("Start time of the meeting")
    length = models.IntegerField("Minutes that the meeting lasts")
    message = models.TextField(
        "Notes to be included in email / text reminders", default=""
    )
    leader = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    attendees = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        help_text="List of attendees",
        through="MeetingAttendees",
        related_name="attendees",
        through_fields=("meeting", "attendee"),
    )

    def __str__(self):
        return f"{self.meeting.series.title} on {self.meeting.day:%m/%d/%Y} leader:{self.leader.name}"
