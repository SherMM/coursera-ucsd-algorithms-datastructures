for file in `ls tests/ | grep -v "\."`
do
  python3 tree-height.py < tests/$file
done
