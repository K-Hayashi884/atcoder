
#!/bin/bash

problem_name=$1
level=${problem_name::3}
round=${problem_name:3:3}
prob=${problem_name:6:1}
test_dir=test/${problem_name}
echo https://atcoder.jp/contests/$level$round/tasks/$level${round}_${prob,,}
# make test directory
if [ ! -e ${test_dir} ]; then
    oj dl -d test/${problem_name} https://atcoder.jp/contests/$level$round/tasks/$level${round}_${prob,,}
fi
oj t -c "python ${level^^}/$level$round/${problem_name}.py" -d test/${problem_name}/ -t 2 -i
read -p "Press [Enter] key to resume."