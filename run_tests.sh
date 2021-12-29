#!/usr/bin/env zsh
function output(){
	cd $2
	/opt/homebrew/bin/g++ -std=c++17 -Wshadow -Wall -O2 -Wno-unused-result "$file_name.cpp" -o $file_name && ./$file_name < "samples/$1" > "samples/output.out"
	touch samples/time.txt
	touch samples/memory.txt
	time=$(bash ~/runtime.sh $file_name $1 "samples/time.txt" &)
	memory=$(bash ~/mem_lim.sh $file_name $1 "samples/memory.txt" &)
	printf "\n$time\n"
	printf "$memory\n"
	rm -f samples/time.txt
	rm -f samples/memory.txt
	printf "Output:\n"
	value=$(cat "samples/output.out")
	echo "$value"
	cd samples
}
function expected(){
	value=$(cat $1)
	echo "$value"
}
function output_diffs(){	
	#fix the difference variable, switch to diff $1 $2 ???
	output_line=$(wc -l $1)
	sample_line=$(wc -l $2)
	output_line=$(echo $output_line | cut -c8-8)
	sample_line=$(echo $sample_line | cut -c8-8)
	output_line=$((output_line))
	sample_line=$((sample_line))
	#printf "output_line: $output_line\n"
	#printf "sample_line: $sample_line\n"
	if [ $((output_line)) -eq $((sample_line)) ]; then
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
			NC='\033[0m'
			YELLOW='\033[1;33m'
			printf "${YELLOW}Mismatch at "$line_number_string"-th value: $output (output.out) vs. $expected ($2)${NC}"
			: > "diffs.txt"
		fi
	else
		NC='\033[0m'
		YELLOW='\033[1;33m'
		printf "${YELLOW}Mismatch: Too little lines or too many lines printed (maybe debug?)${NC}"
	fi
	}
function dbrun(){
amt_passed=0
file_name=$1
cur_dir="$PWD"
printf "[DEBUG MODE] Compiling $file_name.cpp with c++17\n"
#/opt/homebrew/bin/g++ "$1.cpp" -o $1 && ./$1
cd samples
amt_of_ins_output=$(ls *.in | wc -l | xargs)
amt_of_ins_output=$(($amt_of_ins_output))
for i in {1..$(($amt_of_ins_output))}
do
	#printf "Case $i:\n"
	printf "Running sample$i.in:"
	printf "\n- - - - - - - - - - - - - - -"
	strin="sample$i.in"
	strout="sample$i.out"
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
function gprun(){
	file_name=$1
	cur_dir="$PWD"
	printf "[COMPILE MODE] Compiling $file_name.cpp with c++17\n"
	printf "Running samples/input.txt:"
	printf "\n- - - - - - - - - - - - - - -\n"
	printf "Input:\n"
	input_value=$(cat "samples/input.txt")
	echo "$input_value"
	printf "- - - - - - - - - - - - - - -\n"
	/opt/homebrew/bin/g++ -std=c++17 -Wshadow -Wall -O2 -Wno-unused-result "$file_name.cpp" -o $file_name && ./$file_name < "samples/input.txt" > "samples/output.out"
	printf "Output:\n"
	output_value=$(cat "samples/output.out")
	echo "$output_value"
	touch samples/time.txt
	touch samples/memory.txt
	time=$(bash ~/runtime.sh $file_name "input.txt" "samples/time.txt" &)
	memory=$(bash ~/mem_lim.sh $file_name "input.txt" "samples/memory.txt" &)
	printf "\n$time\n"
	printf "$memory\n"
	rm -f samples/time.txt
	rm -f samples/memory.txt
	: > "samples/output.out"
}
#dbrun $1