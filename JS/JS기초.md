# 함수

## 함수 표현식, 선언식

선언식 => 호이스 => 에러X

표현식 =>

## ArrowFunction

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 매개변수가 하나면 `()`도 생략가능

```javascript
const arrow1 = funtion (name) {
    return 'hello, ${name}'
}

// 1. funtion 키워드 삭제
const arrow2 = (name) => { return `hello, ${name}`}

// 2. 매개변수가 1개일 경우에만 () 생략 가능
const arrow3 = name => { return `hello, ${name}`}

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에  {} & return 삭제가능
const arrow4 = name => `hello, ${name}`

//example

console.log

console.log(materials.map(material => matertial.length));
// expected output: Array[8,6, 7, 9]
console.log(materialse.map(function (matertial) {
    
}))
```



## IIFE 함수

# Arrays

## spread operator(...)

```javascript
const array = [1, 2, 3]
const newArray = [0, ...array, 4]

console.log(newArray) // [0, 1, 2, 3, 4]
```

## Array Helper Methods

- 배열을 순회하며 특정 로직을 수핼하는 메서드
- 메서드 호술 시 인자로 `callback함수*`를 받는 것이 특징
  - `callback함수*` : 어떤 함수의 내부에서 실행될 목적으로 인자를 넘겨 받는 함수

<img src="C:\Users\user\AppData\Roaming\Typora\typora-user-images\image-20220426125736563.png" alt="image-20220426125736563" style="zoom:80%;" />

### forEach

```js
array.forEach(callback(element[, index[,array]]))
```

- 배열의 각 요소에 대해 콜백함수를 한번씩 실행

- 콜백 함수는 3가지 매개변수로 구성



### map

```js
array.map(callback(elemnet[, index[, array]]))

//예
const numbers = [1, 2, 3, 4, 5]

const doublleNums = numbers.map((num) => {
    return num * 2
})

console.log(doubleNUms) // [2, 4, 6, 8, 10]

// arrowFunction 
console.log(numbers.map(number => number * 2))// [2, 4, 6, 8, 10]

//예
const rectangles = [
    {'width':30, 'height':20},
    {'width':10, 'height':20}
]

//1 
const area = rectangles.map((wh) => wh.width*wh.height)
console.log(area)// [600, 200]

//2
console.log(reactanles.map(r => r.width*r.height))//[600, 200]

```

- 배열의 각 요소에 대해 콜백함수를 한 번씩 실행
- 콜백 함수의 반환값을 요소로하는 새로운 배열 반환
- 기존 배열 전체를 다른 형태로 바꿀 때 유용

### filter

```js
array.filter(callback(elemnet[, index[, array]]))

//얘
const numbers = [1, 2, 3, 4, 5]

// 1
const oddNums = numbers.filter((num, index) => {
    return num % 2
})

//2
numbers.filter(num, index) => num % 2)
```

- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- 기존 배열의 요소들을 필터링할 때 유용

**자바스크립트는 파라미터 정의된 대로 호출할 필요가 없다.**

```js
// 실습
const students = [
    {python: 100, js: 95},
    {python: 80, js: 100}
]
// 1. function 표현식
students.map(function (student){
    return student.python + student.js
})
// 2. Array function
students.map((student) => {
    return student.python + student.js
})
students.map(student => {
    return student.python + student.js
})
students.map(student => student.python + student.js)
```

### reduce

```js
array.reduce(callback(acc, elemnet[, index[, array]])[, initialVlaue])

array,reduce((acc, element, index, array) => {
	//
}, initialValue)

// 예
const = numbers = [1, 2, 3]
const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)
```

- 값을 두개 받는다.

### find

```js
array.find(callback(elemnet[, index[, array]]))

array.find((element, index, array) =>{
    
})
```



### sum

```js
array.sum(callback(elemnet[, index[, array]]))

array.sum((element, index, array) =>{
    
})
```



### every

```js
array.every(callback(elemnet[, index[, array]]))

array.every((element, index, array) =>{
    
})
```



## 객체

- 객체는 속성의 집합, 중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
- value는 모든 타입 가능
- 객체 요소 접근은 점 또는 대괄호로 가능

# lodash

```js
<script src="https://cdn.jsdelivr.net/npm/lodash@4.17.21/lodash.min.js"></script>
```

