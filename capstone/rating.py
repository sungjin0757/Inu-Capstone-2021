import cv2

def check(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (300, 300))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (3, 3), 0)
    canny = cv2.Canny(blurred_A, 0, 150)
    return canny

def ori_check(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (300, 300))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    canny = cv2.Canny(gray, 0, 150)
    return canny

def check_gray(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (300, 300))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

    return gray

def final_compare(path_ftp, path_isbn):
    ca = check(path_ftp)  # 카메라 jpg 파일
    cb = ori_check(path_isbn)  # isbn 코드 jpg
    # plt.imshow(ca)
    # plt.show()
    # plt.imshow(cb)
    # plt.show()

    percent_a = 0
    percent_b = 0

    for i in range(300):
        for j in range(300):
            if ca[i][j] == 255:
                percent_a += 1

    for i in range(300):
        for j in range(300):
            if cb[i][j] == 255:
                percent_b += 1
    sub = abs(percent_a - percent_b)

    print('percent_a(촬열 흰선):', percent_a)
    print('percent_b(원본 흰선):', percent_b)
    print('sub : ', sub)

    if percent_b == 0:
        print('하급')
    va = (sub / percent_b) * 100

    print('+:', va, '%')
    if percent_b >= 0 and percent_b <= 5000:  # 원본 무늬(흰색선)가 적은 책
        if va <= 40:  # 촬영 이미지가 +40% 이하면 상급
            return '상급'
        elif va > 40 and va < 85:  # 촬열 이미지가 +40~85면 중급
            return '중급'
        else:
            return '하급'
    elif percent_b > 5000 and percent_b <= 8000:
        if va < 30:
            return '상급'
        elif va > 30 and va < 80:
            return '중급'
        else:
            return '하급'
    elif percent_b > 8000 and percent_b <= 10000:
        if va <= 9:
            return '상급'
        elif va > 9 and va < 35:
            return '중급'
        else:
            return '하급'
    elif percent_b > 10000 and percent_b <= 15000:
        if va < 3:
            return '상급'
        elif va > 3 and va < 5:
            return '중급'
        else:
            return '하급'
    elif percent_b > 15000:
        if va <= 2:
            return '상급'
        elif va > 2 and va < 3.0:
            return '중급'
        else:
            return '하급'