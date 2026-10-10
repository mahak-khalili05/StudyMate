# StudyMate — Study Planner

A simple and practical study planner web application built with **Python, Flask, SQLite, HTML, and CSS**.

StudyMate helps students organize their assignments, track their progress, and manage their study tasks in one place.

## Features

- **Add Tasks:** Create tasks with a name, subject, and due date.
- **Track Progress:** Mark tasks as completed or incomplete.
- **Delete Tasks:** Remove tasks when they are no longer needed.
- **Filter Tasks:** View all tasks, active tasks, or completed tasks.
- **Sort by Due Date:** Display tasks in order of their due dates.
- **Persistent Storage:** Store task information in an SQLite database.
- **Responsive Design:** Use a clean and simple interface on different screen sizes.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application logic |
| Flask | Web application framework |
| SQLite | Database and task storage |
| HTML | Page structure |
| CSS | Styling and layout |
| Git & GitHub | Version control and project hosting |

## Project Structure

```text
StudyMate/
├── app.py
├── README.md
├── .gitignore
└── templates/
    └── index.html
```

The `studymate.db` database file is created automatically when the application runs. It is excluded from GitHub, so each new local setup starts with its own database.

## Getting Started

### Prerequisites

- Python installed on your computer
- pip, Python's package installer

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/mahak-khalili05/StudyMate.git
```

**2. Open the project directory**

```bash
cd StudyMate
```

**3. Install Flask**

```bash
python -m pip install flask
```

**4. Run the application**

```bash
python app.py
```

**5. Open StudyMate in your browser**

Visit:

```text
http://127.0.0.1:5000
```

You can now add tasks, update their completion status, delete them, and filter them by status.

## What I Learned

Through this project, I practiced:

- Building a web application with Python and Flask
- Connecting HTML forms to backend routes
- Performing database operations using SQLite
- Working with SQL queries to filter and sort records
- Managing application data and handling user actions
- Organizing project files and using Git for version control

## Future Improvements

Potential improvements include task editing, search functionality, and additional study progress statistics.

## Author

**Mahak Khalili**

An independent learning project created to develop my programming skills and explore practical web application development.

---

*StudyMate — Small steps, steady progress.*
