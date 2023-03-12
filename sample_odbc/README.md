# sample_odbc

## 環境
- Apple M1
- macOS Ventura 13.2.1

## セットアップ
- 以下のページのコマンドを実行
  - [Microsoft ODBC 17](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/install-microsoft-odbc-driver-sql-server-macos?view=sql-server-ver16#17)
  - 加えて以下のsymbolic_linkを貼る
  ```zsh
  % sudo ln -s /opt/homebrew/etc/odbcinst.ini /etc/odbcinst.ini
  % sudo ln -s /opt/homebrew/etc/odbc.ini /etc/odbc.ini
  ```
- LDFLAGSとCPPFLAGSの環境変数を設定
  - [Installing on MacOSX](https://github.com/mkleehammer/pyodbc/wiki/Install#installing-on-macosx)
- 今回はODBC経由でPostgreSQLに接続したいのでpsqlodbcをinstall
```zsh
% brew install psqlodbc
```
- その後、下記の環境変数をそれぞれ実行
```zsh
echo 'export PATH="/opt/homebrew/opt/postgresql@13/bin:$PATH"' >> ~/.zshrc
export LDFLAGS="-L/opt/homebrew/opt/postgresql@13/lib"
export CPPFLAGS="-I/opt/homebrew/opt/postgresql@13/include"
export PKG_CONFIG_PATH="/opt/homebrew/opt/postgresql@13/lib/pkgconfig"
initdb --locale=C -E UTF-8 /opt/homebrew/var/postgresql@14
```
