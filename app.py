
from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "studymate.db"


def get_db_connection():
    connection = sqlite3.connect(DATABASE)
    connection.row_factory = sqlite3.Row
    return connection


def create_table():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            subject TEXT NOT NULL,
            due_date TEXT NOT NULL,
            completed INTEGER NOT NULL DEFAULT 0
        )
    """)

    connection.commit()
    connection.close()


@app.route("/")
def home():
    selected_filter = request.args.get("filter", "all")

    connection = get_db_connection()

    if selected_filter == "active":
        tasks = connection.execute(
            """
            SELECT * FROM tasks
            WHERE completed = 0
            ORDER BY due_date ASC, id DESC
            """
        ).fetchall()

    elif selected_filter == "completed":
        tasks = connection.execute(
            """
            SELECT * FROM tasks
            WHERE completed = 1
            ORDER BY due_date ASC, id DESC
            """
        ).fetchall()

    else:
        selected_filter = "all"

        tasks = connection.execute(
            """
            SELECT * FROM tasks
            ORDER BY due_date ASC, id DESC
            """
        ).fetchall()

    total_count = connection.execute(
        "SELECT COUNT(*) FROM tasks"
    ).fetchone()[0]

    completed_count = connection.execute(
        "SELECT COUNT(*) FROM tasks WHERE completed = 1"
    ).fetchone()[0]

    connection.close()

    return render_template(
        "index.html",
        tasks=tasks,
        total_count=total_count,
        completed_count=completed_count,
        selected_filter=selected_filter
    )


@app.route("/add", methods=["POST"])
def add_task():
    title = request.form.get("title", "").strip()
    subject = request.form.get("subject", "").strip()
    due_date = request.form.get("due_date", "")

    if title and subject and due_date:
        connection = get_db_connection()

        connection.execute(
            """
            INSERT INTO tasks (title, subject, due_date)
            VALUES (?, ?, ?)
            """,
            (title, subject, due_date)
        )

        connection.commit()
        connection.close()

    return redirect("/")


@app.route("/complete/<int:task_id>", methods=["POST"])
def complete_task(task_id):
    connection = get_db_connection()

    connection.execute(
        """
        UPDATE tasks
        SET completed = CASE
            WHEN completed = 0 THEN 1
            ELSE 0
        END
        WHERE id = ?
        """,
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")


@app.route("/delete/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    connection = get_db_connection()

    connection.execute(
        "DELETE FROM tasks WHERE id = ?",
        (task_id,)
    )

    connection.commit()
    connection.close()

    return redirect("/")


create_table()


if __name__ == "__main__":
    app.run(debug=True)
