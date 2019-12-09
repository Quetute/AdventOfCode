static INPUT: &str = include_str!("../input.txt");

type Error = Box<dyn std::error::Error>;
type Result<T, E = Error> = std::result::Result<T, E>;

fn main() -> Result<()> {
    let intcodes: Result<Vec<i32>, _> = INPUT.trim_end().split(',').map(str::parse::<i32>).collect();
    let intcodes = intcodes?;
    //int_code(&mut intcodes.clone(), 1)?;
    int_code(&mut intcodes.clone(), 5)?;
    Ok(())
}

fn int_code(intcodes: &mut Vec<i32>, input: i32) -> Result<()> {
    let mut i = 0;
    loop {
        let instruction = intcodes[i];
        let opcode = instruction % 100;
        println!("opcode: {}", opcode);
        match opcode {  
            1 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, i);
                let write_to = intcodes[i+3] as usize;
                intcodes[write_to] = param1 + param2;
                println!("{} wrote to {}", intcodes[write_to], write_to);
                i += 4;
            },
            2 =>  {
                let (param1, param2) = get_two_parameters(intcodes, instruction, i);
                let write_to = intcodes[i+3] as usize;
                intcodes[write_to] = param1 * param2;
                println!("{} wrote to {}", intcodes[write_to], write_to);
                i += 4;
            },
            3 => {
                let write_to = intcodes[i+1] as usize;
                intcodes[write_to] = input;
                println!("{} wrote to {}", intcodes[write_to], write_to);
                i += 2;
            }
            4 => {
                let output = Mode::get((instruction / 100) % 10).get_value(intcodes, i+1);
                i += 2;
                println!("output: {}", output);
            }
            5 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, i);
                i = if param1 != 0 {param2 as usize } else  {i + 3};
                println!("position of next instruction: {}", i);
            }
            6 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, i);
                i = if param1 == 0 {param2 as usize } else  {i + 3};
                println!("position of next instruction: {}", i);
            }
            7 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, i);
                let write_to = intcodes[i+3] as usize;
                intcodes[write_to] = if param1 < param2 { 1 } else  {0};
                println!("{} wrote to {}", intcodes[write_to], write_to);
                i += 4;
            }
            8 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, i);
                let write_to = intcodes[i+3] as usize;
                intcodes[write_to] = if param1 == param2 { 1 } else  {0};
                println!("{} wrote to {}", intcodes[write_to], write_to);
                i += 4;
            }
            99 => break,
            _ => println!("Error")
        }
        println!("");
    }
    Ok(())
}

fn get_two_parameters(intcodes: &Vec<i32>, instruction: i32, i: usize) -> (i32, i32) {
    println!("instruction: {}", instruction);

    let param1 = Mode::get((instruction / 100) % 10).get_value(intcodes, i+1);
    let param2 = Mode::get((instruction / 1000) % 10).get_value(intcodes, i+2);

    println!("first: mode {}, value {}, param {}", (instruction / 100) % 10, intcodes[i+1], param1);
    println!("second: mode {}, value {}, param {}", (instruction / 1000) % 100, intcodes[i+2], param2);

    (param1, param2)
}
enum Mode {
    Position,
    Immediate
}

impl Mode {
    fn get(mode: i32) -> Mode{
        match mode {
            0 => Mode::Position,
            1 => Mode::Immediate,
            _ => panic!("haaaa")
        }
    }

    fn get_value(&self, intcodes: &Vec<i32>, idx: usize) -> i32 {
        let mut idx = idx;
        match self {
            Mode::Position => idx = intcodes[idx] as usize,
            _ => ()
        }
        intcodes[idx]
    }
}
