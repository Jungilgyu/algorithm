const input = require("fs").readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);

const dna = input.slice(1, 1+n).map(line => line.split(''));



// 열 별로 가장 많이 중복된 문자로 dna를 만들기

let answer = '';
let answerCnt = 0

for (j=0; j<m; j++){
	dict = {'T': 0, 'A':0, 'G':0, 'C':0}
	for (i=0; i<n; i++){
		dict[dna[i][j]] += 1
	}

	let maxKey = '';
	let maxVal = -1;
	for (let key in dict) {
		if (dict[key] > maxVal || (dict[key] === maxVal && key < maxKey)) {
			maxVal = dict[key];
			maxKey = key
		}
	}

	answer += maxKey
	
}

for (i=0; i<n; i++){
	for (j=0; j<m; j++){
		if (answer[j] != dna[i][j]) {
			answerCnt += 1
		}
	}
}

console.log(answer);
console.log(answerCnt);




