from django.shortcuts import render, redirect, reverse
from django.views.generic import View, FormView
from . import models as content_models
from . import forms as content_forms
from users import models as user_models
from teams import models as team_models
from projects import models as project_models
from core import models as core_models


class AddContentTypeView(View):

    """
    class: AddContenTypeView
    author: haein
    des: Class Model to Add Type of a Content
    date: 2020-06-10
    """

    def get(self, *args, **kwargs):
        return render(self.request, "contents/type_content.html")

    def post(self, *args, **kwargs):
        content_type = self.request.POST.get("content_type")
        if content_type is not None:
            return redirect(reverse("contents:add_file_content"))

        else:
            return render(self.request, "contents/type_content.html")


class AddContentFileView(View):

    """
    class: AddContentFileView
    author: haein
    des: Class Model to Add File of a Content
    date: 2020-06-14
    """

    def get(self, *args, **kwargs):
        return render(self.request, "contents/file_content.html")

    def post(self, *args, **kwargs):
        files = self.request.FILES
        if files is not None:
            return redirect(reverse("contents:add_info_content"))
        else:
            return render(self.request, "contents/file_content.html")


class AddContentInfoView(View):

    """
    class: AddContentInfoView
    author: haein
    des: Class Model to Add Info of a Content
    date: 2020-06-14
    """

    def get(self, *args, **kwargs):
        teams = team_models.Team.objects.filter(members=self.request.user)
        genres = core_models.Genre.objects.all()
        context = {"teams": teams, "genres": genres}
        return render(self.request, "contents/info_content.html", context)

    def post(self, *args, **kwargs):
        print(f"POST's DATA: {self.request.POST}")
        teams = team_models.Team.objects.filter(members=self.request.user)
        try:
            self.request.POST["project"]
            return redirect(reverse("contents:add_check_content"))
        except Exception:
            print(self.request.POST)
            selected_team = int(self.request.POST["team"])
            projects = project_models.Project.objects.filter(team=selected_team)
            print(projects)
            form = content_forms.ContentForm(self.request.POST)
            context = {"teams": teams, "form": form, "projects": projects}
            return render(self.request, "contents/info_content.html", context)


class AddContentCheckView(View):

    """
    class: AddContentCheckView
    author: haein
    des: Class Model to Check Info of a Content
    date: 2020-06-15
    """

    def get(self, *args, **kwargs):
        form = content_forms.ContentForm()
        context = {"form": form}
        return render(self.request, "contents/check_content.html", context)

    def post(self, *args, **kwargs):
        form = content_forms.ContentForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            return redirect(reverse("core:home"))
        else:
            context = {"form": form}
            return render(self.request, "contents/check_content.html", context)


# class AddContentTypeView(FormView):

#     """
#     class: AddContenTypeView
#     author: haein
#     des: Class Model to Add Type of a Content
#     date: 2020-06-10
#     """

#     model = content_models.Content
#     template_name = "contents/type_content.html"
#     fields = ("content_type",)
#     form_class = content_forms.ContentForm

#     def form_valid(self, form):
#         self.request.session["content_type"] = form.cleaned_data["content_type"]
#         return redirect(reverse("contents:add_file_content"))


# class AddContentFileView(FormView):

#     """
#     class: AddContentFileView
#     author: haein
#     des: Class Model to Add File of a Content
#     date: 2020-06-14
#     """

#     model = content_models.Content
#     template_name = "contents/file_content.html"
#     fields = "content_file"
#     form_class = content_forms.ContentForm

#     def get_form_kwargs(self):
#         """Return the keyword arguments for instantiating the form."""
#         kwargs = {
#             "initial": self.get_initial(),
#             "prefix": self.get_prefix(),
#         }
#         if self.request.method in ("POST", "PUT"):
#             kwargs.update(
#                 {"data": self.request.POST, "files": self.request.FILES,}
#             )
#         return kwargs

#     def get_form(self, form_class=None):
#         """Return an instance of the form to be used in this view."""
#         if form_class is None:
#             form_class = self.get_form_class()
#         return form_class(**self.get_form_kwargs())

#     def form_valid(self, form):
#         form.save(commit=False)
#         return redirect(reverse("contents:add_info_content"))

#     def form_invalid(self, form):
#         print(form.errors)
#         return self.render_to_response(
#             self.get_context_data(request=self.request, form=form)
#         )
