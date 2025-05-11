// const input = require('fs').readFileSync('./input.txt', 'utf-8').trim().split('\n');
const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);

for (let tc = 0; tc < T; tc++) {
	const order = input[tc*3 + 1].trim()
	const n = Number(input[tc*3 + 2])
	const arr = JSON.parse(input[tc*3 + 3])

	let front = 0;
  let rear = arr.length;
  let reversed = false;
  let isError = false;

	for (let cmd of order) {
    if (cmd === 'R') {
      reversed = !reversed;
    } else { // D
      if (front >= rear) {
        isError = true;
        break;
      }
      if (reversed) {
        rear--; // 뒤에서 제거
      } else {
        front++; // 앞에서 제거
      }
    }
  }

  if (isError) {
    console.log("error");
  } else {
    const result = arr.slice(front, rear);
    if (reversed) result.reverse();
    console.log("[" + result.join(",") + "]");
  }
}

 
