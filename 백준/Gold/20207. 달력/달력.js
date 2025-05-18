const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0])

const schedule = []
let max_day = 0
for (let i = 1; i <= n; i++) {
	const [s, e] = input[i].split(' ').map(Number)
	max_day = Math.max(e, max_day)
	schedule.push([s, e])
}

cal = new Array(max_day + 1).fill(0);

for (let j = 0; j < n; j++) {
	const [s, e] = schedule[j]
	for (let k = s; k < e+1; k++) {
		cal[k] += 1
	}
}

let height = 0
let width = 0
let ans = 0

for (const num of cal) {
	if (num === 0) {
		ans += height * width
		height = 0
		width = 0
	} else {
		width += 1
		height = Math.max(height, num)
	}
}

ans += height * width
console.log(ans);