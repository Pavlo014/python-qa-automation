import pytest
import uuid


class TestProjectsCreate:

    @pytest.fixture
    def api_client(self, base_url, auth_headers):
        from api.projects_api import ProjectsAPI
        return ProjectsAPI(base_url, auth_headers)

    @pytest.fixture
    def unique_project_title(self):
        return f"Тестовый проект {uuid.uuid4().hex[:8]}"

    # ========== Позитивный тест: успешное создание проекта ==========

    def test_create_project_success(self, api_client, unique_project_title):
        response = api_client.create_project(unique_project_title)

        assert response.status_code == 201, (
            f"Ожидался статус 201, получен {response.status_code}. "
            f"Ответ: {response.text}"
        )

        response_data = response.json()
        assert "id" in response_data, "В ответе должно быть поле 'id'"
        assert response_data["id"], "Поле 'id' не должно быть пустым"

    # ========== Негативный тест: создание проекта без авторизации ==========

    def test_create_project_without_auth(self, api_client,
                                         unique_project_title):
        original_headers = api_client.auth_headers

        try:
            api_client.auth_headers = {"Content-Type": "application/json"}

            response = api_client.create_project(unique_project_title)

            assert response.status_code in [401, 403], (
                f"Ожидался статус 401 или 403, "
                f"получен {response.status_code}. "
                f"Ответ: {response.text}"
            )

        finally:
            api_client.auth_headers = original_headers
