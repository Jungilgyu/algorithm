# [Silver V] 번데기 - 15721 

[문제 링크](https://www.acmicpc.net/problem/15721) 

### 성능 요약

메모리: 9332 KB, 시간: 88 ms

### 분류

구현, 브루트포스 알고리즘, 시뮬레이션

### 제출 일자

2025년 5월 7일 17:25:44

### 문제 설명

<p>중앙대학교 소프트웨어학부에 새로 입학한 19학번 새내기 일구는 새내기 새로 배움터에 가서 술게임을 여러 가지 배웠다. 그 중 가장 재미있었던 게임은 바로 번데기 게임이었다.</p>

<p>번데기 게임의 규칙은 다음과 같다. ‘뻔 – 데기 – 뻔 – 데기 – 뻔 – 뻔 – 데기 – 데기’ 를 1회차 문장이라고 하자. 2회차 문장은 ‘뻔 – 데기 – 뻔 - 데기 – 뻔 – 뻔 – 뻔 – 데기 – 데기 – 데기’가 된다. 즉 n-1회차 문장일 때는 ‘뻔 – 데기 – 뻔 – 데기 – 뻔(x n번) – 데기(x n번)’이 된다. 하이픈 사이를 지날 때마다 순서는 다음 사람으로 넘어간다. 원을 돌아 다시 일구 차례가 와도 게임은 계속 진행된다.</p>

<p>일구와 동기들, 그리고 선배들을 포함한 사람 A명이 다음과 같이 원으로 앉아 있다고 가정하자. </p>

<p style="text-align: center;"><img alt="" src="https://onlinejudgeimages.s3-ap-northeast-1.amazonaws.com/problem/15721/1.png" style="width: 227px; height: 197px;"></p>

<p>일구가 0번째이고, 반 시계 방향으로 번데기 게임을 진행한다. T번째 ‘뻔’ 또는 ‘데기’를 외치는 사람은 위 원에서 몇 번 사람인지를 구하여라. (새내기는 10000번째가 되는 순간 시체방에 가기 때문에 T는 10000이하의 임의의 자연수이다.)</p>

### 입력 

 <p>첫째 줄에 게임을 진행하는 사람 A명이 주어진다. A는 2,000보다 작거나 같은 자연수이다.</p>

<p>둘째 줄에는 구하고자 하는 번째 T가 주어진다. (T ≤ 10000)</p>

<p>셋째 줄에는 구하고자 하는 구호가 “뻔”이면 0, “데기”면 1로 주어진다. </p>

### 출력 

 <p>첫째 줄에 구하고자 하는 사람이 원탁에서 몇 번째에 있는지 정수로 출력한다. </p>

