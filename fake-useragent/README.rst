User-Agentを詐称する
=====================

requestsを普通に使うとPythonからリクエストを投げていることがばれてしまします。
User-Agentが `'User-Agent': 'python-requests/1.2.0'` こんな感じだからです。
requestsでリクエストを投げる時にUser-Agentをブラウザっぽいものに詐称することができます。


サーバ起動::

  $ python server.py


リクエスト送信::

  $ python fake-ua.py


リクエストが届くとサーバ側のプロセスがデバッガで届くのでサーバ側でもUser-Agentが変わっていることが確認できる::

  ipdb> self.request.headers
  {'Connection': 'keep-alive', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.17 Safari/537.36', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Host': '127.0.0.1:8000'}
  ipdb>
