# Supply-Invento

Supply-Invento was a CRM-like project developed using Django.

## Overview

Supply-Invento aimed to streamline inventory management and supply chain processes. The website provided different roles: Teacher, Warehouse Manager, Supplier, and Administrator. Each page of the system catered to the specific role of the user.

## Tech Stack

- Django <img height="20" width="20" src="https://cdn.simpleicons.org/django/white" />
- PostgreSQL <img height="20" width="20" src="https://cdn.simpleicons.org/postgresql" />
- HTML / CSS <img height="20" width="20" src="https://cdn.simpleicons.org/html5" /> <img height="20" width="20" src="https://cdn.simpleicons.org/css3" />
- JavaScript <img height="20" width="20" src="https://cdn.simpleicons.org/javascript" />

## Description

The project implemented full CRUD functionality with role-specific restrictions. For example:
- **Teacher**: Could create and edit orders only on specific dates, depending on the teacher's schedule.
- **Storekeeper**: Could make edits and comments only in designated areas.
- **Supplier**: Had access to specific sections for inputting data relevant to their role.

This role-based access control ensured that each user had access only to the functionalities relevant to their responsibilities.

## Usage

To run the project locally, follow these steps:

1. Clone the repository:

```bash
git clone git@github.com:Asadhimself/supply-invento.git
```
2. Install Poetry (if not already installed):
```bash
pip3 install poetry
```
3. Initialize Poetry:
```bash
poetry init
```
4. Install project dependencies:
```bash
poetry install
```
5. Run the Django server:
```bash
python manage.py runserver
```
5. Use the following credentials to log in:
- **Storekeeper**: a.sanches@demo.uz (Password: Demo2020)
- **Supplier**: i.ivanov@demo.uz (Password: Demo2020)
- **Teacher**: j.doe@demo.uz (Password: Demo2020)

## Live Demo

Check out the live demo [here](https://pythonanywhere.asadhimself.com).

## Credits

Frontend developer: [ameerkhansaeed](https://github.com/ameerkhansaeed) <img height="20" width="20" src="https://cdn.simpleicons.org/github/white" /> <br>
You can explore frontend code for itself [here](https://github.com/Asadhimself/supply-invento/tree/frontend)

## Disclaimer

The project has been taken from production since the developer's departure from the organization.

