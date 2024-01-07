# parallel-processing-mandelbrot.py

🍁🍁🍁 Pythonで並列処理でマンデルブロ集合を描画してみる！  

[![ci](https://github.com/osawa-koki/parallel-processing-mandelbrot.py/actions/workflows/ci.yml/badge.svg)](https://github.com/osawa-koki/parallel-processing-mandelbrot.py/actions/workflows/ci.yml)
[![exec](https://github.com/osawa-koki/parallel-processing-mandelbrot.py/actions/workflows/exec.yml/badge.svg)](https://github.com/osawa-koki/parallel-processing-mandelbrot.py/actions/workflows/exec.yml)

![成果物](./docs/images/fruit.png)  

## 実行方法

DevContainerに入り、以下のコマンドを実行します！  

```shell
poetry run python ./app/main.py
```

実行結果は以下のようになります！  
※ M2 Mac(2023)での実行結果です。  

```result
poetry run python ./app/main.py

single_thread: 2.837815999999293
multi_thread : 7.2405362500066985
```

う〜ん、、、  
マルチスレッドの方が遅くなってしまいましたね、、、  

インタプリタのGILのせいで、マルチスレッドの方が遅くなってしまったようです。  
