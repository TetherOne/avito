Функционал сайта:


При входе на главную страницу пользователь видит список объявлений.
Объявление состоит из: главной фотографии, названия, цены, адреса, никнейма пользователя и ссылки «подробнее», нажав на нее
можно увидеть дополнительную информацию об объявлении (дату создания, дополнительные фото, номер тлф продавца), также есть возможность посмотреть профиль пользователя,
где есть список его объявлений (редактировать или удалять чужие объявления нельзя).

Незарегестрированный пользователь может только просматривать объявления, для создания объявлений придется зарагестрироваться

Также на главной странице есть поля поиска, создания объявления, кнопка "ваш профиль" и кнопка "выйти" (которая меняется на кнопку "войти" в зависимости от того,
аутентифицирован пользователь или нет).

При создании объявления заполняется форма с полями (название, описание, цена, адрес, номер тлф, фото). 
Также реализована логика редактирования объявления (можно изменять люое поля и менять или добавлять фотографии).
При нажатии кнопки «Выйти» - пользователь разлогинивается и остается на главной странице.
При нажатии кнопки «Ваш профиль» - пользователя переводит на свой профиль, где есть список его объявлений, там он может их редактировать или удалять.

Ссылка на сайт: http://82.97.240.119/avito/
========================================================================================================================================================================


- Сайт написан на Django 4.0 с использованием базы данных SQLite
- Для публикации сайта использовалась связка Nginx + Gunicorn
