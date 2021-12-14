from collections import defaultdict
 
# ho một đồ thị có hướng
# Sử dụng list gần kề để biểu diễn
class Graph:
    # Xây dựng thuật toán
    def __init__(self):
 
        #Lưu trữ đồ thi vào thư viện
        self.graph = defaultdict(list)
 
    # Hàm thêm cạnh vào đồ thị
    def addEdge(self,u,v):
        self.graph[u].append(v)
 
    # Set hàm BFS
    # Cho hàm bắt đầu từ đỉnh 
    def BFS(self, s):
 
        # Đánh dấu các điểm chưa xét
        visited = [False] * (max(self.graph) + 1)
 
        # Tạo hàng chờ cho hàm BFS
        queue = []
 
        # Đánh dấu nút chính
        # Biểu đồ cho đồ thị trên
        queue.append(s)
        visited[s] = True
 
        while queue:
 
            # Sắp xếp và in
            s = queue.pop(0)
            print (s, end = " ")
 
            # Nhận các đỉnh liền kề
            # Xóa đỉnh khỏi hàng chờ nếu liền kề
            # Đánh dấu các điểm chưa được xét
            # Xét và sắp xếp các điểm đó
            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True
 
# Driver code
 
# Tạo biểu đồ cho sơ đồ trên

g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Phương pháp Breadth First Traversal (BFS)"
                  " (Bắt đầu từ đỉnh 2)")
g.BFS(2)