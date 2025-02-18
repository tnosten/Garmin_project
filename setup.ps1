# Create virtual environment
# python -m venv .venv

# Activate virtual environment
.venv\Scripts\Activate

# Upgrade pip and install dependencies
pip install --upgrade pip
pip install -r requirements.txt

Write-Host "Setup complete. To activate the environment, run: .\.venv\Scripts\Activate"

