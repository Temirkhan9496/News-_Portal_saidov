from django.contrib.auth.models import User
from myapp.models import Author, Category, Post, PostCategory, Comment

# Создаем пользователей
user1 = User.objects.create_user('username1')
user2 = User.objects.create_user('username2')

# Создаем авторов
author1 = Author.objects.create(user=user1, rating=0)
author2 = Author.objects.create(user=user2, rating=0)

# Создаем категории
Category.objects.bulk_create([
    Category(name='Спорт'),
    Category(name='Политика'),
    Category(name='Образование'),
    Category(name='Наука'),
])

# Добавляем статьи и новости
post1 = Post.objects.create(author=author1, type='article', title='Статья 1', content='Текст статьи 1')
post2 = Post.objects.create(author=author2, type='article', title='Статья 2', content='Текст статьи 2')
post3 = Post.objects.create(author=author1, type='news', title='Новость 1', content='Текст новости 1')

# Присваиваем категории
post1.categories.add(Category.objects.get(name='Спорт'))
post2.categories.add(Category.objects.get(name='Политика'), Category.objects.get(name='Наука'))
post3.categories.add(Category.objects.get(name='Наука'))

# Создаем комментарии
Comment.objects.create(post=post1, user=user1, content='Комментарий к статье 1')
Comment.objects.create(post=post2, user=user2, content='Комментарий к статье 2')
Comment.objects.create(post=post3, user=user1, content='Комментарий к новости 1')
Comment.objects.create(post=post3, user=user2, content='Еще один комментарий к новости 1')

# Корректируем рейтинги
# (пример использования функций like и dislike)

# Обновляем рейтинги пользователей
# (пример использования update_rating())

# Выводим информацию по запросам