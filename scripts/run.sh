#!/bin/bash

# 環境変数からSIF_PATHを取得
SIF_PATH="${SIF_PATH}"

# 実行環境 (gpu or cpu) とPythonスクリプトのパスをコマンドライン引数から受け取る
EXEC_ENV="$1"
PYTHON_SCRIPT="$2"

# その他のコマンドライン引数を受け取る
args="${@:3}"

# 実行環境に応じてジョブをサブミット
if [ "$EXEC_ENV" = "gpu" ]; then
  # GPUを使用する場合
  srun --chdir $(pwd) --gpus 20gb:1 -p gpu singularity run --nv "$SIF_PATH" /bin/bash -c "poetry run python3 $PYTHON_SCRIPT $args"
elif [ "$EXEC_ENV" = "cpu" ]; then
  # CPUのみを使用する場合
  srun --chdir $(pwd) -p cpu singularity run "$SIF_PATH" /bin/bash -c "poetry run python3 $PYTHON_SCRIPT $args"
else
  echo "指定された実行環境が不正です。gpuまたはcpuを指定してください。"
fi