from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy, reverse

from .models import Case
from .forms import (CaseUpdateForm,
                    # FollowUpForm, 
                    CommentForm)


class CasesListView(ListView):
    model = Case
    template_name = 'cases_list.html'

class CommentGet(DetailView): # new
    model = Case
    template_name = "case_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        return context

class CommentPost(SingleObjectMixin, FormView): # new
    model = Case
    form_class = CommentForm
    template_name = "case_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    def form_valid(self, form):
        comment = form.save(commit=False)
        form.instance.author = self.request.user
        comment.case = self.object
        comment.save()
        return super().form_valid(form)
    def get_success_url(self):
        case = self.get_object()
        return reverse("case_detail", kwargs={"slug": case.slug})

class CaseDetailView(View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)
    def get_context_data(self, **kwargs): # new
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        return context
    

class CaseUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Case
    # fields="__all__"
    template_name = 'case_edit.html'
    success_url = reverse_lazy("cases_list")
    form_class = CaseUpdateForm
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user

class CaseDeleteView(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Case
    template_name = 'case_delete.html'
    success_url = "/cases"
    def test_func(self): # new
        obj = self.get_object()
        return obj.author == self.request.user


class CaseCreateView(LoginRequiredMixin, CreateView): # new
    model = Case
    template_name = "case_new.html"
    # form_class
    fields=("title","cat","description","pretext","gender","location","job",
            "dwelling", "age", "marriage", "doctor", "source", "reliability",
            "setting", "PR","BP_S","BP_D","RR", "SPO2_O","SPO2_N","Temp",
            "cc","pi","pmh","drg", "sh", "fh", "alg","phe", "dat",
              "summary", "pdx", "act", "slug")
    def form_valid(self, form): # new
        form.instance.author = self.request.user
        return super().form_valid(form)





