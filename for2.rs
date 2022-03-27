//Testing for loops for fun and profit. GV

fn main() {
	for i in 0..5 {
		if i % 2 == 0 { //So far so Python, except for the C stytle { }
			println!("even {}", i);
		}
		else {
			println!("odd {}", i);
		}
	}
}
