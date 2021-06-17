from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    desc = models.CharField(max_length=255, verbose_name=_("Description"))
    price = models.PositiveIntegerField(verbose_name=_("Price"))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Product")
        verbose_name_plural = _("Products")


class Category(models.Model):
	name = models.CharField(max_length=255, verbose_name=_("Name"))

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = _("Category")
		verbose_name_plural = _("Categories")