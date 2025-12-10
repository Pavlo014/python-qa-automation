@echo off
chcp 65001 >nul
echo =======================================
echo    Запуск автотестов с генерацией Allure
echo =======================================
echo.

REM 1. ОЧИСТКА: Удаляем старые результаты
if exist allure-results rmdir /s /q allure-results
if exist allure-report rmdir /s /q allure-report

REM 2. ЗАПУСК ТЕСТОВ
echo [1/3] Запуск тестов через pytest...
pytest --alluredir=allure-results --tb=short
if errorlevel 1 (
    echo Тесты завершились с ошибками.
    goto :end
)

REM 3. ГЕНЕРАЦИЯ ОТЧЕТА
echo [2/3] Генерация Allure-отчета...
allure generate allure-results -o allure-report --clean

echo [3/3] Отчет успешно создан!
echo.
echo =======================================
echo    ОТЧЕТ ДОСТУПЕН ПО АДРЕСУ:
echo    file:///%CD%/allure-report/index.html
echo =======================================
echo.
echo Чтобы открыть отчет в браузере, нажмите Enter.
echo Или закройте это окно.

REM 4. ОТКРЫТИЕ ОТЧЕТА (по желанию)
pause >nul
start "" "allure-report\index.html"

:end
pause