import cv2
from matplotlib import pyplot as plt
from skimage.metrics import structural_similarity as compare_ssim

# path_a = "static/image/test.jpg"
# path_b = "static/image/test2.jpeg"


def check_canny(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (500, 500))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    blurred_A = cv2.GaussianBlur(gray, (3, 3), 0)
    # cv2.imshow("g", blurred_A)
    canny = cv2.Canny(blurred_A, 0, 150)
    return canny


def check_gray(path):
    src = cv2.imread(path)
    src = cv2.resize(src, (500, 500))
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
    # gray = cv2.GaussianBlur(gray, (3,3), 0)

    return gray


def compare(a, b):
    (score, diff) = compare_ssim(a, b, full=True)
    diff = (diff * 255).astype("uint8")
    thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
    plt.imshow(thresh)
    plt.show()
    print(f"Simlarity:{score:.5f}")
    assert score, "못찾음"
    return score

def rating(path_a,path_b):
    gray_a = check_gray(path_a)
    gray_b = check_gray(path_b)
    gray_evl = compare(gray_a, gray_b)
    if gray_evl <= 0.4:
        return '하급'
    canny_a = check_canny(path_a)
    canny_b = check_canny(path_b)
    canny_evl = compare(canny_a, canny_b)
    evl = canny_evl - gray_evl
    ment = ''
    if canny_evl>=0.7:

        if (evl >= 0.3):
            ment='상급'
        elif (0.1 <= evl < 0.29):
            ment='중급'
        else:
            ment='하급'
    else:
        if (evl >= 0.1):
            ment='상급'
        elif (0.05 <= evl < 0.1):
            ment='중급'
        else:
            ment='하급'
    return ment
