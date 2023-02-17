# Тестовые задания на стажировку в greenatom

Для развертывания проекта на локальной машине требуется клонировать репозиторий и сделать следующие шаги.

 - python -m venv .venv - развернуть виртуальное окружение
 - sourse .venv/bin/activate - активировать на unix-подобных системах 
 - .venv/Scripts/Activate - активировать на windows
 - pip install -r requirements.txt - установить зависимости.

## 1 задание

#### Какие шаги следует предпринять, если пользователь сообщит о том, что API возвращает ему ошибку 500?

Ошибка 500 это ошибка сервера. Она может возникнуть из-за недоступности или проблем с базой данных или в самом сервисе. 

 - проверить лог сервера для выявление ошибки;
 - нужно проверить файл .htaccess с настройками для работы сервера;
 - проверить наличие ошибки при соединении с БД;
 - если api имеет зависимости от сторонних api, то проверить доступность
зависимых сервисов;
 - отключить плагины или компоненты;
 - возможно требуется увеличить объем оперативной памяти.

---

## 2 задание

#### Какие ты видишь проблемы в следующем фрагменте кода? Как его следует исправить? Исправь ошибку и перепиши код с использованием типизации.

```python
def create_handlers(callback):
    handlers = []
    for step in range(5):
    # добавляем обработчики для каждого шага
        handlers.append(lambda: callback(step))
    return handlers

def execute_handlers(handlers):
    # добавляем обработчики для каждого шага(шаги от 0 до 4)
    for handler in handlers:
        handler()

```

[Решение 2 задачи](tasks/task_2.py)

 - использование переменной 5 в range не очень приемлемо при написании кода. 
Лучше поместить в атрибут функции.
 - использование lambda функции избыточно в теле цикла. Задачу можно решить через функцию partial из functools.

---

## 3 задание

#### Сколько HTML-тегов в коде главной страницы сайта [greenatom.ru](https://greenatom.ru/)? Сколько из них содержит атрибуты? Необходимо написать скрипт на Python, который выводит ответы на вопросы выше.

[Решение 3 задачи](tasks/task_3.py)

---

## 4 задание

#### Написать функцию на Python, которая возвращает текущий публичный IP-адрес компьютера(например, с использованием сервиса ifconfig.me).

[Решение 4 задачи](tasks/task_4.py)

---

## 5 задание

#### Написать функцию на python, выполняющую сравнение версии. Условия:

- Return -1 if version A is older than version B
- Return 0 if version A and B are equivalent
- Return 1 if version A is newer than version B
- Each subsection is supposed to be interpreted as a number, therefore 1.10 > 1.1.

[Решение 5 задачи](tasks/task_5.py)

---

## Для тестирования нужно перейти по ссылке ниже и запустить скрипт.  

[Тестирование](task/test.py)

---