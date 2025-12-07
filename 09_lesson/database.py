from sqlalchemy import text


class QADatabase:

    def __init__(self, session):
        self.session = session
        self._test_id_base = 10000  # Базовый ID для тестовых данных

    def _get_next_test_id(self):
        sql = text("SELECT MAX(subject_id) FROM subject")
        result = self.session.execute(sql)
        max_id = result.scalar() or 0
        return max(max_id, self._test_id_base) + 1

    def create_subject(self, title, subject_id=None):
        if subject_id is None:
            subject_id = self._get_next_test_id()

        sql = text("""
            INSERT INTO subject (subject_id, subject_title)
            VALUES (:subject_id, :title)
        """)

        self.session.execute(sql, {"subject_id": subject_id, "title": title})
        self.session.commit()
        return subject_id

    def get_subject(self, subject_id):
        sql = text("SELECT * FROM subject WHERE subject_id = :subject_id")
        result = self.session.execute(sql, {"subject_id": subject_id})
        return result.mappings().first()

    def update_subject(self, subject_id, new_title):
        sql = text("""
            UPDATE subject
            SET subject_title = :new_title
            WHERE subject_id = :subject_id
        """)
        result = self.session.execute(
            sql,
            {"subject_id": subject_id, "new_title": new_title}
        )
        self.session.commit()
        return result.rowcount

    def delete_subject(self, subject_id):
        sql = text("DELETE FROM subject WHERE subject_id = :subject_id")
        result = self.session.execute(sql, {"subject_id": subject_id})
        self.session.commit()
        return result.rowcount > 0

    def create_student(self, user_id, level, education_form, subject_id):
        sql = text("""
            INSERT INTO student (user_id, level, education_form, subject_id)
            VALUES (:user_id, :level, :education_form, :subject_id)
        """)
        result = self.session.execute(
            sql,
            {
                "user_id": user_id,
                "level": level,
                "education_form": education_form,
                "subject_id": subject_id
            }
        )
        self.session.commit()
        return result.rowcount > 0

    def get_student(self, user_id):
        sql = text("SELECT * FROM student WHERE user_id = :user_id")
        result = self.session.execute(sql, {"user_id": user_id})
        return result.mappings().first()

    def delete_student(self, user_id):
        sql = text("DELETE FROM student WHERE user_id = :user_id")
        result = self.session.execute(sql, {"user_id": user_id})
        self.session.commit()
        return result.rowcount > 0

    def get_subject_count(self):
        sql = text("SELECT COUNT(*) FROM subject")
        result = self.session.execute(sql)
        return result.scalar() or 0
