from django.shortcuts import render, redirect, reverse
from django.views.generic import FormView
from . import models as content_models
from . import forms as content_forms


class AddContentView(FormView):

    """
    class: AddContentView
    author: haein
    des: Class Model to Create a Content
    date: 2020-06-10
    """

    model = content_models.Content
    template_name = "contents/create_content.html"
    fields = ("content_type",)
    form_class = content_forms.ContentTypeForm

    def form_valid(self, form):
        form.save()
        return redirect(reverse())
