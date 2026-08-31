# DetectiveFiles

An interactive mystery investigation website where users solve fictional cases using a complex investigation engine.

## Installation

To set up the project locally, follow these steps:

1. Clone the repository.
2. Ensure you have Python 3.9+ installed.
3. Create a virtual environment:
   ```bash
   python -m venv venv
   ```
4. Activate the virtual environment.
5. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
6. (Optional) Install frontend dependencies:
   ```bash
   npm install
   ```

## Build

You can build the Docker image for production deployment:

```bash
docker build -t detectivefiles .
```

## Run

To run the application locally using the provided Makefile:

```bash
make run
```

Alternatively, you can run the entry point directly:

```bash
python main.py
```

## Dependencies

The project relies on the following major components:
- Flask
- Flask-SQLAlchemy
- Flask-Login
- SQLite

See `requirements.txt` and `package-lock.json` for full dependency details.

## Usage
Navigate to `http://localhost:5000` in your browser. Register a new detective account and begin solving the cases loaded from the engine.
