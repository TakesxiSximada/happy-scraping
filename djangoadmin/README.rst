Djangoのadmin認証を突破してみるサンプル
=======================================

関連パッケージのインストール::

  $ pip install -r requirements.txt


準備::

  $ python manage.py migrate
  $ python manage.py createsuperuser

サーバ起動::

  $ python manage.py runserver

実行::

  $ python client.py [USERNAME]

取得したHTMLがres.htmlに出力されるようになっています。
