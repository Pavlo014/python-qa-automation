import os
import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def base_url():
    """Базовый URL API"""
    url = os.getenv("YOUGILE_BASE_URL")
    assert url, "YOUGILE_BASE_URL не указан в .env"
    return url


@pytest.fixture(scope="session")
def auth_headers():
    """Заголовки авторизации"""
    token = os.getenv("YOUGILE_API_TOKEN")
    assert token, "YOUGILE_API_TOKEN не указан в .env"

    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }


@pytest.fixture
def create_test_project(base_url, auth_headers):
    """Создает временный проект для тестов и удаляет его после"""
    import requests
    import uuid

    # Создаем уникальное название для проекта
    project_title = f"Test Project {uuid.uuid4().hex[:8]}"
    project_data = {"title": project_title}

    # Создаем проект
    response = requests.post(
        f"{base_url}/projects",
        headers=auth_headers,
        json=project_data
    )

    # Проверяем успешное создание
    error_msg = f"Не удалось создать тестовый проект: {response.text}"
    assert response.status_code == 201, error_msg

    # Получаем ID созданного проекта
    project_id = response.json()["id"]

    # Возвращаем ID проекта (тест выполняется здесь)
    yield project_id

    # Удаляем проект после теста
    cleanup_response = requests.delete(
        f"{base_url}/projects/{project_id}",
        headers=auth_headers
    )

    # Логируем результат удаления
    if cleanup_response.status_code != 200:
        msg = f"Не удалось удалить тестовый проект {project_id}"
        print(f"Предупреждение: {msg}")
