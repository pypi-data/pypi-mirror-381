import pandas as pd
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


class DatabaseManager:
    """Utility class for managing database operations with SQLAlchemy.

    This class provides convenient methods for:
    - Managing SQLAlchemy engine and sessions.
    - Inserting single ORM instances.
    - Bulk inserting pandas DataFrames.
    - Direct DataFrame insertion via pandas `to_sql`.
    - Querying all records from a given model.
    """

    def __init__(self, database_url: str, Base: any):
        """Initialize the DatabaseManager.

        Args:
            database_url (str): SQLAlchemy database URL (e.g., sqlite:///db.sqlite).
            Base (any): Declarative base that contains ORM models.

        Notes:
            If `Base` is provided, all models defined in the base will be created automatically.
        """
        self.engine = create_engine(
            url=database_url,
            pool_pre_ping=True,
            pool_recycle=1800,
            future=True
        )
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            future=True
        )
        if Base:
            Base.metadata.create_all(bind=self.engine)

    def _get_session(self):
        """Create and return a new SQLAlchemy session.

        Returns:
            Session: A new session bound to the engine.
        """
        return self.SessionLocal()
    
    ## CREATE
    def insert_data(self, model_instance):
        """Insert a single ORM instance into the database.

        Args:
            model_instance: An instance of an ORM model to be persisted.
        """
        session = self._get_session()
        with session.begin():
            session.add(model_instance)
        session.close()

    def bulk_insert_dataframe(self, df: pd.DataFrame, model_cls: any, truncate: bool = False):
        """Insert a pandas DataFrame into the database using bulk insert.

        Args:
            df (pd.DataFrame): DataFrame containing the data to insert.
            model_cls: ORM model class that maps to the target table.

        Notes:
            This method uses `bulk_insert_mappings` for better performance
            when inserting many records at once.
        """
        records = df.to_dict(orient="records")
        with self._get_session() as session:
            if truncate:
                session.execute(model_cls.__table__.delete())
            session.bulk_insert_mappings(model_cls, records)
            session.commit()

    def to_sql_dataframe(self, df: pd.DataFrame, table_name: str, if_exists="append"):
        """Insert a pandas DataFrame directly into a SQL table.

        Args:
            df (pd.DataFrame): DataFrame containing the data to insert.
            table_name (str): Name of the database table.
            if_exists (str, optional): Behavior if the table already exists.
                Options: "append" (default), "replace", or "fail".
        """
        df.to_sql(table_name, self.engine, if_exists=if_exists, index=False)

    ## READ
    def select_all(self, model) -> list[dict]:
        """Retrieve all rows from a given ORM model's table.

        Args:
            model: ORM model class representing the target table.

        Returns:
            list[dict]: List of rows as dictionaries, where each key is a column name.
        """
        with self._get_session() as session:
            rows = session.execute(select(model)).scalars().all()
            cols = [c.name for c in model.__table__.columns]

            for row in rows:
                print(" | ".join(f"{c}: {getattr(row, c)}" for c in cols))

            return [{c: getattr(r, c) for c in cols} for r in rows]

    ## UPDATE
    # (To be implemented as needed)

    ## DELETE
    def delete_all(self, model):
        """Delete all rows from a given ORM model's table.

        Args:
            model: ORM model class representing the target table.
        """
        with self._get_session() as session:
            session.execute(model.__table__.delete())
            session.commit()
