# Description: implement poetry collectly
# Usage: ./poetry.sh add <module_name>
#        ./poetry.sh update
#        ./poetry.sh install


PYTHON_KEYRING_BACKEND=keyring.backends.fail.Keyring poetry "$@"