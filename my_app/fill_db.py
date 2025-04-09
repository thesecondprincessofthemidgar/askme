# my_app/management/commands/fill_db.py

from django.core.management.base import BaseCommand
from django.utils import timezone
import random
from datetime import timedelta
from models import User, Profile, Tag, Question, Answer, QuestionLike, AnswerLike

class Command(BaseCommand):
    help = 'Fill database with test data'

    def add_arguments(self, parser):
        parser.add_argument('ratio', type=int, help='Ratio to generate data')

    def handle(self, *args, **options):
        ratio = options['ratio']

        # Генерация пользователей
        users = []
        for _ in range(ratio):
            username = f'user{random.randint(1, 9999)}'
            email = f'{username.lower()}@example.com'
            password = 'password123'
            
            # Проверяем существование пользователя с таким именем
            if User.objects.filter(username=username).exists():
                continue
            
            user = User.objects.create(
                username=username,
                email=email,
                password=password
            )
            users.append(user)

        # Генерация профилей
        for _ in range(ratio):
            # Выбираем случайного пользователя из тех, кто был создан
            user = random.choice(users)
            Profile.objects.create(
                user=user,
                avatar=f'path/to/avatar/{random.randint(1, 9999)}.jpg'
            )

        # Генерация тегов
        tags = [f'tag_{i}' for i in range(ratio)]

        # Генерация вопросов
        for _ in range(ratio * 10):
            question = Question.objects.create(
                title=f'Question {_}',
                content=f'Content for question {_}',
                author=random.choice(users),
                created_at=timezone.now() - timedelta(days=random.randint(1, 30))
            )
            question.tags.add(random.sample(tags, random.randint(1, 5)))

        # Генерация ответов
        for _ in range(ratio * 100):
            answer = Answer.objects.create(
                content=f'Response {_}',
                author=random.choice(users),
                question=Question.objects.order_by('?').first(),
                created_at=timezone.now() - timedelta(hours=random.randint(1, 24))
            )

        # Генерация оценок вопросов
        for _ in range(ratio * 200):
            QuestionLike.objects.create(
                user=random.choice(users),
                question=Question.objects.order_by('?').first(),
                created_at=timezone.now() - timedelta(days=random.randint(1, 365))
            )

        # Генерация оценок ответов
        for _ in range(ratio * 200):
            AnswerLike.objects.create(
                user=random.choice(users),
                answer=Answer.objects.order_by('?').first(),
                created_at=timezone.now() - timedelta(hours=random.randint(1, 24))
            )

        self.stdout.write(self.style.SUCCESS(f'Database filled with {ratio} users'))
