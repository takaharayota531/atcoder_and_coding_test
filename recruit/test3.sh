#!/bin/bash


files=$(find data -type f)

for file in $files; do
  total_price=0
  # ファイルの中身を読み込んで、各行について価格を計算する
  while read line; do
    # 行をカンマで分割して、価格を取り出す
    price=$(echo "$line" | cut -d',' -f3)
    total_price=$((total_price + ${price%.*}*80/100))
  done < "$file"
  date=$(echo "$file" | sed 's/data\///;s/\.csv//')
  echo "$date: $total_price"
done

# 総和を出力する







