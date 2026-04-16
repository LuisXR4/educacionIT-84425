"""Ejemplo de CRUD completo con SQLAlchemy.

Este script demuestra cómo crear, leer, actualizar y eliminar registros
utilizando SQLAlchemy ORM con una base de datos SQLite.

Requisitos:
    pip install SQLAlchemy

Estructura:
    - Definición del modelo de datos (User)
    - Configuración de la conexión y sesión
    - Funciones CRUD reutilizables
    - Ejecución de un flujo de trabajo completo en `main()`
"""

from datetime import datetime
from typing import List, Optional

from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

# Base para los modelos de SQLAlchemy
Base = declarative_base()


class User(Base):
    """Modelo de usuario para el ejemplo CRUD."""

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self) -> str:
        return f"<User(id={self.id}, name={self.name}, email={self.email})>"


def create_database(engine) -> None:
    """Crea las tablas de la base de datos si no existen."""
    Base.metadata.create_all(engine)


def get_engine(database_url: str = "sqlite:///usuarios_sqlalchemy.db"):
    """Crea un motor de base de datos SQLAlchemy."""
    return create_engine(database_url, echo=False, future=True)


def get_session(engine) -> Session:
    """Crea una sesión de SQLAlchemy para interactuar con la base de datos."""
    SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False, future=True)
    return SessionLocal()


def create_user(session: Session, name: str, email: str) -> User:
    """Inserta un nuevo usuario en la base de datos."""
    new_user = User(name=name, email=email)
    session.add(new_user)
    session.commit()
    session.refresh(new_user)
    return new_user


def get_user_by_id(session: Session, user_id: int) -> Optional[User]:
    """Consulta un usuario por su ID."""
    return session.query(User).filter(User.id == user_id).first()


def get_all_users(session: Session) -> List[User]:
    """Obtiene todos los usuarios registrados."""
    return session.query(User).order_by(User.id).all()


def update_user_email(session: Session, user_id: int, new_email: str) -> Optional[User]:
    """Actualiza el correo electrónico de un usuario existente."""
    user = get_user_by_id(session, user_id)
    if user is None:
        return None

    user.email = new_email
    session.commit()
    session.refresh(user)
    return user


def delete_user(session: Session, user_id: int) -> bool:
    """Elimina un usuario de la base de datos."""
    user = get_user_by_id(session, user_id)
    if user is None:
        return False

    session.delete(user)
    session.commit()
    return True


def print_users(users: List[User]) -> None:
    """Imprime la lista de usuarios en forma legible."""
    if not users:
        print("No se encontraron usuarios.")
        return

    print("Usuarios registrados:")
    for user in users:
        print(f"  - ID: {user.id}, Nombre: {user.name}, Email: {user.email}, Creado: {user.created_at}")


def main() -> None:
    """Ejecuta un flujo de trabajo CRUD completo con ejemplos."""
    engine = get_engine()
    create_database(engine)

    with get_session(engine) as session:
        try:
            # Crear usuarios
            print("Creando usuarios...")
            alice = create_user(session, "Alice García", "alice@example.com")
            bob = create_user(session, "Bob Pérez", "bob@example.com")
            jose = create_user(session, "Jose Gomez", "jg@example.com")
            print(f"Usuario creado: {alice}")
            print(f"Usuario creado: {bob}\n")
            print(f"Usuario creado: {jose}\n")

            # Leer todos los usuarios
            users = get_all_users(session)
            print_users(users)
            print()

            # Consultar usuario por ID
            user = get_user_by_id(session, alice.id)
            print(f"Consultando usuario con ID {alice.id}: {user}\n")

            # Actualizar email de usuario
            print("Actualizando email de Bob...")
            updated_bob = update_user_email(session, bob.id, "bob.perez@nuevoemail.com")
            print(f"Usuario actualizado: {updated_bob}\n")

            # Eliminar un usuario
            print(f"Eliminando usuario con ID {alice.id}...")
            eliminated = delete_user(session, alice.id)
            print(f"Eliminado exitoso: {eliminated}\n")

            # Leer usuarios restantes
            users = get_all_users(session)
            print_users(users)
            print()

        except SQLAlchemyError as error:
            session.rollback()
            print("Ocurrió un error con la base de datos:", error)


if __name__ == "__main__":
    main()
