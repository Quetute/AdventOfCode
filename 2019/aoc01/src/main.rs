static INPUT: &str = include_str!("../input.txt");

type Error = Box<dyn std::error::Error>;
type Result<T, E = Error> = std::result::Result<T, E>;

fn main() -> Result<()> {
    let modules: Result<Vec<i128>, _> = INPUT.lines().map(str::parse::<i128>).collect();
    let modules = modules?;
    part1(&modules)?;
    part2(&modules)?;
    Ok(())
}

fn part1(modules: &Vec<i128>) -> Result<()> {
    let mut sum = 0;
    for module in modules {
        sum += module / 3 - 2;
    }
    println!("{}", sum);
    Ok(())
}

fn part2(modules: &Vec<i128>) -> Result<()> {
    let mut sum = 0;
    for module in modules {
        let mut curr = module / 3 - 2;
        while curr > 0 {
            sum += curr;
            curr = curr / 3 - 2;
        }
    }

    println!("{}", sum);
    Ok(())
}
