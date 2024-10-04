def calculate_iou(rect1, rect2): 
    # rect1, rect2는 각각 (x, y, w, h) 형태 
    x1, y1, w1, h1 = rect1 
    x2, y2, w2, h2 = rect2 
     
    # 교집합의 넓이 계산 
    x_overlap = max(0, min(x1 + w1, x2 + w2) - max(x1, x2)) 
    y_overlap = max(0, min(y1 + h1, y2 + h2) - max(y1, y2)) 
    intersection_area = x_overlap * y_overlap 
 
    # 합집합의 넓이 계산 
    area1 = w1 * h1 
    area2 = w2 * h2 
    union_area = area1 + area2 - intersection_area 
 
    # IoU 계산 
    if union_area == 0: 
        return 0 
    return intersection_area / union_area 
 
def find_max_iou_pair(rectangles): 
    max_iou = -1 
    max_pair = (0, 0) 
    n = len(rectangles) 
 
    # 모든 직사각형 쌍에 대해 IoU 계산 
    for i in range(n): 
        for j in range(i + 1, n): 
            iou = calculate_iou(rectangles[i], rectangles[j]) 
            if iou > max_iou: 
                max_iou = iou 
                max_pair = (i + 1, j + 1)  # 1-based index 
            elif iou == max_iou: 
                # 사전순으로 가장 앞서는 순서쌍 선택 
                if (i + 1, j + 1) < max_pair: 
                    max_pair = (i + 1, j + 1) 
 
    return max_pair 
 
# 입력 받기 
n = int(input().strip()) 
rectangles = [] 
 
for _ in range(n): 
    x, y, w, h = map(int, input().strip().split()) 
    rectangles.append((x, y, w, h)) 
 
# 결과 계산 및 출력 
result = find_max_iou_pair(rectangles) 
print(result[0], result[1]) 
