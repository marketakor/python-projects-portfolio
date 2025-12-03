## csv_analyzer_lite

A simple Python program for analyzing CSV files – it loads data and calculates basic statistics.

### Running and Testing

```bash

# Clone the repository and navigate to the project folder
git clone https://github.com/marketakor/csv_analyzer_lite.git
cd csv_analyzer_lite

# Run the main script
python main.py

# Run tests (Linux / Mac)
PYTHONPATH=. pytest tests/

# Run tests (Windows PowerShell)
$env:PYTHONPATH="."
pytest tests/
