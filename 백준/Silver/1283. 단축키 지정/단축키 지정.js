// const input = require('fs').readFileSync('./input.txt', 'utf-8').trim().split('\n');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const n = Number(input[0])

// 단축키 
const usedKeys = new Set();

const answer = []

for (let i = 1; i <= n; i ++) {
	const words = input[i].split(' ').map(word => word.replace('\r', ''))
	let hasAssigned = false;

	for (let j = 0; j < words.length; j++) {
		const firstChar = words[j][0].toLowerCase()
		if (!usedKeys.has(firstChar)) {
			usedKeys.add(firstChar);
			words[j] = `[${words[j][0]}]` + words[j].slice(1);
			hasAssigned = true;
			break
		}
	}

	if(!hasAssigned) {
		outer : {
			for (let j = 0; j < words.length; j++) {
				for (let k = 0; k < words[j].length; k++) {
					const ch = words[j][k].toLowerCase()
					if (!usedKeys.has(ch)) {
						usedKeys.add(ch);
						words[j] = words[j].slice(0, k) + `[${words[j][k]}]` + words[j].slice(k+1);
						break outer;
					}
				}
			}
		}
	}

	answer.push(words.join(' '));
}

console.log(answer.join('\n'));

// 1. 단어 덩어리로 첫 번째 문자들 확인 
// 2. 첫 문자가 이미 단축키로 지정됐으면, 일반단어들도 확인
// 3. 단축키 지정이 불가능하면 패스 
