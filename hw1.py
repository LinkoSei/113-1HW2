def getResult():
    # 定義字符
    alphabet1 = [
        ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],  
        ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],  
        ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L', ';'],  
        ['Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '/']   
    ]
    
    # 要求輸入測試次數 N
    N = int(input("輸入測試次數 N (1 < N < 2147483647): "))
    
    # 進行 N 次測試
    for _ in range(N):
        s, K = input("輸入字符 S 和方向 K (1 <= K <= 4): ").split()
        K = int(K) 
        
        # 找出字符 S 在網格中的位置
        row, col = None, None  # 初始化行和列
        for i, row_list in enumerate(alphabet1):  # 逐行搜索
            if s in row_list:  # 如果字符 S 在當前行中
                row = i  # 紀錄該字符的行索引
                col = row_list.index(s)  # 紀錄該字符的列索引
                break

        # 如果找不到字符 S，則跳過該次測試
        if row is None or col is None:
            print(f"字符 {s} 未找到。")
            continue
        
        # 根據方向 K 計算相鄰字符的位置
        if K == 1:  # K=1，向上移動
            new_row = (row - 1) % 4  # 行索引減一，超過範圍則回繞到最後一行
            new_char = alphabet1[new_row][col]  # 保持列不變，取得新位置的字符
        elif K == 2:  # K=2，向下移動
            new_row = (row + 1) % 4  # 行索引加一，超過範圍則回到第一行
            new_char = alphabet1[new_row][col]  
        elif K == 3:  # K=3，向左移動
            new_col = (col - 1) % 10  
            new_char = alphabet1[row][new_col]  # 保持行不變，取得新位置的字符
        elif K == 4:  # K=4，向右移動
            new_col = (col + 1) % 10  
            new_char = alphabet1[row][new_col]  
        else:
            print(f"無效的方向 K={K}.")  # 如果 K 的值不在 1 到 4 範圍內，則提示無效
            continue
        
        # 輸出找到的字符
        print(new_char)
getResult()