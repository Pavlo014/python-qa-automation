import requests


class ProjectsAPI:

    def __init__(self, base_url, auth_headers):
        self.base_url = base_url
        self.auth_headers = auth_headers
        self.projects_url = f"{base_url}/projects"

    def create_project(self, title, users=None):
        # Создать новый проект
        payload = {"title": title}
        if users:
            payload["users"] = users

        response = requests.post(
            url=self.projects_url,
            headers=self.auth_headers,
            json=payload
        )
        return response

    def delete_project(self, project_id):
        # Удалить проект по ID
        url = f"{self.projects_url}/{project_id}"
        response = requests.delete(
            url=url,
            headers=self.auth_headers
        )
        return response

    def get_project(self, project_id):
        # Получить проект по ID
        url = f"{self.projects_url}/{project_id}"
        response = requests.get(
            url=url,
            headers=self.auth_headers
        )
        return response

    def update_project(self, project_id, data):
        # Обновить проект по ID (метод PUT)
        url = f"{self.projects_url}/{project_id}"
        response = requests.put(
            url=url,
            headers=self.auth_headers,
            json=data
        )
        return response
