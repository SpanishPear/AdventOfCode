use std::env;
use std::io;

use advent_of_code::*;

macro_rules! run_day {
    ($day:path, $input:expr) => {{
        use $day::*;
        println!(
            "{}: part1 = {:?}, part2 = {:?}",
            stringify!($day),
            part1($input),
            part2($input)
        );
    }};
}

fn main() {
    // Get day string
    let args: Vec<String> = env::args().collect();
    let mut day = String::new();

    if args.len() >= 2 {
        day = args[1].clone();
    } else {
        println!("Enter day: ");
        io::stdin()
            .read_line(&mut day)
            .expect("Failed to read line");
    }

    // Parse day as number
    day = day.trim().to_string();
    let day_num: u8 = match day.parse() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid day number: {}", day);
            return;
        }
    };

    let input = read_input(day_num);

    match day_num {
        1 => run_day!(day01, &input),
        2 => run_day!(day02, &input),
        _ => println!("Invalid day number: {}", day_num),
    }
}
