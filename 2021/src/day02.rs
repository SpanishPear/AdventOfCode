use regex::bytes::Split;

pub fn part1(input: &String) -> u32 {

    let lines: Vec<(&str, u32)> = input.lines().map(|item| {
        let mut split = item.split(" ");
        (split.next().unwrap(), split.next().unwrap().parse::<u32>().unwrap())
    }).collect();


    let mut horizontal =0;
    let mut depth = 0;
    for (direction, magnitude) in lines {
        match direction  {
            "forward" => horizontal += magnitude,
            "up" => depth -= magnitude,
            "down" => depth += magnitude,
            "right" => horizontal -= magnitude,
            _ => unreachable!()
        }
    }

    horizontal * depth

}


pub fn part2(input: &String) -> u32 {
    let lines: Vec<(&str, u32)> = input.lines().map(|item| {
        let mut split = item.split(" ");
        (split.next().unwrap(), split.next().unwrap().parse::<u32>().unwrap())
    }).collect();


    let mut horizontal =0;
    let mut depth = 0;
    let mut aim = 0;
    for (direction, magnitude) in lines {
        match direction  {
            "forward" => {
                horizontal += magnitude;
                depth += aim * magnitude;
            },
            "up" => aim -= magnitude,
            "down" => aim += magnitude,
            "right" => {
                horizontal -= magnitude;
                depth -= aim * magnitude;
            },
            _ => unreachable!()
        }
    }

    horizontal * depth
}