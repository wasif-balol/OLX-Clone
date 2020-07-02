from django.shortcuts import render
from .models import Product, ProductImages, Category
from django.core.paginator import Paginator
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404

# Create your views here.
def productlist(request, category_slug=None):
    category = None
    productList = Product.objects.all()
    category_list = Category.objects.annotate(total_products=Count('product'))
    if category_slug:
        category = get_object_or_404(Category,slug=category_slug)
        productList = productList.filter(Category=category)

    search_query = request.GET.get('q')
    if search_query:
        productList = productList.filter(
            Q(Name__icontains=search_query) |
            Q(Description__icontains=search_query) |
            Q(Condition__icontains=search_query) |
            Q(Brand__Brand_Name__icontains=search_query)|
            Q(Category__Category_Name__icontains=search_query)
        )

    paginator = Paginator(productList, 1)
    page = request.GET.get('page')
    productList = paginator.get_page(page)

    context = {"product_list": productList, "category_list": category_list, "category": category}
    return render(request, 'product/product_list.html', context)


def productdetail(request, product_slug):
    productDetail = get_object_or_404(Product, slug=product_slug)
    # print(productList)
    product_images = ProductImages.objects.filter(product=productDetail)
    context = {"product_detail": productDetail, "product_images": product_images}
    return render(request, 'product/product_detail.html', context)
