from django.db import models
from django.db.models.signals import pre_save
from django.utils.text import slugify
from django.conf import settings
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.contrib.auth import get_user_model


# def upload_location(instance, filename):
# 	file_path = 'blog/{author_id}/{title}-{filename}'.format(
# 				author_id=str(instance.author.id),title=str(instance.title), filename=filename)
# 	return file_path


class Record(models.Model):
    title                   = models.CharField(max_length=50, null=False, blank=False)
    item_name               = models.CharField(max_length=50, null=False, blank=False)
    inital_price            = models.IntegerField(null=True, blank=False)
    quantity                = models.IntegerField(null=False, blank=False)
    total_price             = models.IntegerField(null=False, blank=False)
    # image                 = models.ImageField(upload_to=upload_location, null=True, blank=True)
    date_published          = models.DateTimeField(auto_now_add=True, verbose_name="date published")
    author                  = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug                    = models.SlugField(blank=True, unique=True)

    def __str__(self):
        return self.title

    # @receiver(post_delete, sender=Record)
    # def submission_delete(sender, instance, **kwargs):
    #     instance.image.delete(False) 


# user records stored  
def get_record_count(user):
    return Record.objects.filter(author=user).count()


def pre_save_record_receiver(sender, instance, *args, **kwargs):

    author = instance.author
    record_count = get_record_count(author)
    print("Number of records created by the user:", record_count)
    instance.title="Order "+str(record_count)

    if not instance.slug:
        instance.slug = slugify(instance.author.username + "-" + instance.title)

    instance.total_price=instance.inital_price*instance.quantity 

       

pre_save.connect(pre_save_record_receiver, sender=Record)


