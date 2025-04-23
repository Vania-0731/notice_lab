# news/management/commands/seed_data.py
from django.core.management.base import BaseCommand
from news.models import Category, Reporter, Article, Tag
from django.contrib.auth.models import User
from random import choice, randint

class Command(BaseCommand):
    help = "Genera datos de ejemplo para la aplicación News"

    def handle(self, *args, **kwargs):
        # Crear categorías de ejemplo
        categories = ["Technology", "Sports", "Health", "Politics", "Entertainment", "Science"]
        created_categories = []

        for category_name in categories:
            category, created = Category.objects.get_or_create(name=category_name)
            created_categories.append(category)
            self.stdout.write(self.style.SUCCESS(f'Categoría "{category_name}" creada'))

        # Crear reporteros de ejemplo
        for i in range(5):
            user = User.objects.create_user(
                username=f'user{i}',
                first_name=f'First{i}',
                last_name=f'Last{i}',
                email=f'user{i}@example.com',
                password='password123'
            )
            reporter = Reporter.objects.create(user=user, bio=f'Bio del reportero {i}')
            self.stdout.write(self.style.SUCCESS(f'Reportero "{user.username}" creado'))

        # Crear etiquetas de ejemplo
        tags = ["Technology", "Football", "Health", "Politics", "Music", "Space"]
        created_tags = []

        for tag_name in tags:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            created_tags.append(tag)
            self.stdout.write(self.style.SUCCESS(f'Etiqueta "{tag_name}" creada'))

        # Crear artículos de ejemplo
        for i in range(10):
            article = Article.objects.create(
                title=f'Test Article {i+1}',
                slug=f'test-article-{i+1}',
                content=f'Contenido del artículo de prueba número {i+1}.',
                reporter=choice(Reporter.objects.all()),
                category=choice(created_categories),
                status=choice(['published', 'draft']),
            )
            # Agregar algunas etiquetas al artículo
            article.tags.add(choice(created_tags))
            article.save()
            self.stdout.write(self.style.SUCCESS(f'Artículo "{article.title}" creado'))

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo generados exitosamente'))
