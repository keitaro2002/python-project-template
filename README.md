# Python Project Template
This is a template for Python projects.

# How to use 
1. GitHub上で新しいリポジトリを作成する
    * `Repository template`を選択し、このリポジトリを選択する
2. ローカルで以下のコマンドを実行する
    ```bash
    git clone　<repository_url>
    cd <repository_name>
    ```
3. 環境構築
* `pyproject.toml`の`name`を変更する
* 以下のコマンドを実行する
    ```bash
    pyenv local <python-version>
    python -m venv .venv
    poetry config virtualenvs.in-project true
    sh poetry.sh install
    ```

# Tips
* モジュールの追加
   ```bash
   sh poetry.sh add <module_name>