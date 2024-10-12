#!/usr/bin/sh
export PYTHONUNBUFFERED=1

if [ -x "poetry" ]; then
    pip3 install poetry
fi

git clone https://github.com/zalun/djpoe.git djpoe-installation
cd djpoe-installation
poetry install -q

# Use a temporary file to capture the exit status
tmp_file=$(mktemp)

# Run the command and capture its output and exit status
{
    poetry run python3 scripts/customize.py | tee /dev/tty
    echo $? >"$tmp_file"
} | tail -n 1 >app_name_file

# Read the exit status and app name from files
exit_status=$(cat "$tmp_file")
app_name=$(cat app_name_file)

# Clean up temporary files
rm -f "$tmp_file" app_name_file

# Check the exit status
if [ "$exit_status" = "0" ]; then
    echo "Project customized successfully"
    cd ..
    mv djpoe-installation "$app_name"
    cd "$app_name"
    rm -rf .venv
    poetry install -q
    cp "$app_name"/"$app_name"/.env.local "$app_name"/"$app_name"/.env
else
    echo "Installation failed with exit status $exit_status"
fi
