//Attempt at recreating the Lotty Analyser I made in Python in Rust. Not sure 
//why, but it seems like a lark. 
//by Gwen Virtue

use random::Rng; //for making the randoms

fn main() {
	let mut rng = rand::thread_rng();

	let my_ticket = [0, 0, 0, 0, 0];
	let guess_ticket = [0, 0, 0, 0, 0];

	for i in my_ticket {
		my_ticket[i] = rnd.gen_range(1..11);
	}
	
	for i in guess_ticket {
		guess_ticket[i]= rnd.gen_range(1..11);
	}
}
