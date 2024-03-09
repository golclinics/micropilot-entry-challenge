function countZeros(A) {
    let count = 0;  // Initialize count of zeros
    for (let number of A) {  // Loop through each element in the array
        if (number === 0) {  // Check if the element is zero
            count++;  // Increment the count if a zero is found
        }
    }
    return count;  // Return the total count of zeros
}

// Example usage
const A = [1, 0, 5, 6, 0, 2];
const result = countZeros(A);
console.log(result);  // Output should be 2
