from django.db import models
import uuid

# Create your models here.
class CommonModel(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "%s" % self.name


class Categories(CommonModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    isactive = models.BooleanField(default=True)


class Products(CommonModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    category = models.ForeignKey('Categories', related_name='categories', on_delete=models.PROTECT)
    isactive = models.BooleanField(default=True)


class Items(CommonModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, null=False)
    product = models.ForeignKey('Products', related_name='products', on_delete=models.PROTECT)
    isactive = models.BooleanField(default=True)
    quantity = models.IntegerField(default=100)