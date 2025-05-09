// const input = require('fs').readFileSync('./input.txt', 'utf-8').trim().split('\n');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0])

const area = input.slice(1).map(line => line.trim().split(''));

const di = [0, 1, 0, -1]
const dj = [1, 0, -1, 0]

const visited = Array.from({length: n}, () => Array(n).fill(false));

function bfs(i, j) {
	const q = []
	q.push([i, j])
	visited[i][j] = true
	let idx = 0 // q의 시작 인덱스
	let res = 1
	while (idx < q.length) {
		const [x, y] = q[idx++]

		for (let k = 0; k < 4; k++) {
			const nx = x + di[k]
			const ny = y + dj[k]
			if ( 0 <= nx && nx < n && 0 <= ny && ny < n && !visited[nx][ny] && area[nx][ny] === '1') {
				visited[nx][ny] = true
				q.push([nx, ny])
				res += 1
			}

		}
	}

	return res
}

const answer = []
for (let i = 0; i < n; i++) {
	for (let j = 0; j < n; j++) {
		if (area[i][j] === '1' && !visited[i][j]) {
			answer.push(bfs(i, j))
		}
	}
}

answer.sort((a, b) => a - b)

console.log(answer.length)
for (const num of answer) {
	console.log(num)
}


