use std::collections::HashMap;

static INPUT: &str = include_str!("../input.txt");

fn main() {
    let mut map = HashMap::new();
    let orbits: Vec<&str> = INPUT.lines().collect();
    for orbit in orbits {
        let orbit: Vec<&str> = orbit.split(')').collect();
        let planet1: &str = orbit.get(0).unwrap();
        let planet2: &str = orbit.get(1).unwrap();
        map.insert(planet2.to_string(), planet1.to_string());
    }

    let mut orbit_count = HashMap::new();
    let mut total = 0;
    for planet in map.keys() {
        let mut count = 0;
        let mut curr = planet;
        while map.contains_key(curr) {
            match orbit_count.get(curr) {
                Some(c) => {
                    count += c;
                    break;
                }
                None => count += 1,
            }
            curr = map.get(curr).unwrap();
        }
        orbit_count.insert(planet, count);
        total += count;
    }

    println!("part1: {}", total);

    let mut path_from_you = HashMap::new();
    let mut count = 0;
    let mut curr = map.get("YOU").unwrap();

    loop {
        match map.get(curr) {
            Some(p) => {
                path_from_you.insert(curr, count);
                count += 1;
                curr = p;
            }
            None => break,
        }
    }

    let mut curr = map.get("SAN").unwrap();
    let mut count = 1;
    loop {
        match map.get(curr) {
            Some(p) => match path_from_you.get(p) {
                Some(c) => {
                    println!("part2: {}", c + count);
                    break;
                }
                None => {
                    count += 1;
                    curr = p;
                }
            },
            None => panic!("haaaa"),
        }
    }
}
