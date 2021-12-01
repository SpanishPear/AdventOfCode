pub fn part1(input: String) {
    let lines: Vec<_> = include_str!("input_a.txt").lines().collect::<Result<_, _>>().unwrap();
    let mut sum = 0;

    for window in lines.windows(2) {


        &println!{"[{}, {}]", window[0].parse::<i32>().unwrap(), window[1]};
        // if next.parse::<i32>().unwrap() > prev.parse::<i32>().unwrap() {
        //     sum += 1;
        // }
    }

    println!("{}", sum);
    println!("{}", input.chars().rev().collect::<String>());
}