## Prefix Sum (누적 합)
- 일반배열에서 특정 인덱스까지의 값들로 배열이 만들어진 것을 누적합 배열이라고 함
> ex) 일반배열 => 1, 2, 3, 4, 5, 6   
    누적합배열 => 1, 3, 6, 10, 15, 21
- 구간의 합을 빠르게 구할 수 있는 알고리즘

```

int[] arr = {1, 2, 3, 4, 5, 6};
		
int[] prefixSum = new int[arr.length];
prefixSum[0] = arr[0];

for(int i=1; i<arr.length; i++) {
    prefixSum[i] = prefixSum[i-1] + arr[i];
}

```