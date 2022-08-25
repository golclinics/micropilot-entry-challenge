const countZero = (A) => {
   let number_of_zeros = 0
   for (let num of A) {
      if (num === 0) {
         number_of_zeros++
      }
   }
   return number_of_zeros
}

console.log(countZero([1, 0, 5, 0, 0, 0]))