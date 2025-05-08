const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0])

const dict = {}

for (let i = 1; i <= n; i++){
	const [name, stateRaw] = input[i].split(' ')
	const state = stateRaw.trim();

	if (state === "enter") {
		dict[name] = 1
	} else {
		dict[name] = 0
	}

}

const result = Object.keys(dict).filter(name => dict[name] === 1)

result.sort().reverse();

console.log(result.join('\n'));
