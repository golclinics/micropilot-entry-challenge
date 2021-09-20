fn main() {}

fn count_zeros(arr: &[u32]) -> u32 {
    let mut counter = 0;
    for nums in arr {
        match nums {
            0 => counter += 1,
            _ => (),
        }
    }
    counter
}

#[test]
fn two_zeros() {
    let arr = [1, 0, 5, 6, 0, 2];
    let res = count_zeros(&arr);
    assert_eq!(res, 2)
}

#[test]
fn no_zero() {
    let arr = [13, 34, 23, 23523];
    let res = count_zeros(&arr);
    assert_eq!(res, 0)
}
