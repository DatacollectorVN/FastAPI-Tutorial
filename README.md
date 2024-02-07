# FastAPI-Tutorial

# Sample structure of FastAPI project

All materials in `app` folder. The `docs` folder contain all *.md* files for document services

## 1. app
### 1.1. config
Contains all configuration files for `app`

- `config_reader.py`: initialize `config` object
- `config.ini`: configuration file

### 1.2. database
Contain all database connection management object / class. All connections in `connections` folder with:
- `__init__.py`: creates all session connections for all database
- `<database_engine>.py`: contains session of **<database_engine>**

### 1.3. models
Define all tables in database

### 1.4. services
Contains all services of API support

### 1.5. test
Unit test folder

### 1.6. utils
All utilities functions

### 1.7. main.py
Main running application. Need to add route's service inside the `main.py`

## 2. Run application
```bash
python app/main.py
```