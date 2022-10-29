import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # TODO: Добавьте сохранение модели
            cur_phone = Phone(phone['id'],
                              phone['name'],
                              phone['image'],
                              phone['price'],
                              phone['release_date'],
                              phone['lte_exists'])
            cur_phone.save()
            cur_phone.save_slug()
