from django.shortcuts import get_object_or_404, render

from .models import Category, Product

# ürünlerin hepsini (kategoriden bağımsız olarak) listelenmesi için 
# bilgilerin döndüğü fonksiyon
def product_all(request):
    products = Product.objects.prefetch_related("product_image").filter(is_active=True)
    return render(request, "catalogue/index.html", {"products": products})

# ürünlerin listelenirken bir kategoriye bağımlı olarak 
# listelendiği kısım
def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(
        category__in=Category.objects.get(name=category_slug).get_descendants(include_self=True)
    )
    return render(request, "catalogue/category.html", {"category": category, "products": products})

# üzerine tıklandığından ürün detaylarını listelendiği kısım
def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, is_active=True)
    return render(request, "catalogue/single.html", {"product": product})
