import cv2

def calculate_histogram_similarity(image1, image2):
    # 이미지를 그레이스케일로 변환
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 히스토그램 계산
    hist1 = cv2.calcHist([gray1], [0], None, [256], [0, 256])
    hist2 = cv2.calcHist([gray2], [0], None, [256], [0, 256])

    # 히스토그램 비교
    similarity_score = cv2.compareHist(hist1, hist2, cv2.HISTCMP_CORREL)
    return similarity_score

def judge_similarity(image1_path, image2_path):
    threshold = 0.5


# 이미지 파일 읽기
    image1 = cv2.imread(image1_path)
    image2 = cv2.imread(image2_path)

    if image1.shape[0] > image2.shape[0]:
        image1 = cv2.resize(image1, (image2.shape[1], image2.shape[0]), interpolation=cv2.INTER_AREA)

# 이미지 유사도 계산
    similarity_score = calculate_histogram_similarity(image1, image2)
    if similarity_score > threshold:
        return True
    else:
        return False
    