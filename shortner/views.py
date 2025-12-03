from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from .forms import URLForm
from .models import URL


def home_view(request):
    short_url = None
    form = URLForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        original = form.cleaned_data["original_url"]
        # simple duplicate avoidance. If a same original_url exists, reuse slug
        obj, created = URL.objects.get_or_create(original_url=original)
        # if created, model.save() will generate slug
        if created:
            # ensure object has slug saved
            obj.save()
        short_url = request.build_absolute_uri(
            reverse("shortener:redirect", kwargs={"slug": obj.slug}))
    context = {
        "form": form,
        "short_url": short_url,
    }
    return render(request, "shortner/home.html", context)


def redirect_view(request, slug):
    url_obj = get_object_or_404(URL, slug=slug)
    # increment clicks count and redirect
    url_obj.clicks = url_obj.clicks + 1
    url_obj.save(update_fields=["clicks"])
    return HttpResponseRedirect(url_obj.original_url)
