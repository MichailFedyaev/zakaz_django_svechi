from django.shortcuts import render
from django.http import HttpResponse, HttpResponseForbidden
from .models import Candles
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy


class CandleListView(ListView):
    model = Candles

    def get_queryset(self):
        return Candles.objects.all()


class CandleCreateView(CreateView):
    model = Candles
    #form_class = ProductForm
    success_url = reverse_lazy("catalog:product_list")

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class CandleDetailView(DetailView):
    model = Candles
