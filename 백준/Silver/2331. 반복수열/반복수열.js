// const input = require('fs').readFileSync('./input.txt', 'utf-8').trim().split('\n');
const input = require("fs").readFileSync('/dev/stdin').toString().trim().split('\n');
// console.log(input)
const [a, p] = input[0].split(" ").map(Number);

// console.log(a, p);

let arr = [a]
let repeatStartIndex = -1;
let temp = a.toString()
while (true) {
	let num = 0;
	for (let i = 0; i < temp.length; i++) {
		const x = parseInt(temp[i])
		num += x**p
	}

	if (arr.includes(num)) {
		repeatStartIndex = arr.indexOf(num);
		break;
	} else {
		arr.push(num)
	}

	temp = num.toString()
}


const answer = arr.slice(0, repeatStartIndex);
// console.log(answer);
console.log(answer.length);



// console.log(arr);

// 57, 74, 65, 61, '37, 58, 89, 145, 42, 20, 4, 16', '37, 58, 89,...'


