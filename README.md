# URL_Storage
Данное API является решением тестового задания

## Запросы
Со скриптом можно взаимодействовать посредством http-запросов. 

### Создание новой пары ключ:значение в Redis:

Запрос:

    POST /?url=**Адрес сайта**

Ответ:

    { **Адрес сайта**: **Код** }

#### Пример:

Запрос:

    POST /?url=google.com

Ответ:

    { https://google.com: 8263489703957293 }
    
Либо, при условии, что была введена некорректная ссылка:
    
    { error: Была введена некорректная ссылка googlecom }
    
### Переход на сайт по известному коду:

Запрос:

    POST /**Код**

#### Пример:

Запрос:

    POST /8263489703957293

Ответ:

    **Учитывая предыдущий пример - переход на google.com**
    
Либо, при условии, что код, который вы ввели, не существует в базе:

    { error: 8263489703957293 кода не существует в базе данных }
