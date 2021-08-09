# 책Check
## 2021 인천대학교 캡스톤디자인 졸업작품 경진대회 - 장려상

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
1. 시작 화면

<img width="150px" height="200px" src="https://user-images.githubusercontent.com/56334761/128700006-34115c9f-01d6-4ba0-9a2d-c589c589f899.PNG">  <img width="100px" height="150px" src="https://user-images.githubusercontent.com/56334761/128700015-c2c53e14-a998-4773-81e6-5d8484d20899.PNG">

3. ISBN 스캔 화면

![isbn](https://user-images.githubusercontent.com/56334761/128700026-abeb65cb-da9e-41d4-94e3-dfbe0f873d58.PNG)

4. 스캔 완료 후 화면

![스캔후](https://user-images.githubusercontent.com/56334761/128700033-1b87918d-3693-4a55-a04d-e947561c33b9.PNG)

5. 등급 판정 화면

![왼료](https://user-images.githubusercontent.com/56334761/128700040-59278694-fd6f-4f6f-9a07-0e18b1f73d97.PNG)


