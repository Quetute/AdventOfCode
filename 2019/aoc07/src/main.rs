use std::collections::VecDeque;

static INPUT: &str = include_str!("../input.txt");

type Error = Box<dyn std::error::Error>;
type Result<T, E = Error> = std::result::Result<T, E>;

fn main() -> Result<()> {
    let intcodes: Result<Vec<i32>, _> = INPUT.trim_end().split(',').map(str::parse::<i32>).collect();
    let intcodes = intcodes?;
    let mut max = 0;
    let permutations = get_permutations(&mut (5..=9).collect());
    for permutation in permutations {
        let mut amplifiers = vec![];
        for phase_setting in permutation {
            let amplifier = Amplifier::new(intcodes.clone(), phase_setting);
            amplifiers.push(amplifier);
        }
        let mut input = 0;
        let mut stop = false;
        while !stop {
            for amplifier in &mut amplifiers {
                println!("===== TRANSISTOR =====");
                match amplifier.generate_with_input(input) {
                    Some(i) => input = i,
                    None => stop = true
                }
            }
            println!("===== FEEDBACK LOOP =====");
        }

        if max < input {
            max = input;
        }
    }
    println!("{}", max);
    Ok(())
}

fn get_permutations(inputs: &mut Vec<i32>) -> Vec<Vec<i32>> {
    let elt = inputs.pop().unwrap();
    if inputs.len() == 0 {
        return vec![vec![elt]];
    }

    let mut ret = vec![];
    let perms_to_fill = get_permutations(inputs);
    for perm in perms_to_fill {
        for i in 0..=perm.len(){
            let mut new_perm = perm.clone();
            new_perm.insert(i, elt);
            ret.push(new_perm);
        }
    }
    ret
}

struct Amplifier {
    intcodes: Vec<i32>,
    pointer: usize,
    inputs: VecDeque<i32>
}

impl Amplifier {

    pub fn new(intcodes: Vec<i32>, phase_setting: i32) -> Amplifier {
        let mut a = Amplifier {
            intcodes: intcodes,
            inputs: VecDeque::new(),
            pointer: 0,
        };

        a.inputs.push_front(phase_setting);

        a
    }

    fn generate(&mut self) -> Option<i32>{
        return int_code_with_pointer(&mut self.intcodes, &mut self.inputs, &mut self.pointer);
    }

    fn generate_with_input(&mut self, input: i32) -> Option<i32>{
        self.inputs.push_front(input);
        return self.generate();
    }
}

fn int_code_with_pointer(intcodes: &mut Vec<i32>, inputs: &mut VecDeque<i32>, pointer: &mut usize) -> Option<i32> {
    loop {
        let instruction = intcodes[*pointer];
        let opcode = instruction % 100;
        println!("opcode: {}", opcode);
        match opcode {  
            1 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, *pointer);
                let write_to = intcodes[*pointer + 3] as usize;
                intcodes[write_to] = param1 + param2;
                println!("{} wrote to {}", intcodes[write_to], write_to);
                *pointer += 4;
            },
            2 =>  {
                let (param1, param2) = get_two_parameters(intcodes, instruction, *pointer);
                let write_to = intcodes[*pointer+3] as usize;
                intcodes[write_to] = param1 * param2;
                println!("{} wrote to {}", intcodes[write_to], write_to);
                *pointer += 4;
            },
            3 => {
                let write_to = intcodes[*pointer+1] as usize;
                intcodes[write_to] = inputs.pop_back().unwrap();
                println!("{} wrote to {}", intcodes[write_to], write_to);
                *pointer += 2;
            }
            4 => {
                let output = Mode::get((instruction / 100) % 10).get_value(intcodes, *pointer+1);
                *pointer += 2;
                println!("output: {}", output);
                return Some(output);
            }
            5 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, *pointer);
                *pointer = if param1 != 0 {param2 as usize } else  {*pointer + 3};
                println!("position of next instruction: {}", *pointer);
            }
            6 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, *pointer);
                *pointer = if param1 == 0 {param2 as usize } else  {*pointer + 3};
                println!("position of next instruction: {}", *pointer);
            }
            7 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, *pointer);
                let write_to = intcodes[*pointer+3] as usize;
                intcodes[write_to] = if param1 < param2 { 1 } else  {0};
                println!("{} wrote to {}", intcodes[write_to], write_to);
                *pointer += 4;
            }
            8 => {
                let (param1, param2) = get_two_parameters(intcodes, instruction, *pointer);
                let write_to = intcodes[*pointer+3] as usize;
                intcodes[write_to] = if param1 == param2 { 1 } else  {0};
                println!("{} wrote to {}", intcodes[write_to], write_to);
                *pointer += 4;
            }
            99 => return None,
            _ => panic!("Unkown intcode")
        }
        println!("");
    }
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
