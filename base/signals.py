from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver


from .models import Product, Subscriber, Comment


def get_emails():
    emails = []
    for instance in Subscriber.objects.all():
        emails.append(instance.email)
    return emails


def get_product():
    product = Product.objects.latest('id')
    return product.id


@receiver(post_save, sender=Product)
def send_mass_mail(sender, instance, created, **kwargs):
    send_mail(
        "New product available!!!",
        "Dear user, we suggest you checking out new stuff!!!"
        "Here is the link to the product"
        "http://127.0.0.1:8000/detail/{}".format(get_product()),
        "beingp0z1t1v3@gmail.com",
        get_emails(),
    )


@receiver(post_save, sender=Comment)
def send_new_comment_mail(sender, instance, created, **kwargs):
    send_mail(
        "Verify new comment!",
        "Dear admin, you have a new comment, so check in as soon as possible",
        "beingp0z1t1v3@gmail.com",
        ["beingp0z1t1v3@gmail.com"]
    )