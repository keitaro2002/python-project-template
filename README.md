# Python Project Template
This is a template for Python projects.

# How to use 
1. GitHub上で新しいリポジトリを作成する
    * `Repository template`を選択し、このリポジトリを選択する
2. ローカルで新しいディレクトリを作成する
    ```bash
    mkdir <repository_name>
    cd <repository_name>
    ```
3. 以下のコマンドを実行する
    ```bash
    git clone　<repository_url>
    cd <repository_name>
    ```
4. 環境構築
    ```bash
    pyenv local <python-version>
    python -m venv .venv
    ./poetry.sh install
    ```
    