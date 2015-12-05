Javascriptで生成されるHTMLを解析する
====================================

Webからデータを取ろうとした時にJavascriptで動的に生成されているものがしばしばあります。
sleniumを使うと割と簡単にそれらの値を取得できます。


サーバ起動::

  $ python -m http.server


今までの方法ではデータは取得できません。

::

   $ python cannot-scrape.py


そういう場合はslenium packageを使うとjavascriptを実行した後の状態のデータを取得できます。

.. note::

   Selenium本体とPythonバインディングのseleniumライブラリが必要です。

Firefoxの場合::

   $ python cannot-scrape.py

PhantomJSを使ってヘッドレスにもできます。

.. note::

   PhantomJSが必要です。またPhantonJSにパスを通す必要があります。

PhantomJSの場合::

   $ python can-scrape-headless.py
