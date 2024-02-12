# Simple AirBnB Clone console

## Introduction

This is a simple clone website project that implements various functionalities using Python classes and a command-line interface.

## Project Structure

The project consists of several modules and classes:

### `models/base_model.py`

- Defines a `BaseModel` class with common attributes and methods for other classes.
- Public instance attributes:
  - `id`: string - assigned with a UUID when an instance is created.
  - `created_at`: datetime - assigned with the current datetime when an instance is created.
  - `updated_at`: datetime - assigned with the current datetime when an instance is created and updated every time you change your object.
- Public instance methods:
  - `save(self)`: updates the public instance attribute `updated_at` with the current datetime.
  - `to_dict(self)`: returns a dictionary containing all keys/values of `__dict__` of the instance.

### `models/engine/file_storage.py`

- Defines a `FileStorage` class that serializes instances to a JSON file and deserializes JSON files to instances.
- Private class attributes:
  - `__file_path`: string - path to the JSON file.
  - `__objects`: dictionary - stores all objects by `<class name>.id`.
- Public instance methods:
  - `all(self)`: returns the dictionary `__objects`.
  - `new(self, obj)`: sets in `__objects` the obj with key `<obj class name>.id`.
  - `save(self)`: serializes `__objects` to the JSON file.
  - `reload(self)`: deserializes the JSON file to `__objects`.

### `console.py`

- Contains the entry point of the command interpreter.
- Implements a class `HBNBCommand` that inherits from `cmd.Cmd`.
- Command interpreter implements:
  - `quit` and `EOF` to exit the program.
  - `help` to display help information.
  - Custom prompt: `(hbnb)`
  - Commands: `create`, `show`, `destroy`, `all`, `update`.

### Other Classes

- `User`, `State`, `City`, `Amenity`, `Place`, `Review`: Classes that inherit from `BaseModel` with specific attributes.

## Usage

To run the program, execute `./console.py` and use the implemented commands.

