# Divine Dragonflies

TBD project.

## Running this project

- Create a Python 3.9 virtualenv and activate it.
- Install nox.

  ```
  $ pip install nox
  ```

- Run this project, with nox.

  ```
  $ nox -s run
  ```

## Development Workflow

### Set up

- Create a Python 3.9 virtualenv and activate it.
- Install the development requirements for this project.

  ```
  $ pip install -r requirements-dev.txt
  ```

### Run the project

```
nox
```

### Run linters

```
nox -s lint
```
