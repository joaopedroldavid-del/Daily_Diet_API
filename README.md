# Daily Diet API

This is a simple Flask-based API for managing meals in a daily diet. It allows users to create, read, update, and delete meal records. The API is connected to a MySQL database, where meal information such as food name, description, timetable, and dietary flag is stored.

## Features

* **Register a new meal**: Allows you to add a meal by providing details such as food, description, timetable, and dietary flag.
* **View all meals**: Fetches all meals stored in the database.
* **Get meal by ID**: Retrieves a specific meal's details by its unique ID.
* **Update a meal**: Update the details of an existing meal.
* **Delete a meal**: Remove a meal from the database by its ID.
* **Hello World Route**: A simple test route to verify the server is running correctly.

## Technologies

* **Flask**: A lightweight Python web framework for building APIs.
* **SQLAlchemy**: ORM (Object Relational Mapping) used for database interactions.
* **MySQL**: Relational database management system.
* **Pymysql**: MySQL database driver for Python.

## Endpoints

* **POST /register**: Register a new meal.
   * Request Body:

```json
{
  "food": "Meal Name",
  "description": "Meal Description",
  "timetable": "2025-03-28 13:20:00",
  "fl_diet": true
}
```

   * Response:

```json
{
  "message": "Refeição cadastrada com sucesso"
}
```

* **GET /meal**: Get a list of all meals.
   * Response:

```json
{
  "Meals": [
    {
      "food": "Meal Name",
      "description": "Meal Description",
      "timetable": "2025-03-28 13:20:00",
      "fl_diet": true
    }
  ]
}
```

* **GET /meal/<id>**: Get a specific meal by its ID.
   * Response:

```json
{
  "Meal": {
    "food": "Meal Name",
    "description": "Meal Description",
    "timetable": "2025-03-28 13:20:00",
    "fl_diet": true
  }
}
```

* **PUT /meal/<id>**: Update a specific meal by its ID.
   * Request Body:

```json
{
  "food": "Updated Meal Name",
  "description": "Updated Meal Description",
  "timetable": "2025-03-28 13:20:00",
  "fl_diet": false
}
```

   * Response:

```json
{
  "message": "Refeição atualizada com sucesso"
}
```

* **DELETE /meal/<id>**: Delete a meal by its ID.
   * Response:

```json
{
  "message": "Refeição deletada com sucesso"
}
```

* **GET /helloworld**: A simple test endpoint to verify the API server is working. It returns "Hello World".