def worstFit(blockSize, m, processSize, n):   
    # Lưu trữ id của khối được cấp cho một tiến trình
    #Ban dầu không có khôi nào được chỉ định cho bất kì tiến trình nào
    allocation = [-1] * n  
    # pick each process and find suitable blocks
    # according to its size ad assign to it
    for i in range(n):
   #chọn tiến trình và tìm các khối phù hợp theo kích thước
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1:
                    wstIdx = j
                elif blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
        if wstIdx != -1:
            allocation[i] = wstIdx
            blockSize[wstIdx] -= processSize[i]
 
    print("Process No. Process Size Block no.")
    for i in range(n):
        print(i + 1, "         ",
              processSize[i], end = "     ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")
if __name__ == '__main__':
    blockSize = [100, 500, 200, 300, 600]
    processSize = [212, 417, 112, 426]
    m = len(blockSize)
    n = len(processSize)
 
    worstFit(blockSize, m, processSize, n)