import uuid
from api.projects_api import ProjectsAPI


class TestUpdateProject:
    """Тесты для метода PUT /api-v2/projects/{id}"""

    def test_update_project_title_positive(
            self, base_url, auth_headers, create_test_project
    ):
        """Позитивный тест: успешное обновление названия проекта"""
        # Arrange
        project_id = create_test_project
        projects_api = ProjectsAPI(base_url, auth_headers)

        new_title = f"Updated Title {uuid.uuid4().hex[:6]}"
        update_data = {"title": new_title}

        # Act
        response = projects_api.update_project(project_id, update_data)

        # Assert
        assert response.status_code == 200, (
            f"Ожидался код 200, получен {response.status_code}"
        )

        response_data = response.json()
        assert "id" in response_data, "Ответ должен содержать поле 'id'"
        assert response_data["id"] == project_id, (
            f"ID должен быть {project_id}"
        )

    def test_update_project_invalid_id_negative(
            self, base_url, auth_headers
    ):
        """Негативный тест: обновление несуществующего проекта"""
        # Arrange
        projects_api = ProjectsAPI(base_url, auth_headers)
        fake_project_id = "00000000-0000-0000-0000-000000000000"
        update_data = {"title": "Some Title"}

        # Act
        response = projects_api.update_project(fake_project_id, update_data)

        # Assert
        assert response.status_code == 404, (
            f"Ожидался код 404 для несуществующего проекта, "
            f"получен {response.status_code}"
        )
