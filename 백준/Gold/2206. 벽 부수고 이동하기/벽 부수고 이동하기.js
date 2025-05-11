// const input = require('fs').readFileSync('./input.txt', 'utf-8').trim().split('\n')
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n')

const [n, m] = input[0].split(' ').map(Number)

const area = input.slice(1, n+1).map(line => line.trim().split('').map(Number))

const visited = []

for (let i = 0; i < 2; i++) {
	const temp = Array.from( {length: n}, () => Array(m).fill(false))
	visited.push(temp)
} 

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

const q = [[0, 0, 0, 1]]
let pointer = 0

visited[1][0][0] = true
if (n === 1 && m === 1) {
	console.log(1)
} else {
	while (pointer < q.length) {
	const [x, y, dist, chance] = q[pointer++]

	for (let k = 0; k < 4; k++) {
		const nx = x + di[k]
		const ny = y + dj[k]

		if (nx === n-1 && ny === m-1) {
			console.log(dist + 2)
			return
		}

		if (0 <= nx && nx < n && 0 <= ny && ny < m) {
			if (area[nx][ny] === 0 && !visited[chance][nx][ny]) {
				q.push([nx, ny, dist + 1, chance]);
				visited[chance][nx][ny] = true;
			}

			if (area[nx][ny] === 1 && chance === 1 && !visited[0][nx][ny]) {
				q.push([nx, ny, dist + 1, 0]);
				visited[0][nx][ny] = true;
			}
		}
		}
	}

	console.log(-1)
}



