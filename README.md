# URL_Storage
Данное API является решением тестового задания

## Запросы
Со скриптом можно взаимодействовать посредством http-запросов. 

### Создание новой пары ключ:значение в Redis:

Запрос:

    POST /url?url=**Адрес сайта**

Ответ:

    { **Адрес сайта**: **Код** }

#### Пример:

Запрос:

    POST /code?code=google.com

Ответ:

    { google.com: 8263489703957293 }
    
Либо, при условии, что была введена некорректная ссылка:
    
    { "Была введена некорректная ссылка": "google" }
    
### Переход на сайт по известному коду:

Запрос:

    POST /url?url=**Код**

#### Пример:

Запрос:

    POST /code?code=8263489703957293

Ответ:

    **Учитывая предыдущий пример - переход на google.com**
    
Либо, при условии, что код, который вы ввели, не существует в базе:

    { Данного кода не существует в базе данных: 8263489703957293 }
