"""Node 클래스: 해당 문제 풀이의 기본이 되는 자료구조를 형성합니다. """
class Node:
    def __init__(self, data, level, fval):
        """노드를 초기화 합니다. 입력된 data와 level, f(x)의 값을 넣습니다 """
        self.data = data
        self.level = level
        self.fval = fval

    def generate_child(self):
        """ 각 네 방향으로 이동하는 자식 노드들을 생성합니다. """
        x, y = self.find(self.data, '_')
        """ 추정값을 저장할 배열을 만들고, 빈 퍼즐(_)을 이동시키기 위한 위치 값을 넣습니다. """
        val_list = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
        children = []
        for i in val_list:
            child = self.shuffle(self.data, x, y, i[0], i[1])
            if child is not None:
                child_node = Node(child, self.level + 1, 0)
                children.append(child_node)
        return children

    def shuffle(self, puz, x1, y1, x2, y2):
        """ 주어진 방향으로 blank(_)를 이동시킵니다. """
        if x2 >= 0 and x2 < len(self.data) and y2 >= 0 and y2 < len(self.data):
            temp_puz = []
            temp_puz = self.copy(puz)
            temp = temp_puz[x2][y2]
            temp_puz[x2][y2] = temp_puz[x1][y1]
            temp_puz[x1][y1] = temp
            return temp_puz
        else:
            return None

    def copy(self, root):
        """ 주어진 노드를 기반으로 행렬을 작성합니다."""
        temp = []
        for i in root:
            t = []
            for j in i:
                t.append(j)
            temp.append(t)
        return temp

    def find(self, puz, x):
        """ 퍼즐 내에서 지정한 요소를 찾습니다. """
        for i in range(0, len(self.data)):
            for j in range(0, len(self.data)):
                if puz[i][j] == x:
                    return i, j

"""Puzzle 클래스 : 과제의 rule을 적용한 퍼즐 게임 클래스입니다. """
class Puzzle:
    def __init__(self, size):
        """ 퍼즐 사이즈와 사용할 open, closed 리스트를 초기화합니다. """
        self.n = size
        self.open = []
        self.closed = []
    def accept(self):
        """ 사용자로부터 퍼즐을 입력받습니다. """
        puz = []
        for i in range(0, self.n):
            temp = input().split(" ")
            puz.append(temp)
        return puz

    def showf(self, start, goal):
        """hueristic value f(x)를 출력합니다."""
        print("f(x) = %d + %d " %(self.h(start.data, goal), start.level))

    def f(self, start, goal):
        """ hueristic value f(x) = h(x) + g(x)를 계산합니다.  """
        """계산 과정을 확인하고 싶다면, 주석 해제 """
        """
        f = self.h(start.data, goal) + start.level
        print("%d = %d + %d " %(f, self.h(start.data, goal), start.level ))
        """
        return self.h(start.data, goal) + start.level

    def h(self, start, goal):
        """ 처음 퍼즐과 목표 퍼즐사이의 차이점을 계산합니다. """
        temp = 0
        for i in range(0, self.n):
            for j in range(0, self.n):
                if start[i][j] != goal[i][j] and start[i][j] != '_':
                    temp += 1
        return temp

    def process(self):
        """ 프로그램 메인 프로세스 입니다. """
        print("Enter the start state node")
        start = self.accept()
        print("Enter the goal state node")
        goal = self.accept()

        start = Node(start, 0, 0)
        start.fval = self.f(start, goal)
        """open 리스트에 시작 노드(시작 퍼즐)을 집어넣습니다. """
        self.open.append(start)
        print("\n")
        index = 0
        while True:
            index += 1
            """예외처리입니다. 만약 node의 수가 *30을 넘어가면 메세지를 띄우고 프로그램을 종료합니다."""
            """*30은 과제를 위한 예시입니다. 충분히 수를 늘려줘도 상관없습니다. """
            if(index >= 30) :
                print("Error. This puzzle cannot be solved.")
                print("Exit the program.")
                break
            cur = self.open[0]
            print("")
            print("Node #",index)
            for i in cur.data:
                for j in i:
                    print(j, end=" ")
                print("")
            """과제 조건대로 노드에 해당하는 휴리스틱 측정값을 출력합니다."""
            self.showf(cur, goal)
            """ 현재의 퍼즐 상태와 목표인 퍼즐 상태의 차이가 없을 경우 성공입니다."""
            if (self.h(cur.data, goal) == 0):
                break
            """아니라면 자식노드들을 보면서 최단 경로를 찾습니다."""
            for i in cur.generate_child():
                i.fval = self.f(i, goal)
                self.open.append(i)
            self.closed.append(cur)
            del self.open[0]

            """ lambda를 사용해 가장 비용이 적은 이상적인 솔루션으로 정렬시킵니다."""
            self.open.sort(key=lambda x: x.fval, reverse=False)

"""메인 프로그램 동작"""
puz = Puzzle(3)
puz.process()
