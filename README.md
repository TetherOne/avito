Описание функционала сайта:

Главная страница:

    Поле поиска по объявлениям
    Список объявлений, включая главную фотографию, название, цену, адрес, никнейм пользователя и ссылку "подробнее".
    По нажатию на ссылку "подробнее" открывается дополнительная информация об объявлении (дата создания, дополнительные фотографии, номер телефона продавца).
    Возможность просмотра профиля пользователя со списком его объявлений (редактирование или удаление чужих объявлений недоступно).


2. Создание и редактирование объявлений:

  - Форма заполняется полями: название, описание, цена, адрес, номер телефона, фото.
  - Реализована возможность редактирования объявлений (изменение любых полей, добавление или изменение фотографий).
  - Редактировать или удалять чужие объявления нельзя


3. Взаимодействие с профилем пользователя:

  - При нажатии кнопки "Выйти" пользователь разлогинивается и остается на главной странице.
  - При нажатии кнопки "Ваш профиль" пользователь переходит на свой профиль, где может просматривать и редактировать свои объявления.
  - Пользователь может просматривать чужие профили и видеть их объявления



Техническая информация:

- Сайт разработан на Django 4.0 с использованием базы данных PostgreSQL.
- Реализовано API (полный CRUD) для взаимодействия с сущностями.
- Профили пользователей кэшируются при помощи Redis.
- Для работы сайта используется Nginx для статики и Gunicorn для динамического контента.


Ссылка на сайт: http://82.97.240.119/avito/
