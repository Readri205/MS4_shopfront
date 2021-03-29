from django.db import models


class Type(models.Model):

    class Meta:
        verbose_name_plural = "Types"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Country(models.Model):

    class Meta:
        verbose_name_plural = "Countries"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    flag_url = models.URLField(
        max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name

    def get_flag_url(self):
        return self.flag_url


class Appellation(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Variety(models.Model):

    class Meta:
        verbose_name_plural = "Varieties"

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    type = models.ForeignKey(
        'Type', null=True, blank=True, on_delete=models.SET_NULL)
    country = models.ForeignKey(
        'Country', null=True, blank=True, on_delete=models.SET_NULL)
    appellation = models.ForeignKey(
        'Appellation', null=True, blank=True, on_delete=models.SET_NULL)
    variety = models.ForeignKey(
        'Variety', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(
        max_length=254, null=True, blank=True)
    product = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(
        max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.product
