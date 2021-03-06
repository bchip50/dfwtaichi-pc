from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model

from dfwtaichi.users.forms import UserChangeForm, UserCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserChangeForm
    add_form = UserCreationForm
    fieldsets = (
        (
            "User",
            {
                "fields": (
                    "name",
                    "gmail",
                    "phone",
                    "cell",
                    "favorite_style",
                    "city",
                    "leaderFlag",
                    "sponsor",
                )
            },
        ),
    ) + tuple(auth_admin.UserAdmin.fieldsets)
    list_display = ["username", "name", "leaderFlag"]
    search_fields = ["name"]
