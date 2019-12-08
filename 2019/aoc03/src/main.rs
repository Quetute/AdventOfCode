use std::ops::Add;

static INPUT: &str = include_str!("../input.txt");

type Error = Box<dyn std::error::Error>;
type Result<T, E = Error> = std::result::Result<T, E>;

#[derive(Copy, Clone, Debug)]
struct Point {
    x: i32,
    y: i32,
}

impl Add for Point {
    type Output = Self;

    fn add(self, other: Self) -> Self {
        Self {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

#[derive(Copy, Clone, Debug)]
enum Direction {
    Up,
    Right,
    Left,
    Down,
}

impl Direction {
    fn from(input: &str) -> Direction {
        match input {
            "U" => Direction::Up,
            "D" => Direction::Down,
            "R" => Direction::Right,
            "L" => Direction::Left,
            _ => panic!("haaaa"),
        }
    }
}

#[derive(Copy, Clone, Debug)]
struct Segment {
    p: Point,
    dir: Direction,
    len: i32,
}

impl Segment {
    fn get_left_x(&self) -> i32 {
        match self.dir {
            Direction::Left => self.p.x - self.len,
            _ => self.p.x,
        }
    }

    fn get_right_x(&self) -> i32 {
        match self.dir {
            Direction::Right => self.p.x + self.len,
            _ => self.p.x,
        }
    }

    fn get_up_y(&self) -> i32 {
        match self.dir {
            Direction::Up => self.p.y + self.len,
            _ => self.p.y,
        }
    }

    fn get_down_y(&self) -> i32 {
        match self.dir {
            Direction::Down => self.p.y - self.len,
            _ => self.p.y,
        }
    }

    fn get_end(&self) -> Point {
        match self.dir {
            Direction::Up => Point {
                x: self.p.x,
                y: self.p.y + self.len,
            },
            Direction::Down => Point {
                x: self.p.x,
                y: self.p.y - self.len,
            },
            Direction::Left => Point {
                x: self.p.x - self.len,
                y: self.p.y,
            },
            Direction::Right => Point {
                x: self.p.x + self.len,
                y: self.p.y,
            },
        }
    }
}

fn main() -> Result<()> {
    let paths: Vec<&str> = INPUT.lines().collect();
    let path1: Vec<Segment> = get_segments(paths[0]);
    let path2: Vec<Segment> = get_segments(paths[1]);

    let mut min_dist = i32::max_value();
    let mut min_signal = i32::max_value();

    let mut step1 = 0;
    for s1 in path1 {
        let mut step2 = 0;
        for &s2 in &path2 {
            match is_inter(s1, s2) {
                Some(p) => {
                    println!("{:?}", p);
                    min_dist = min_dist.min(p.x.abs() + p.y.abs());
                    min_signal = min_signal.min(
                        step1
                            + (s1.p.x - p.x + s1.p.y - p.y).abs()
                            + step2
                            + (s2.p.x - p.x + s2.p.y - p.y).abs(),
                    );
                }
                _ => (),
            }
            step2 += s2.len;
        }
        step1 += s1.len;
    }

    println!("distance min: {}", min_dist);
    println!("signal min: {}", min_signal);
    Ok(())
}

fn get_segments(paths: &str) -> Vec<Segment> {
    let paths: Vec<&str> = paths.split(',').collect();
    let mut curr: Point = Point { x: 0, y: 0 };
    let mut ret: Vec<Segment> = vec![];
    for s in paths {
        let seg = get_segment(curr, s);
        ret.push(seg);
        curr = seg.get_end();
    }
    ret
}

fn get_segment(origin: Point, next: &str) -> Segment {
    let (dir, dist) = next.split_at(1);
    let dist: i32 = dist.parse().unwrap();
    return Segment {
        p: origin,
        dir: Direction::from(dir),
        len: dist,
    };
}

fn is_inter(s1: Segment, s2: Segment) -> Option<Point> {
    match s1.dir {
        Direction::Left | Direction::Right => is_inter_with_dir(s1, s2),
        Direction::Down | Direction::Up => is_inter_with_dir(s2, s1),
    }
}

fn is_inter_with_dir(s_hor: Segment, s_vert: Segment) -> Option<Point> {
    if s_hor.get_left_x() < s_vert.get_left_x()
        && s_hor.get_right_x() > s_vert.get_right_x()
        && s_vert.get_down_y() < s_hor.get_down_y()
        && s_vert.get_up_y() > s_hor.get_up_y()
    {
        return Some(Point {
            x: s_vert.p.x,
            y: s_hor.p.y,
        });
    }
    return None;
}
