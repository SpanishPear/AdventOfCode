
pub fn part1(input: &String) -> u32 {

    let lines: Vec<u32> = input.lines().map(|item| {
        item.parse::<u32>().unwrap()
    }).collect();

    let mut sum =0;
    for num in lines.windows(2) {
        if let &[prev, next] = num {
            if next > prev {
                sum += 1;
            }
        }
    }

    sum
}

pub fn part2(_input: &String) -> u32 {
    4
}
