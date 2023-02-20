name: PyLint
on: push
jobs:
  PEP8:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v1
        with:
          python-version: 3.9
      - name: Install Python lint libraries
        run: |
          pip install autoflake isort black
      - name: Remove unused imports and variables
        run: |
          autoflake --in-place --recursive --remove-all-unused-imports --remove-unused-variables --ignore-init-module-imports .
          
          
          # commit changes
      - uses: stefanzweifel/git-auto-commit-action@v4
        with:
          commit_message: 'PandaX_Userbot: auto fixes'
          commit_options: '--no-verify --signoff'
          repository: .
          commit_user_name: ilham77mansiz
          commit_user_email: imansiez7@gmail.com
          commit_author: ilham77mansiz <imansiez7@gmail.com>
