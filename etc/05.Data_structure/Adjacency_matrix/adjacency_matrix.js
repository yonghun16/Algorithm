class Graph {
  constructor(size) {
    this.size = size;
    this.adjMatrix = Array.from({ length: size }, () => Array(size).fill(0));
  }

  // 간선 추가 (무방향 그래프)
  addEdge(u, v, weight = 1) {
    this.adjMatrix[u][v] = weight;
    this.adjMatrix[v][u] = weight;  // 방향 그래프면 이 줄 제거
  }

  // 간선 제거
  removeEdge(u, v) {
    this.adjMatrix[u][v] = 0;
    this.adjMatrix[v][u] = 0;
  }

  // 인접 행렬 출력
  printMatrix() {
    console.log('Adjacency Matrix:');
    for (let row of this.adjMatrix) {
      console.log(row.join(' '));
    }
  }
}


const graph = new Graph(5); // 정점 5개 (0~4)

graph.addEdge(0, 1);
graph.addEdge(0, 2);
graph.addEdge(1, 2);
graph.addEdge(3, 4);

graph.printMatrix();

/*
결과:
Adjacency Matrix:
0 1 1 0 0
1 0 1 0 0
1 1 0 0 0
0 0 0 0 1
0 0 0 1 0
*/
