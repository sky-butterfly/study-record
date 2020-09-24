# Set, Interator

- Set은 중복이 없고 순서도 없는 자료구조
- Iterator 로 값을 가져올 수 있다.

- ex)
```
Set<String> set = new HashSet<String>();
Iterator<String> iter = set.iterator();

while(iter.hasNext()) {
    System.out.println(iter.next());     
}
```