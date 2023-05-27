#!/bin/bash

# 引数が渡されていない場合はエラーを出力して終了する
if [ -z "$1" ]; then
  
  exit 1
fi

# 引数として渡された日付を変数に格納する
d="$1"

# 出力するファイル名を作成する
output_file="data/$d.csv"

# データファイルから、指定された日付に対応する行を抽出して、出力ファイルに書き込む
grep "^$d," data.csv > "$output_file"