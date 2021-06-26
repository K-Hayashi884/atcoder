level=$1
round=$2
prob=$3
problem_name=$level$round${prob^^}
test_dir=test/${problem_name}
# make test directory
oj s https://atcoder.jp/contests/$level$round/tasks/$level${round}_${prob,,} ./${level^^}/$level$round/$problem_name.py