from django.urls import reverse_lazy, reverse
from django.views.generic import UpdateView, DeleteView, DetailView, CreateView

from webapp.forms import ProductForm
from webapp.models import Product
from webapp.views.base_view import SearchView


class IndexView(SearchView):
    model = Product
    template_name = 'products/index.html'
    ordering = ['category', 'name']
    search_fields = ['name__icontains']
    paginate_by = 6
    context_object_name = 'products'


class ProductView(DetailView):
    model = Product
    template_name = 'products/product_view.html'
    context_object_name = 'products'


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_create.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.create_product") or \
               self.request.user == self.get_object().users


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'products/product_update.html'

    def get_success_url(self):
        return reverse('webapp:product_view', kwargs={'pk': self.object.pk})

    def has_permission(self):
        return self.request.user.has_perm("webapp.update_product") or \
               self.request.user == self.get_object().users


class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'products/product_delete.html'
    success_url = reverse_lazy('webapp:index')

    def has_permission(self):
        return self.request.user.has_perm("webapp.delete_product") or \
               self.request.user == self.get_object().users