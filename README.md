# API de Danzas patrimonio
API hecha para las danzas y fiestas declaradas patrimonio de la nación

> Los datos fueron extraídos de la página del ministerio de la cultura

## 1. Instalación

```sh
pip install -r requirements.txt
```
> Es necesario crear un archivo llamado **.env** donde pondremos nuestro URL de la base de datos MySQL. Ejemplo: DATABASE_URL = "mysql+pymysql://`user`:`password`@`localhost`:`3306`/`database`"

## 2. Data
Ejecutamos el archivo 'data.ipynb' que nos crea una base de datos mysql local con todas las columnas necesarias en la tabla

## 3. Ejecución
Ejecutamos la API mediante el comando
```sh
fastapi dev sql_app/main.py
```

## 4. Prueba
Ingresar al link para visualizar todas las expresiones `http://127.0.0.1:8000/`