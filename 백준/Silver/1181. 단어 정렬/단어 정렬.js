// const input = require('fs').readFileSync('./input.txt', 'utf-8').trim().split('\n');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = parseInt(input[0])

// console.log(n);

const arr = []

for (let i = 1; i <= n; i++) {
	arr.push(input[i].trim())
}

const uniqueArr = [...new Set(arr)];

uniqueArr.sort((a, b) => {
	if (a.length !== b.length) {
		return a.length - b.length;
	} else {
		return a.localeCompare(b);
	}
})

for (const str of uniqueArr) {
	console.log(str)
}
