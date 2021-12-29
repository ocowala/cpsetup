#!/usr/bin/env bash
cur_dir="$PWD"
{ time "./$1" < "samples/$2" > "samples/output2.out"; } 2> $3
rm -f samples/output2.out
real_line=$(head -2 samples/time.txt)
ans=$(echo $real_line | cut -c8-13)
printf "Time: $ans\n"
: > $3
exec bash