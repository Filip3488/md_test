import duckdb
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.path.dirname(__file__), "md_test.env"))

MD_DB = "md:md_test"


def _connect():
    token = os.environ["MOTHERDUCK_TOKEN"]
    return duckdb.connect(f"{MD_DB}?motherduck_token={token}")


def load_data(table: str | None = None) -> tuple[list[str], list[tuple]]:
    con = _connect()
    try:
        tables = [row[0] for row in con.execute("SHOW TABLES").fetchall()]
        if not tables:
            return [], []
        target = table if table in tables else tables[0]
        result = con.execute(f"SELECT * FROM {target}").fetchall()
        columns = [desc[0] for desc in con.description]
        return columns, result
    finally:
        con.close()


def get_tables() -> list[str]:
    con = _connect()
    try:
        return [row[0] for row in con.execute("SHOW TABLES").fetchall()]
    finally:
        con.close()
