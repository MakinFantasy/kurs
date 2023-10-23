from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from base import views

urlpatterns = [
	path('', views.index, name='index'),
	path('send', views.send, name='send'),
	path('products', views.products_list, name='products'),
	path('category/<int:id>', views.category, name='category'),
	path('categories', views.categories, name='categories'),
	path('detail/<int:id>', views.product_detail_view, name='details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
