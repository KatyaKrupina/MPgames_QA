# Тестирование веб-системы MPgames

## Настройка окружения
Для запуска веб-приложения должен быть установлен docker.
Команды для запуска:

    docker pull qapropeller/qa-battle
    docker run -d -p 8080:8080 qapropeller/qa-battle:latest

Приложение будет доступно по ссылке: http://localhost:8080

## Запуск тестов
Для запуска тестов должно быть настроено окружение согласно requirements.txt

Команда для запуска тестов:

    pytest --alluredir=allure-results


## Получение отчета allure

Allure отчет генерится командой:

    allure serve allure-results
