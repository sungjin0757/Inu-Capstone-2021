# 책Check
## 2021 인천대학교 캡스톤디자인 졸업작품 경진대회 - 장려상 🎖

**<a href="https://github.com/sungjin0757/Inu-Capstone-2021/raw/master/presentation.pptx">DOWNLOAD : 발표 자료 </a>**
**<a href="https://github.com/sungjin0757/Inu-Capstone-2021/raw/master/%EB%B0%9C%ED%91%9C%EC%98%81%EC%83%81.mp4">DOWNLOAD : 발표 영상 </a>**

### [ 팀명 : 5인가족 ]
- **김대현 : <a href="https://github.com/kimdh-hi">github</a>**
- **김윤성 : <a href="https://github.com/f-dev-kys">github</a>**
- **박창헌 : <a href="https://github.com/parkchangheon">github</a>**
- **조주영 : <a href="https://github.com/chojooyoung">github</a>**
- **홍성진 : <a href="https://github.com/sungjin0757">github</a>**

### [ 개발 기간 ]
**2020/08 ~ 2021/05**

### [ 작품 개요 ]
중고서적 촬영 후, 책 상태에 따른 등급을 측정하여 책의 등급을 사용자에게 제공하는 시스템

### [ 아이디어 선정 이유 ]
최근 중고제품 플랫폼이 성장함에 따라 중고 거래 이용자가 늘어나는 추세.
- 일반적인 중고 서적 구매 과정
	1. 중고 서적 검색
	2. 가격 및 상세 정보 파악
	3. 판매자가 지정한 책의 등급을 신회
	4. 구매 후 **분쟁** 발생 가능
책을 중고로 판매할 시 중고 플랫폼 이용자가 가격을 측정함에 있어 별다른 기준이 없다는 점에서 IDEA 착안.</br>
구매 후 분쟁 발생이 가능하다는 점에 Focus!</br>
-> 책의 등급을 객관적으로 판별 해줄 수 있는 Application!

### [ 사용 기술 ]
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
	- FTP Server : Client와 Server간의 추가 통신을 위해

### [ 핵심 기능 ]
<img width="90%" alt="스크린샷_2021-08-09_오후_7 39 28-removebg-preview" src="https://user-images.githubusercontent.com/56334761/128695330-54f86fb8-c219-4266-84a5-63add0d51a94.png">

1. Kakao API를 통해 불러온 원본 이미지와, 촬영된 이미지의 크기를 맞추어 두 개의 이미지를 전처리
2. 전처리 된 두 이미지를 비교하여 픽셀 단위로 노이즈 산출
3. 기존 이미지의 비율과 산출된 노이즈를 근거로 등급 판정

>
- **Detail**
책을 Blur처리 후 이미지를 흑백으로 이진화한 후 두 이미지의 외곽선을 도출. </br>
이 과정을 통해 광원(빛)으로 인한 간섭을 기존보다 최소화 시키며 책의 상태를 보다 명확하게 비교 가능.</br>
책의 원본 이미지와 촬영된 이미지는 Blur를 이용하여 명도를 낮추고, OpenCV 라이브러리 함수로 흑백전환을 통해 명암 비율 조정.</br>
명암비를 확실하게 0과 1로 이진화 한 후 Byte 배열로 나타내어 빛의 영향을 없애고, 외곽선을 도출하여 책의 구겨짐과 흠집을 나타내 줌. </br>
도출된 외곽선으로 책의 등급을 판정하기 위해 원본 이미지와 촬영된 이미지의 Byte배열을 Pixel단위로 비교. 


### 📱 작품 시연

<img width="200px" height="250px" src="https://user-images.githubusercontent.com/56334761/128700006-34115c9f-01d6-4ba0-9a2d-c589c589f899.PNG">     <img width="200px" height="250px" src="https://user-images.githubusercontent.com/56334761/128700015-c2c53e14-a998-4773-81e6-5d8484d20899.PNG"> 
<img width="200px" height="250px" src="https://user-images.githubusercontent.com/56334761/128700033-1b87918d-3693-4a55-a04d-e947561c33b9.PNG">
<img width="200px" height="250px" src="https://user-images.githubusercontent.com/56334761/128700040-59278694-fd6f-4f6f-9a07-0e18b1f73d97.PNG">

>
1. 사용자로 부터 책 고유 번호인 ISBN을 입력 받음. (스마트폰의 바코드 스캐너 이용)
2. 판정하고자 하는 책을 입력 받음.
3. 사진 업로드가 완료되면 '감정하기' 버튼 활성화.
4. 등급 판정 실행.

</br>
---
**<a href="https://www.inu.ac.kr/user/indexSub.do?codyMenuSeq=2452975&siteId=isis&dum=dum&boardId=630255&page=3&command=view&boardSeq=630325">인천대학교 졸업작품 갤러리 - 책Check</a>**