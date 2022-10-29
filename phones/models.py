from django.db import models
from django.utils.text import slugify


class Phone(models.Model):
    # TODO: Добавьте требуемые поля
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    image = models.URLField()
    price = models.IntegerField()
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=100)

    def save_slug(self):
        self.slug = slugify(self.name, allow_unicode=True)
        super().save()
