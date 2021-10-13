from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from store.models import Order, Category, Product
from store.filters import ProductFilter
from store.mixins import CustomerRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


# @method_decorator(permission_required('users.is_customer'))
class HomeView(TemplateView):
    """Home view"""

    template_name = "store/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        customer = self.request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        context["cartItems"] = order.get_cart_items
        context["category"] = Category.objects.all()
        return context


class StoreView(DetailView):
    """Store detail view"""

    template_name = "store/store.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order, created = Order.objects.get_or_create(
            customer=self.request.user, complete=False
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


class DescriptionView(DetailView):
    template_name = "store/description.html"
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.filter(pk=self.kwargs["pk"])
        return context
