fn count_zeros(nums: Vec<i32>) -> i32 {
    let mut sum = 0;

    for num in nums {
        if num == 0 {
            sum += 1;
        }
    }

    sum

}

fn main() {
    let arr = vec![1, 0, 5, 6, 0, 2, 0];
    let solution =  count_zeros(arr);
    println!("The number of zeros are {}", solution)
}
