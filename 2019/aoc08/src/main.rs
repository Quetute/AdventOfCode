static INPUT: &str = include_str!("../input.txt");

fn main() {
    let mut digits: Vec<u8> = INPUT.trim_end().chars().map(|c| c.to_digit(10).unwrap() as u8).collect();

    let mut layers = vec![];
    let mut min0 = std::u32::MAX;
    let mut ret = 0;
    loop {
        let mut layer = vec![];
        let mut count0 = 0;
        let mut count1 = 0;
        let mut count2 = 0;
        for _ in 0..6 {
            let mut row = vec![];
            for _ in 0..25 {
                let elt = digits.remove(0); 
                row.push(elt);
                match elt { 
                    0 => count0 += 1,
                    1 => count1 += 1,
                    2 => count2 += 1,
                    _ => ()
                }
            }
            layer.push(row);
        }
        if count0 < min0 {
            min0 = count0;
            ret = count1 * count2;
        }
        layers.push(layer);
        if digits.is_empty(){
            break;
        }
    }
    println!("part1: {}", ret);

    let mut img = String::default();
    for i in 0..6 {
        'pixel:for j in 0..25 {
            for layer in &layers {
                match layer.get(i).unwrap().get(j).unwrap() {
                    2 => (),
                    v => {
                        print!("{}", *v);
                        img.push(*v as char);
                        break;
                    }
                }
            }
        }
        println!("");
        img.push('\n');
    }
}
