from web_shop.database.models import Category, SubCategory, Manufacturer


def filter_output(request):
    page = int(request.GET.get('page', 1))
    per_page = int(request.GET.get('per_page', 8))
    category = request.GET.get('category', '')
    sub_category = request.GET.get('sub_category', '')
    manufacturer = request.GET.get('manufacturer', '')
    return {
        'page': page,
        'per_page': per_page,
        'category': category,
        'sub_category': sub_category,
        'manufacturer': manufacturer,
    }


def objects_for_nav():
    """
    Returns a trio of objects:
    categories, sub_categories, manufacturers

    """

    categories = sorted(Category.objects.all(), key=lambda item: item.name)

    sub_categories = sorted(
        SubCategory.objects.all(),
        key=lambda item: item.name
    )

    manufacturers = sorted(
        Manufacturer.objects.all(),
        key=lambda item: item.name
    )

    return categories, sub_categories, manufacturers
