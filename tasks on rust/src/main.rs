
fn first() {
    let mut total:i64 = 0;

    for i in 1..1000 {
        if i % 3 == 0 || i % 5 == 0 {
            total += i;
        }
    }

    println!("#1 The sum of all the multiples of 3 or 5 below 1000 is {}", total);
}



fn third() {
    let mut n:i64 = 600851475143;
    let mut largest_factor = 1;

    while n % 2 == 0 {
        largest_factor = 2;
        n /= 2;
    }

    let mut i = 3;
    let mut max_factor = (n as f64).sqrt().floor() as i64;

    while i <= max_factor {
        while n % i == 0 {
            largest_factor = i;
            n /= i;
        }

        i += 2;
        max_factor = (n as f64).sqrt().floor() as i64;
    }

    if n > 2 {
        largest_factor = n;
    }

    println!("#3 The largest prime factor of 600851475143 is {}", largest_factor);
}

fn third_two() {
    let mut n: i64 = 600851475143;
    let mut i = 2;

    while i * i <= n {
        while n % i == 0 {
            n /= i;
        }
        i += 1;
    }

    println!("#3 variant two {}", n);
}




fn fifth() {
    let mut n = 20;

    while (1..=20).all(|i| n % i == 0) {
        n += 20;
    }

    println!("# 5 The smallest positive number that is evenly divisible by all of the numbers from 1 to 20 is {}", n);
}




fn seventh() {
    let mut primes = vec![true; 10001];
    primes[0] = false;
    primes[1] = false;

    for i in 2..10001 {
        if primes[i] {
            let mut j = i * i;
            while j < 10001 {
                primes[j] = false;
                j += i;
            }
        }
    }

    let mut count = 0;
    for i in 2..10001 {
        if primes[i] {
            count += 1;
            if count == 10001 {
                println!("#7 The 10,001st prime number is {}", i);
                break;
            }
        }
    }
}


fn ninth() {
    for a in 1..1000 {
        for b in a..1000 {
            let c = 1000 - a - b;
            if a*a + b*b == c*c {
                println!("# 9 {}", a*b*c);
                return;
            }
        }
    }
}

fn main(){
    first();
    third();
    third_two();
    fifth();
    seventh();
    ninth();

}

