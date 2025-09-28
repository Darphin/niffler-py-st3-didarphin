from sqlalchemy import create_engine, Engine
from sqlmodel import Session, select, delete
from sqlalchemy.exc import SQLAlchemyError
import allure
from allure_commons.types import AttachmentType
from sqlalchemy import create_engine, Engine, event
from niffler_qa_5.models.spend import Category, Spend


class SpendDB:
    engine: Engine
    def __init__(self, db_url:str):
        self.engine = create_engine(db_url)
        event.listen(self.engine, "do_execute", fn=self.attach_sql)

    @staticmethod
    def attach_sql(cursor, statement, parameters, context):
        statement_with_params = statement % parameters
        name = statement.split(" ")[0] + " " + context.engine.url.database
        allure.attach(statement_with_params, name=name, attachment_type=AttachmentType.TEXT)

    def get_user_categories(self, username):
        with Session(self.engine) as session:
            statement = select(Category).where(Category.username == username)
            return session.exec(statement).all()

    def get_category_by_name(self, name, username):
        with Session(self.engine) as session:
            statement = select(Category).where(Category.username == username and Category.name == name)
            return session.exec(statement).all()

    def get_category_by_id(self, id):
        with Session(self.engine) as session:
            statement = select(Category).where(Category.id == id)
            return session.exec(statement).first()

    def delete_category(self, category_id):
        with Session(self.engine) as session:
            statement = delete(Category).where(Category.id == category_id)
            try:
                session.exec(statement)
                session.commit()
            except SQLAlchemyError as e:
                error = str(e.__dict__['orig'])
                return error


    def delete_all_categories_for_user(self, username):
        with Session(self.engine) as session:
            statement = delete(Category).where(Category.username == username)
            session.exec(statement)
            session.commit()

    def delete_all_spendings_for_user(self, username):
        with Session(self.engine) as session:
            statement = delete(Spend).where(Spend.username == username)
            session.exec(statement)
            session.commit()



