fn main() {
    let min = 372037;
    let max = 905157;

    let mut count = 0; 
    'outer: for i in min..=max {
        let s = i.to_string();
        let mut s = s.chars();
        let mut prev = s.next().unwrap();
        let mut adj_same = false;
        let mut count_same = 0;
        for c in s {
            if prev.to_digit(10) > c.to_digit(10){
                continue 'outer;
            }

            if prev == c {
                count_same += 1;
            } else {
                if count_same == 1 {
                    adj_same = true;
                }
                count_same = 0;
            }
            prev = c;
        }

        if count_same == 1 || adj_same {
            count += 1;
        }
    }
    println!("{}", count);
}
