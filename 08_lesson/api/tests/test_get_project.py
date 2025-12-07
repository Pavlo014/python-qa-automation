from api.projects_api import ProjectsAPI


class TestGetProject:
    """Тесты для метода GET /api-v2/projects/{id}"""

    def test_get_existing_project_positive(
            self, base_url, auth_headers, create_test_project
    ):
        """Позитивный тест: получение существующего проекта"""
        # Arrange
        project_id = create_test_project
        projects_api = ProjectsAPI(base_url, auth_headers)

        # Act
        response = projects_api.get_project(project_id)

        # Assert
        assert response.status_code == 200, (
            f"Ожидался код 200, получен {response.status_code}"
        )

        project_data = response.json()

        # Проверяем обязательные поля из реального ответа API
        # (основываемся на реальных данных, а не документации)
        assert "id" in project_data, "Ответ должен содержать поле 'id'"
        assert project_data["id"] == project_id, (
            f"ID должен быть {project_id}"
        )

        assert "title" in project_data, (
            "Ответ должен содержать поле 'title'"
        )
        assert "timestamp" in project_data, (
            "Ответ должен содержать поле 'timestamp'"
        )

        # Дополнительно: проверяем типы данных
        assert isinstance(project_data["id"], str), (
            "Поле 'id' должно быть строкой"
        )
        assert isinstance(project_data["title"], str), (
            "Поле 'title' должно быть строкой"
        )
        assert isinstance(project_data["timestamp"], (int, float)), (
            "Поле 'timestamp' должно быть числом"
        )

    def test_get_nonexistent_project_negative(
            self, base_url, auth_headers
    ):
        """Негативный тест: получение несуществующего проекта"""
        # Arrange
        projects_api = ProjectsAPI(base_url, auth_headers)
        fake_project_id = "00000000-0000-0000-0000-000000000000"

        # Act
        response = projects_api.get_project(fake_project_id)

        # Assert
        assert response.status_code == 404, (
            f"Ожидался код 404 для несуществующего проекта, "
            f"получен {response.status_code}"
        )
