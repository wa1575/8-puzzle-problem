# 8-puzzle-problem
solve the 8-puzzle problem using A* python


 4 rules
	   - blank move upward
	   - move blank downward
	   - move blank to the right
	   - move blank to the ledt


 문제 해결을 위해 구현한 클래스와 함수들은 다음과 같습니다. 이러한 기능들을 활용해 A* 알고리즘을 구현하고, 이를 바탕으로 메인 프로세스에서 8-Puzzle 문제를 해결할 수 있습니다. 

 Code Review
　　  1) Node 클래스 : 해당 문제 풀이의 기본이 되는 자료구조를 생성합니다.
	   - generate_child( ) : 각 네 방향으로 이동하는 자식 노드들을 생성합니다.
	   - shuffle( puz, x1, y1, x2, y2 ) : 주어진 방향으로 blank(_)를 이동시킵니다.
	   - copy( root ) : 주어진 노드를 기반으로 행렬을 작성합니다.
	   - find( puz, x ): 퍼즐 내에서 지정한 요소를 찾습니다.
	
　　  2) Puzzle 클래스 : 과제의 rule을 적용한 퍼즐 게임 클래스입니다.
	   - accept( ) : 사용자로부터 퍼즐을 입력받습니다.
	   - showf( start, goal ) : hueristic value f(x)를 출력합니다.
	   - f( start, goal ) : hueristic value f(x) = h(x) + g(x)를 계산합니다.
  	   - h( start, goal ) : 처음 퍼즐과 목표 퍼즐사이의 차이점을 계산합니다.
  	   - process( ) : 프로그램 메인 프로세스 입니다.


