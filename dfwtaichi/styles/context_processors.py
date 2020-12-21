from dfwtaichi.styles.models import Style


def style_menu(request):
    return {"style_menu": Style.objects.values("title", "slug")}
