#if __name__ == '__main__':
#    n = int(input())
 #   arr = map(int, input().split())
 #   maximum_score = max(arr)
 #   
 #   runner_up = maximum_score - 1
 #   print(runner_up)


n = int(input())
arr =list(map(int, input().split()))
arr.sort()
print(arr[(arr.index(max(arr)))-1])

#l = [-1,-1,-1,1,1,1]
#s = sorted(l)
#print(s)
 
