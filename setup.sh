echo "python3 -m venv venv"
python3 -m venv venv

echo "source venv/bin/activate"
source venv/bin/activate

echo "curl https://bootstrap.pypa.io/get-pip.py | python"
curl https://bootstrap.pypa.io/get-pip.py | python

echo "pip install --upgrade setuptools wheel"
pip install --upgrade setuptools wheel

if [ -f requirements.txt ]; then
    echo "requirements.txt found, installing Python package dependencies"
    pip install -r requirements.txt
else
    echo "requirements.txt not found, will not install Python package dependencies"
fi


