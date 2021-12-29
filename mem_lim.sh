#!/usr/bin/env bash
cur_dir="$PWD"
{ env time -al "./$1" < "samples/$2" > "samples/output2.out"; } 2> $3
rm -f samples/output2.out
real_line=$(head -2 $3)
#printf "real_line:$real_line\n"
ans=$(echo $real_line | cut -c30-36)
printf "Memory: $ans KB\n"
: > $3
exec bash