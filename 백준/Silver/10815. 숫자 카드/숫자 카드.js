const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const myCards = input[1].split(' ').map(Number);
const m = Number(input[2]);
const target = input[3].split(' ').map(Number);



const dict = {}

for (let i = 0; i < n; i++) {
	if (myCards[i] in dict) {
		dict[myCards[i]] += 1
	} else {
		dict[myCards[i]] = 1
	}
}

let answer = []

for (let i = 0; i < m; i++) {
	if (target[i] in dict) {
		answer.push(1)
	} else {
		answer.push(0)
	}
}

console.log(answer.join(' '));


