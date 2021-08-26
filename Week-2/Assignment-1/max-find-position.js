function max(numbers) {
  let maxNumber = numbers[0]  // set first number as max
  for (let number of numbers) {  // compare step by step 
    if (maxNumber <= number) {
      maxNumber = number      
    }    
  }
  return maxNumber
}


function findPosition(numbers, target){
  for (let i in numbers) {
    if (numbers[i] === target) {  // when target found
      return i
    }
  }
  return -1  // not found
}

// test run for max
console.log(max([1, 2, 4, 5]))  // 5
console.log(max([5, 2, 7, 1, 6]))  // 7

// test run for findPosition
console.log(findPosition([5, 2, 7, 1, 6], 5))  // 0
console.log(findPosition([5, 2, 7, 1, 6], 7))  // 2
console.log(findPosition([5, 2, 7, 7, 7, 1, 6], 7))  // 2
console.log(findPosition([5, 2, 7, 1, 6], 8))  // -1