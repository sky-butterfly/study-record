## Bubble Sort (버블정렬)
- 서로 인접한 두 원소를 비교하여 정렬
- 1번원소-2번원소 => 2번원소-3번원소 => 3번원소-4번원소 =>... 순으로 비교하여 크기가 큰 원소를 위쪽으로 이동
- 1번원소부터 마지막 원소까지 비교가 끝나면 1회전 완료되며, 1회전 완료 후에는 가장 큰 원소가 맨 뒤에 위치
- 각각의 회전이 끝날 때마다 맨 뒤의 원소를 하나씩 제외시키며 정렬

## 예제 소스
```

int[] arr = {5, 1, 4, 2, 3, 7, 6};
int size = arr.length;

for(int i=0; i<size; i++) {
    
    for(int k=0; k<size-i-1; k++) {
        
        if(arr[k+1] >= arr[k]) {
            continue;				
        }
        
        int tmp = arr[k+1];
        arr[k+1] = arr[k];
        arr[k] = tmp;
    }
}

for(int a : arr) {
    System.out.println(a);
}

```