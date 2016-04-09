for file in `ls tests/ | grep -v "\."`
do
  python3 check_brackets.py < tests/$file
done
