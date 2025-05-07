const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

const banned = Array.from({ length: n + 1 }, () => Array(n + 1).fill(false));

for (let i =1; i <=m; i++){
	const [a, b] = input[i].split(' ').map(Number);
	banned[a][b] = true;
	banned[b][a] = true;
}

let cnt = 0;

// 3개씩 

for (let i = 1; i <= n; i++) {
	for (let j = i+1; j <= n; j ++) {
		if (banned[i][j]) continue;

		for (let k = j+1; k <= n; k ++) {
			if (banned[i][k] || banned[j][k]) continue;

			cnt += 1;
		}
	}
}

console.log(cnt)







