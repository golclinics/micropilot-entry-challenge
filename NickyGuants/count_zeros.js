function numberOfZeros(array) {
    //Initialize an empty array to hold all the zeros in the array.
    let zeros = [];
    // Traverse/ loop through the array checking whether eaxh element is a zero
    for(let i = 0; i < array.length; i ++){
        //For every zero encountered, push the zero to the array containing zeros
        if(array[i] === 0) {
            zeros.push(array[i]);
        }
    }
    //Find the length of the array containing the zeros which is the number of zeros in the orinal array
    console.log(zeros.length);
}
//Test the function
numberOfZeros([0, 4, 0, false, 5, 0, 0, 0, 0, 0, 'H', "You"]);