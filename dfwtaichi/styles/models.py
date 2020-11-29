from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils.text import slugify
from django_lifecycle import LifecycleModel, hook, BEFORE_UPDATE, AFTER_UPDATE, BEFORE_SAVE
from model_utils.models import TimeStampedModel

# Create your models here.

class Style(TimeStampedModel):
    title = models.CharField(
        "Title for TaiChi Style",
        max_length=90,
        unique=True, null=False,
        help_text="Short title for each TaiChi Style",
    )
    slug = models.SlugField(verbose_name="Style address", unique=True, null=False)
    description = models.TextField(verbose_name="Description", blank=True)
    wikipedia = models.URLField(verbose_name="Wikipedia page.", blank=True)
    #coverphotos = models.ManyToManyField(to="resource.Resource", on_delete=models.CASCADE)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL
    )
    #resources = models.ManyToManyField(to="resource.Resource", on_delete=models.CASCADE)

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
