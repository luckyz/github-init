# GitHub initialize ![Build Status](https://img.shields.io/badge/build-under%20development-orange)

## Install

```bash
git clone https://github.com/luckyz/github-init.git
cd github-init/
virtualenv venv && source venv/bin/activate  # (only if you wish use virtual environment)
pip3 install -r requirements.txt`
touch .env
```

Then open the .env file and store your username, password, and desired file destination. Use the provided format at the bottom of this README.

```bash
source ~/.my_commands.sh
```


## Usage

To run the script type

```bash
 create <foldername>
```

## Env File Format

```bash
USERNAME="Username123"
PASSWORD="Password123"
FILEPATH="/path/to/your/project/"
```
