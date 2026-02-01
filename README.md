# Project Structure
aegean-tour/
    |-src/
    |    -optimizer.py # Core business logic
    |-tests/
    |    -test_aegean_tour.py # Unit tests (pytest)
    |-main.py
    |-README.md
    |-requirements.txt

# Prerequisites
Download Project from Git
Check version Python 3.9 or later
pip installed

# Create and activate a Virtual Environment
python -m venv venv

# Install Dependencies
pip install -r requirements.txt

# Run project with passing input.txt file from the Project Directory
python3 main.py input.txt
OR
python3 main.py < input.txt

# To run test cases
pytest -v