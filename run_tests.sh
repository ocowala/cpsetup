#!/usr/bin/env zsh
function output(){
	cd $2
	/opt/homebrew/bin/g++ "$file_name.cpp" -o $file_name && ./$file_name < "samples/$1" > "samples/output.out"
	value=$(cat "samples/output.out")
	echo "$value"
	cd samples
}
function expected(){
	value=$(cat $1)
	echo "$value"
}
function output_diffs(){	
	difference=$(grep -Fxvf $1 $2)
	ans=""	
	if [[ -z "$difference" ]]; then
		printf ""
		#amt_passed=$(($amt_passed + 1))
	else	
		line=$(grep -n $difference $2)
		echo $line > diffs.txt
		first_line_of_diff_txt=$(head -1 diffs.txt)
		line_number=$(echo $first_line_of_diff_txt | cut -c1-1)
		#printf "line number: $line_number\n"
		expected=$(sed -n "$line_number"p $2)
		output=$(sed -n "$line_number"p $1)
		line_number_string="$line_number"
		printf "Mismatch at "$line_number_string"-th value: $output (output.out) vs. $expected ($2)"
		: > "diffs.txt"
	fi
	}
function dbrun(){
amt_passed=0
file_name=$1
cur_dir="$PWD"
printf "[DEBUG MODE] Compiling $file_name.cpp\n"
#/opt/homebrew/bin/g++ "$1.cpp" -o $1 && ./$1
cd samples
amt_of_ins_output=$(ls *.in | wc -l | xargs)
amt_of_ins_output=$(($amt_of_ins_output))
for i in {1..$(($amt_of_ins_output))}
do
	#printf "Case $i:\n"
	printf "Running samples$i.in:"
	printf "\n- - - - - - - - - - - - - - -"
	strin="sample$i.in"
	strout="sample$i.out"
	printf "\nOutput:\n"
	output $strin $cur_dir
	printf "- - - - - - - - - - - - - - -\n"
	printf "Expected:\n"
	expected $strout
	printf "- - - - - - - - - - - - - - -\n"
	if [[ $(output_diffs "output.out" $strout) == "" ]]; then
		printf "\n"
		amt_passed=$(($amt_passed + 1))
	else
		printf "$(output_diffs "output.out" $strout)\n\n"
	fi
	#clearing contents
	: > "output.out"
done
if [ $(($amt_passed)) -eq $(($amt_of_ins_output)) ];
then
	GREEN='\033[0;32m'
	printf "${GREEN}Passed!\n$amt_passed/$amt_of_ins_output passed!"
else
	RED='\033[0;31m'
	printf "${RED}Failed!\n$amt_passed/$amt_of_ins_output passed!"
fi
cd $cur_dir
exec zsh
}
#dbrun $1