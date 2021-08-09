## 책Check
### 2021 인천대학교 캡스톤디자인 졸업작품 경진대회 - 장려상

### 팀명 : 5인가족
- 김대현
- 김윤성
- 박창헌
- 조주영
- 홍성진

### 작품 개요
중고서적 촬영 후, 책 상태에 따른 등급을 측정하여 책의 등급을 사용자에게 제공하는 시스템

### 아이디어 선정 이유
- 일반적인 중고 서적 구매 과정
	1. 중고 서적 검색
	2. 가격 및 상세 정보 파악
	3. 판매자가 지정한 책의 등급을 신회
	4. 구매 후 **분쟁** 발생 가능

구매 후 분쟁 발생이 가능하다는 점에 Focus!
-> 책의 등급을 객관적으로 판별 해줄 수 있는 Application!

### 사용 기술
- Python
- OpenCV
	- 등급 판정
	- 이미지 처리
- Flask
	- Mobile Application과의 통신을 위한 Web Server
- App Inventor
	- 책의 바코드 인식 기능 및 촬영기능
	- UI
- File zilla
	- FTP Server

### 핵심 기능
<img width="80%" alt="스크린샷_2021-08-09_오후_7 39 28-removebg-preview" src="https://user-images.githubusercontent.com/56334761/128695330-54f86fb8-c219-4266-84a5-63add0d51a94.png">

1. Kakao API를 통해 불러온 원본 이미지와, 촬영된 이미지의 크기를 맞추어 두 개의 이미지를 전처리
2. 전처리 된 두 이미지를 비교하여 픽셀 단위로 노이즈 산출
3. 기존 이미지의 비율과 산출된 노이즈를 근거로 등급 판정

### 작품 시연
	초기화면		책 ISBN 스캔
![12-removebg-preview (3)](https://user-images.githubusercontent.com/56334761/128698711-224df5ce-a3bb-4eab-8ac4-c756be3c0f11.png)


![34-removebg-preview](https://user-images.githubusercontent.com/56334761/128698566-76565dcc-6277-45c6-bc4e-bf38cc4f6029.png)

