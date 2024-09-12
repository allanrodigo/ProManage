
# ProManage

**ProManage** is a project and task management system inspired by Trello. The project was developed to provide an intuitive interface for task control and status tracking using a Kanban-style layout. The system is simple but efficient, offering essential functionalities for managing small to medium-sized projects.

## Features
- Creation and management of multiple projects.
- Visual task management system (Kanban) with customizable statuses such as "To-Do", "In Progress", "Review", and "Done".
- User authentication with signup and login pages.
- Task editing and deletion, keeping users updated on project progress.
- Modern, responsive interface using Bootstrap 4.
- Backend developed with Django to ensure security and efficiency in data management.

## Requirements

- **Python 3.10+**
- **Poetry** (for dependency management)
- **Django 4.x**

## Initial Setup

### Step 1: Clone the repository

Clone this repository to your local machine:

```bash
git clone https://github.com/allanrodigo/ProManage.git

cd promanage
```

### Step 2: Install dependencies with Poetry
ProManage uses **Poetry** for dependency management. Make sure Poetry is installed:

Install Poetry (if not already installed):
```bash
pip install poetry
```

Install the dependencies:
```bash
poetry install
```

Activate the virtual environment (if it does not activate automatically):
```bash
poetry shell
```

### Step 3: Set up the database

The system uses SQLite as the default database. To initialize the database, run the migrations:

```bash
poetry run python manage.py makemigrations
poetry run python manage.py migrate
```

### Step 4: Create a superuser (optional)

To access the Django admin panel and manage users, you can create a superuser:

```bash
poetry run python manage.py createsuperuser
```

### Step 5: Start the development server

Now you can start the development server:

```bash
poetry run python manage.py runserver
```

Access the system in your browser at: http://127.0.0.1:8000/.

## How to Contribute
1. Fork the project.
2. Create a new branch for your feature: `git checkout -b my-new-feature`.
3. Commit your changes: `git commit -m 'Adding new feature'`.
4. Push to the branch: `git push origin my-new-feature`.
5. Submit a pull request for review.

## License

This project is licensed under the [MIT License](LICENSE).