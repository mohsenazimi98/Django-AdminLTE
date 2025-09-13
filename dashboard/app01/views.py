from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from utils.menu import register_menu
from utils.menu_ids import APP_IDS

@login_required
@register_menu(label="آپ 01", app_id="app_01")
def app01(request):
    context = {}
    return render(request, "app01/app01.html", context)


@login_required
@register_menu(label="آپ 01_1", parent="app_01")
def app01_1(request):
    context = {}
    return render(request, "app01/app01_1.html", context)
