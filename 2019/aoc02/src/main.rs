static INPUT: &str = include_str!("../input.txt");

type Error = Box<dyn std::error::Error>;
type Result<T, E = Error> = std::result::Result<T, E>;

fn main() -> Result<()> {
    let intcodes: Result<Vec<i128>, _> = INPUT.trim_end().split(',').map(str::parse::<i128>).collect();
    let intcodes = intcodes?;
    part1(&mut intcodes.clone(), 12, 2)?;
    part2(&mut intcodes.clone(), 19690720)?;
    Ok(())
}

fn part1(intcodes: &mut Vec<i128>, param1: i128, param2: i128) -> Result<i128> {
    intcodes[1] = param1;
    intcodes[2] = param2;
    let mut i = 0;
    
    loop {
        let curr = intcodes[i];
        match curr {
            1 => {
                let pos3 = intcodes[i+3] as usize;
                intcodes[pos3] = intcodes[intcodes[i+1] as usize] + intcodes[intcodes[i+2] as usize];
            },
            2 =>  {
                let pos3 = intcodes[i+3] as usize;
                intcodes[pos3] = intcodes[intcodes[i+1] as usize] * intcodes[intcodes[i+2] as usize];
            },
            99 => break,
            _ => println!("Error")
        }
        i += 4;
    }

    println!("{} {} -> {}", param1, param2, intcodes[0]);
    Ok(intcodes[0])
}

fn part2(intcodes: &mut Vec<i128>, output: i128) -> Result<()> {
    let mut max = 0;
    'outer:loop  {
        for i in 0..=max {
            if output == part1(&mut intcodes.clone(), i, max)?{
                println!("({} {})", i, max);
                break 'outer;
            }
            if output == part1(&mut intcodes.clone(), max, i)?{
                println!("({} {})", max, i);
                break 'outer;
            }
        }
        max += 1;
    };
    Ok(())
}
