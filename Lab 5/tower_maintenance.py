
"""Manage tower maintenance records using an in-memory SQLite database."""

import sqlite3


conn = sqlite3.connect(":memory:")
conn.execute(
    """
    CREATE TABLE towers (
        id INTEGER PRIMARY KEY,
        site TEXT,
        last_service INTEGER,
        faults INTEGER
    )
    """
)


def add_tower(site, last_service, faults=0):
    """Add a tower to the database."""
    conn.execute(
        """
        INSERT INTO towers (site, last_service, faults)
        VALUES (?, ?, ?)
        """,
        (site, last_service, faults),
    )
    conn.commit()


def service_tower(tower_id, year):
    """Record tower maintenance and reset its fault count."""
    try:
        cursor = conn.execute(
            """
            UPDATE towers
            SET last_service = ?, faults = 0
            WHERE id = ?
            """,
            (year, tower_id),
        )
        conn.commit()

        if cursor.rowcount > 0:
            return True

        print("Service failed: tower not found.")
        return False

    except sqlite3.Error as error:
        print(f"Service failed: {error}")
        return False


def overdue(year):
    """Return tower sites whose last service was at least two years ago."""
    rows = conn.execute(
        "SELECT site, last_service FROM towers"
    ).fetchall()

    return [
        site
        for site, last_service in rows
        if year - last_service >= 2
    ]


def risk_level(tower_id):
    """Return the risk level based on the tower's fault count."""
    row = conn.execute(
        "SELECT faults FROM towers WHERE id = ?",
        (tower_id,),
    ).fetchone()

    if row is None:
        return "unknown"

    if row[0] > 3:
        return "high"

    return "normal"


def snapshot():
    """Return a snapshot of all tower records."""
    return conn.execute("SELECT * FROM towers").fetchall()


def main():
    """Run a demonstration of the tower maintenance functions."""
    add_tower("Ridge-A", 2021, 5)
    add_tower("Coast-B", 2024)

    service_count = 0
    if service_tower(2, 2025):
        service_count += 1

    total = len(snapshot())
    print(overdue(2025), risk_level(1), total, service_count)


if __name__ == "__main__":
    main()
