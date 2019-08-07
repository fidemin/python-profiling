# -n: 각 타이머 당 실행되는 loops. 각 loop를 실행하는데 걸린 시간의 평균이 타이머의 대표값이다.
# -r: 타이머가 반복되는 횟수. 각 타이머의 대표값 중 가장 작은 실행시간이 선택된다. 
echo "bubble sort"
python -m timeit -n 10 -r 5 -v -s "import sort" "sort.bubble_sort()"
echo "tim sort"
python -m timeit -n 10 -r 5 -v -s "import sort" "sort.tim_sort()"
