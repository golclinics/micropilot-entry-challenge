//Creating dummy array input
let nums = [1,0,9,8,7];

//Creating count function
const countZeros = (nums) => {
  //Initiate sum variable
  let sum = 0;

  //Initaiting a for loop
  for (let i = 0; i < nums.length; i++) {
    if(nums[i]===0){
        sum=sum+1
    }
  }
  return sum
};

//Displaying the output
console.log(countZeros(nums));
