from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render
from django.core.mail import send_mail

from base.models import Product, Category, Comment


# Create your views here.
def send(request):
	send_mail(
		"Subject here",
		"Here is the message TEST TEST TEST",
		"beingp0z1t1v3@gmail.com",
		["flammeturk@gmail.com", "tap00k@mail.ru"],
		fail_silently=False,
	)
	return JsonResponse({"message": "EMAIL"})


def index(request):
	product = Product.objects.all().first()
	products = Product.objects.all()[0:3]
	categories = Category.objects.all()[0:3]

	return render(
		request,
		'home.html',
		{'product': product, 'products': products, 'categories': categories,}
	)


def category(request, id):
	category = Category.objects.get(id=id)
	products = Product.objects.filter(category=category)

	return render(
		request,
		'products-by-category.html',
		{
			"products": products,
			"category": category
		}
	)


def categories(request):
	categories = Category.objects.all()

	return render(
		request,
		'category.html',
		{'categories': categories}
	)


def products_list(request):
	products = Product.objects.all()

	return render(
		request,
		'products.html',
		{'products': products,}
	)


def product_detail_view(request, id):
	product = Product.objects.get(id=id)
	if request.method == 'POST':
		name = request.POST['name']
		comment = request.POST['message']
		email = request.POST['email']
		Comment.objects.create(
			product=product,
			title=name,
			email=email,
			content=comment
		)
		messages.success(request, 'Your comment now in moderation mode.')
	category = Category.objects.get(id=product.category.id)
	comments = Comment.objects.filter(product=product, status=True).order_by('-id')
	related_news = Product.objects.filter(category=category).exclude(id=id)

	return render(
		request,
		'detail.html',
		{
			'products': product,
			'related_news': related_news,
			'comments': comments
		}
	)

