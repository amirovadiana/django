import csv

from django.core.management.base import BaseCommand
from django.utils.text import slugify

from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            p = Phone(id=phone['id'], name=phone['name'],
                    price=phone['price'], image=phone['image'],
                    release_date=phone['release_date'],
                    lte_exists = phone['lte_exists'],
                    slug=slugify(phone['name']))
            p.save()


            # TODO: Добавьте сохранение модели


            # for phone in phones:
            #     p = Phone(id=phone['id'], name=phone['name'],
            #         price=phone['price'], image=phone['image'],
            #         release_date=phone['release_date'],
            #         lte_exists = phone['lte_exists'])
            #     p.save()