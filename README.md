# BeautyTime
Cosmetology master app

Скворцов Александр Владимирович, гр. 153503

# Функциональные требования проекта:

Гость:

    - Создание аккаунта
    - Возможность чтения информации о доступных услугах, процедурах

Пользователь:
    
    - Аутентификация
    - Авторизация
    - Чтение информации о доступных услугах, процедурах
    - Создание записи/заказа услуги или продукта
    - Редактирование записи/заказа
    - Отмена записи/заказа

Сотрудник:
    
    - Создание записи/заказа услуги или продукта
    - Редактирование записи/заказа
    - Отмена записи/заказа
    - Создание записей о поставках
    - Добавление продуктов/услуг

Администратор:

    - Журналирование действий пользователя
    - Полный доступ к CRUD операциям приложения


# Описание сущностей базы данных

1. Клиенты (Client) – таблица, содержащая общую информацию о клиентах, которые уже пользовались услугами и соответственно о роли Customer:

Содержит связи:

    • “Многие ко многим” с услугами
    • “Один ко многим” с отзывами
    • “Один ко многим” с записями
    • “Многие ко многим” с продажами
Содержит поля:

	- Имя (first_name) – строка, до 20 символов, не пустая
	- Фамилия (second_name) – строка, до 20 символов, не пустая
	- Отчество (surname) – строка, до 20 символов
	- Номер телефона (phone) – строка (макет +375(29)ХХХ-ХХ-ХХ), 17 символов, не пустая
	- Электронная почта (email) – строка, до 30 симоволов

2. Услуги (Service) – таблица всех услуг, предоставляемых мастеров:

Содержит связи:

    • “Многие ко многим” с клиентами
    • “Один ко многим” с записями

Содержит поля:

	- Название услуги (name) – строка до 30 символов, не пустая
	- Внутреннее (краткое) название услуги (alias) – строка до 10 символов, не пустая, уникальное
	- Описание (description) – текстовое поле
	- Стоимость (cost) – целочисленное поле, не пустое

3. Расписание (Schedule) – таблица, содержащая информацию о записях клиентов на процедуры:

Содержит поля:

	- ID клиента (Foreign Key, связь с таблицей "Клиенты") – связь один к одному (одна запись в расписании для одного клиента)
	- Дата и время начала (start_datetime) – поле датавремя, не пустое
	- Длительность (duration) – длительность процедуры
	- ID услуги (Foreign Key, связь с таблицей "Услуги") - для оптимизации можно сделать один ко многим (одна запись в расписании ко многим услугам, услуги могли были быть выполнены одна за одной)

4. Сотрудники (Staff) – таблица содержащая информацию о роли Staff, чтобы сотрудники могли авторизоваться в приложение:

Содержит поля:

	- Имя (first_name) – строка, до 20 символов, не пустая
	- Фамилия (second_name) – строка, до 20 символов, не пустая
	- Должность (job_title) – строка, до 20 символов, не пустая
	- Номер телефона (phone) – строка (макет +375(29)ХХХ-ХХ-ХХ), 17 символов, не пустая
	- Электронная почта (email) – строка, до 30 симоволов


5. Записи о выполненных услугах (shedule_archive) – таблица-архив для уже прошедших записей, MTM для клиентов и записей:

Содержит поля:

	- ID клиента (Foreign Key, связь с таблицей "Клиенты") 
	- ID сотрудника (Foreign Key, связь с таблицей "Сотрудники")
	- ID услуги (Foreign Key, связь с таблицей "Услуги")
	- Дата и время выполнения
	- Примечания

6. Продукты (product) – таблица имеющихся в прайсе продуктов для продажи (таких как косметика и т.п.):

Содержит поля:

	- Название продукта - строка, до 20 символов, не пустая
	- Внутреннее (краткое) название услуги (alias) – строка до 10 символов, не пустая, уникальное
	- Описание (description) – текстовое поле
	- Стоимость (cost) – целочисленное поле, не пустое

7. Запасы (in_stock) – таблица указания количества тех или иных продуктов:

Содержит поля:

	- ID продукта (Foreign Key, связь с таблицей "Продукты") – связь один к одному
	- Количество(quantity) - целочисленное поле, не пустое
	- Дата пополнения (date) – датавремя последнего пополнения

8. Продажи (sale) – таблица, содержащая информацию о проданных продуктах:

Содержит поля:

	- ID продукта (Foreign Key, связь с таблицей "Продукты")
	- ID клиента (Foreign Key, связь с таблицей "Клиенты")
	- Количество(quantity) - целочисленное поле, не пустое
	- Дата и время продажи(date) – датавремя продажи

9. Отзывы (reviews) – таблица отзывов:

Содержит связи:

    • “Один к одному” с клиентом

Содержит поля:

	- ID клиента (Foreign Key, связь с таблицей "Клиенты")
	- Текст отзыва (comment) – текстовое поле
	- Рейтинг (от 1 до 5) (raiting) – целочисленное поле, не пустое

10. Финансы (Finance) – таблица, содержащая информацию о доходах/расходах:

Содержит поля:

	- Тип (доход или расход) (type) – строка, не пустая
	- Сумма (sum) – дробное число, не пустое
	- Дата и время (date) – датавремя, не пустое
	- Описание (description) – текстовое поле