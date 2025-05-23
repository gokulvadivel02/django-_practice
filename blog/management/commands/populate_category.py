from typing import Any
from blog.models import Category
from django.core.management.base import BaseCommand    

class Command(BaseCommand):
    help = 'this command insert category data'

    def handle(self, *arg: Any, **option: Any):
        # deiete existing data 
        Category.objects.all().delete()

        categories = ['sports', 'education', 'trending', 'testing', 'development']
       
        for category_name in categories:
            Category.objects.create(names = category_name)

        self.stdout.write(self.style.SUCCESS('completed inserting data'))
        