// Codeforces Problem 50A - Domino piling
// Row-centric solution: M // 2 * N + N // 2 (if M is odd)

use std::io;

fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();

    let nums: Vec<i32> = input
        .trim()
        .split_whitespace()
        .map(|s| s.parse().unwrap())
        .collect();

    let m = nums[0];
    let n = nums[1];

    // Row-centric formula:
    // - M // 2 * N: Complete pairs of rows filled with horizontal dominoes
    // - N // 2: If M is odd, fill the remaining row with vertical dominoes
    let mut result = (m / 2) * n;
    if m % 2 == 1 {
        result += n / 2;
    }

    println!("{}", result);
}
