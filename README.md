# ЗАПУСК ПРИЛОЖЕНИЯ НА BASH:
### Способ 1:
(для запуска необходим предустановленный Docker)

`$ docker run --rm -p 8000:8000 nesteatea/some_portal:latest`

Для просмотра работы веб-приложения открыть в браузере страницу http://0.0.0.0:8000/home/
Для остановки ввести комбинацию Ctrl+C


### Способ 2:
Открыть bash-терминал в корневой папке проекта.
Ввести

`$ pip3 install -r requirements.txt`  
`$ python3 manage.py runserver`

Для просмотра работы веб-приложения открыть в браузере страницу http://0.0.0.0:8000/home/
Для остановки ввести комбинацию Ctrl+C

# ОПИСАНИЕ РАБОТЫ ПРИЛОЖЕНИЯ
На главной странице приложения http://0.0.0.0:8000/home/ можно увидеть все публикации(они разбиты на несколько страниц 
по 5 штук на каждой с помощью пагинатора) и последние 4 новости(более поздние новости не отображаются, но их можно 
посмотреть в базе данных или в админке). Около каждой новости или публикации(далее - пост) выведено количество голосов 
плюсов и минусов и их общее количество.

На индивидуальной странице каждого поста можно, аналогично, увидеть количество голосов, поставить свой голос и оставить 
комментарий. За комментарии можно голосовать также, как и за посты. Каждый пользователь(авторизованный) может
проголосовать за каждый пост лишь один раз. Так как авторизацию реализовывать не требовалось, для определения
пользователей я воспользовалась встроенной в админку таблицей пользователей.

Данные для входа для одного из пользователей:  
  логин: admin  
  пароль: 111  

# ОПИСАНИЕ АРХИТЕКТУРЫ
**some_portal/manage.py** - основной скрипт всего приложения

**some_portal/some_portal** - пакет проекта, здесь находятся конфиги и главный URL-контроллер, который может передавать управления URL-контроллерам приложений, которые, в свою очередь, вызовут нужные отображения

**some_portal/home** - пакет приложения, реализующего основной бизнес-процесс: выставление голосов и комментариев к постам

**some_portal/home/view.Home** - класс вью для главной страницы

**some_portal/home/view.DetailPost** - родительский класс для классов вью индивидуальных страниц постов. Так как логика
новости и публикации ничем не отличается, было решено наследовать эти классы от одного во избежание дублирования кода.
