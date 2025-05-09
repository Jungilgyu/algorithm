// const input = require('fs').readFileSync('./input.txt', 'utf-8').trim().split('\n');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0])

const area = input.slice(1).map(line => line.trim().split(''));

const answer = Array.from({length: n}, () => Array(n).fill(0))
// console.log(area);

// 1. 8방향 탐사 
const di = [-1, -1, 0, 1, 1, 1, 0, -1]
const dj = [0, 1, 1, 1, 0, -1, -1, -1]

for (let i = 0; i < n; i++) {
	for (let j = 0; j < n; j++) {
		// area[i][j]가 숫자인지, '.'인지 판별 
		if (area[i][j] === '.') {
			// 숫자가아니면 8방향 탐사
			let sum = 0;
			for (let k = 0; k < 8; k++) {
				const ni = i + di[k]
				const nj = j + dj[k]
				if (0 <= ni && ni < n  && 0 <= nj && nj < n && (area[ni][nj] != '.')) {
					// 주변에 있는 area[ni][nj]가 범위안이고, '.'이 아니면
					sum += Number(area[ni][nj]);
				}
			}
			answer[i][j] = sum >= 10 ? 'M' : String(sum);

		} else {
			// 숫자면 => answer에 지뢰표시
			answer[i][j] = '*'
		}
	}
}

for (let i = 0; i < n; i++) {
	console.log(answer[i].join(''));
}

