from django.contrib.auth.models import User

from django.db import models



def ad_preview_directory_path(instance: 'Ad', filename: str):

    return 'ads/ad_{pk}/preview/{filename}'.format(
        pk=instance.pk,
        filename=filename,
    )



class Ad(models.Model):

    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    address = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    preview = models.ImageField(null=True, blank=True, upload_to=ad_preview_directory_path)
    phone = models.CharField(max_length=100, default=0)



def ad_images_directory_path(instance: 'Ad', filename: str):

    return 'ads/ad_{pk}/images/{filename}'.format(
        pk=instance.ad.pk,
        filename=filename,
    )



class AdImage(models.Model):

    ad = models.ForeignKey(Ad, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=ad_images_directory_path)

