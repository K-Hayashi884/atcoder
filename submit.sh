level=$1
round=$2
prob=$3
PROB=$prob
tr '[a-z]' '[A-Z]' <<< $PROB
LEVEL=$level
tr '[a-z]' '[A-Z]' <<< $LEVEL
problem_name=$level$round$PROB
test_dir=test/${problem_name}
# make test directory
oj s https://atcoder.jp/contests/$level$round/tasks/$level${round}_${prob} ./$LEVEL/$level$round/$problem_name.py