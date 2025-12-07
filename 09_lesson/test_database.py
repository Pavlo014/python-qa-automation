from database import QADatabase


class TestDatabaseOperationsFinal:

    # === Тест 1: Добавление новой сущности ===

    def test_add_subject(self, db_session):
        # Arrange
        db = QADatabase(db_session)
        subject_count_before = db.get_subject_count()
        test_subject_title = "Тестовая автоматизация"

        # Act - добавляем новый предмет
        new_subject_id = db.create_subject(test_subject_title)

        # Assert - проверяем, что предмет добавился
        subject_count_after = db.get_subject_count()
        expected_count = subject_count_before + 1
        assert subject_count_after == expected_count, (
            f"Ожидалось {expected_count} предметов, "
            f"получено {subject_count_after}"
        )

        # Проверяем данные добавленного предмета
        added_subject = db.get_subject(new_subject_id)
        assert added_subject is not None, (
            f"Предмет с ID {new_subject_id} не найден"
        )
        assert added_subject["subject_title"] == test_subject_title, (
            f"Ожидалось '{test_subject_title}', "
            f"получено '{added_subject['subject_title']}'"
        )

        # Cleanup - удаляем тестовые данные
        db.delete_subject(new_subject_id)
        subject_count_final = db.get_subject_count()
        assert subject_count_final == subject_count_before, (
            "Количество предметов после очистки "
            "не совпадает с исходным"
        )

    # === Тест 2: Изменение существующей сущности ===

    def test_update_subject(self, db_session):
        # Arrange
        db = QADatabase(db_session)
        original_title = "Исходный предмет"
        updated_title = "Обновленный предмет"

        # Создаем тестовый предмет
        test_subject_id = db.create_subject(original_title)

        # Проверяем, что предмет создан
        subject_before_update = db.get_subject(test_subject_id)
        assert subject_before_update is not None
        assert subject_before_update["subject_title"] == original_title

        # Act - изменяем предмет
        updated_rows = db.update_subject(test_subject_id, updated_title)
        assert updated_rows == 1, f"Обновлено {updated_rows} строк вместо 1"

        # Assert - проверяем изменения
        updated_subject = db.get_subject(test_subject_id)
        assert updated_subject is not None, (
            "Предмет не найден после обновления"
        )
        assert updated_subject["subject_title"] == updated_title, (
            f"Ожидалось '{updated_title}', "
            f"получено '{updated_subject['subject_title']}'"
        )
        assert updated_subject["subject_title"] != original_title

        # Cleanup - удаляем тестовые данные
        db.delete_subject(test_subject_id)

    # === Тест 3: Удаление сущности ===

    def test_delete_subject(self, db_session):
        # Arrange
        db = QADatabase(db_session)
        subject_count_before = db.get_subject_count()
        test_subject_title = "Предмет для удаления"

        # Создаем тестовый предмет
        test_subject_id = db.create_subject(test_subject_title)

        # Проверяем, что предмет создан
        subject_after_creation = db.get_subject(test_subject_id)
        assert subject_after_creation is not None, "Предмет не создан"
        assert subject_after_creation["subject_title"] == test_subject_title

        # Act - удаляем предмет
        deletion_result = db.delete_subject(test_subject_id)

        # Assert - проверяем удаление
        assert deletion_result is True, "Предмет не был удален"

        # Проверяем, что предмет больше не существует
        deleted_subject = db.get_subject(test_subject_id)
        assert deleted_subject is None, (
            "Предмет все еще существует после удаления"
        )

        # Проверяем количество предметов
        subject_count_after = db.get_subject_count()
        assert subject_count_after == subject_count_before, (
            f"Ожидалось {subject_count_before} предметов, "
            f"получено {subject_count_after}"
        )

    # === Тест 4: Работа со связанными данными (студентами) ===

    def test_create_and_delete_student(self, db_session):
        # Arrange
        db = QADatabase(db_session)

        # Создаем тестовый предмет
        test_subject_title = "Python Programming"
        test_subject_id = db.create_subject(test_subject_title)

        # Тестовые данные студента
        test_user_id = 99999  # Используем большой ID для избежания конфликтов
        test_level = "Intermediate"
        test_education_form = "Online"

        # Act - создаем студента
        student_created = db.create_student(
            user_id=test_user_id,
            level=test_level,
            education_form=test_education_form,
            subject_id=test_subject_id
        )
        assert student_created is True, "Студент не был создан"

        # Assert - проверяем создание
        created_student = db.get_student(test_user_id)
        assert created_student is not None, "Студент не найден"
        assert created_student["user_id"] == test_user_id
        assert created_student["level"] == test_level
        assert created_student["education_form"] == test_education_form
        assert created_student["subject_id"] == test_subject_id

        # Cleanup - удаляем тестовые данные
        student_deleted = db.delete_student(test_user_id)
        assert student_deleted is True, "Студент не был удален"

        subject_deleted = db.delete_subject(test_subject_id)
        assert subject_deleted is True, "Предмет не был удален"

        # Проверяем удаление
        deleted_student = db.get_student(test_user_id)
        assert deleted_student is None, "Студент все еще существует"

        deleted_subject = db.get_subject(test_subject_id)
        assert deleted_subject is None, "Предмет все еще существует"
