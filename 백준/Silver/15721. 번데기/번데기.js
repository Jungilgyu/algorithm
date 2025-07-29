const fs = require("fs");
const input = fs.readFileSync("/dev/stdin").toString().trim().split('\n');

const [a, t, r] = input.map(Number);

let idx = 0; // r(0 또는 1) 구호가 나온 횟수
let turn = 0; // 현재 사람 번호
let cnt = 2;

while (true) {
  const sequence = [0, 1, 0, 1];
  for (let x of sequence) {
    if (x === r) idx++;
    if (idx === t) {
      console.log(turn);
      process.exit();
    }
    turn = (turn + 1) % a;
  }

  for (let i = 0; i < cnt; i++) {
    if (0 === r) idx++;
    if (idx === t) {
      console.log(turn);
      process.exit();
    }
    turn = (turn + 1) % a;
  }

  for (let i = 0; i < cnt; i++) {
    if (1 === r) idx++;
    if (idx === t) {
      console.log(turn);
      process.exit();
    }
    turn = (turn + 1) % a;
  }

  cnt++;
}