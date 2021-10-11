from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from store.models import Order, Category, Product
from store.filters import ProductFilter


class HomeView(LoginRequiredMixin, TemplateView):
    """Home view"""

    template_name = "store/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context["cartItems"] = order.get_cart_items
        context["category"] = Category.objects.all()
        return context


class Store(LoginRequiredMixin, DetailView):
    """Store detail view"""

    template_name = "store/store.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create(
            customer=self.request.user.customer, complete=False
        )
        context["cartItems"] = order.get_cart_items

        myFilter = ProductFilter(
            self.request.GET,
            queryset=Product.objects.filter(
                category=Category.objects.get(pk=self.kwargs["pk"])
            ),
        )
        context["products"] = myFilter.qs
        context["myFilter"] = myFilter
        return context
