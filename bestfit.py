def bestFit(blockSize, m, processSize, n):   
    # Lưu trữ id của khối được phân bổ cho 1 tiến trình
    allocation = [-1] * n      
    # Chọn từng quy trình va tìm các khối phù hợp theo kích thước của nó mà đã chỉ định
    for i in range(n):     
        # Tìm khối phù hợp nhất cho tiến trình thực hiện 
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1: 
                    bestIdx = j 
                elif blockSize[bestIdx] > blockSize[j]: 
                    bestIdx = j  
        # Nếu không thể tìm thấy khối cho quy trình hiện tại  
        if bestIdx != -1:    
            # Thì ta cấp pháp khối j cho quá trình p[i]
            allocation[i] = bestIdx 
            # Giảm bộ nhớ khả dụng trong khối bloock
            blockSize[bestIdx] -= processSize[i] 
    print("Process No. Process Size     Block no.")
    for i in range(n):
        print(i + 1, "         ", processSize[i], 
                                end = "         ") 
        if allocation[i] != -1: 
            print(allocation[i] + 1) 
        else:
            print("Not Allocated")    
if __name__ == '__main__': 
    blockSize = [100, 500, 200, 300, 600] 
    processSize = [212, 417, 112, 426] 
    m = len(blockSize) 
    n = len(processSize) 
  
    bestFit(blockSize, m, processSize, n)
      