from django.shortcuts import render
from ..models import Category, Page


def index(request):
    ### Troquei por id, pois likes estava dando pau no sistema
    category_list = Category.objects.order_by('-id')[:5]
    # print('Categorias: ', len(category_list), ':', category_list)

    page_list = Page.objects.order_by('-views')[:5]
    # print('Páginas: ', len(page_list), ':', page_list)

    context_dict = {'categories': category_list, 'pages': page_list}
    return render(request, 'rango/index.html', context=context_dict)
