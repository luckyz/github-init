# GitHub initialize ![Build Status](https://img.shields.io/badge/build-under%20development-orange)

## Install

```bash
git clone https://github.com/luckyz/github-init.git
cd github-init/

# if you wish use virtual environments
pip3 install python-virtualenv
virtualenv venv && source venv/bin/activate

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
EMAIL="your_email"
USERNAME="your_username"
PASSWORD="your_password"
FILEPATH="/path/to/your/project/"
```
