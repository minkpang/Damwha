# 🌸 담화 Frontend 

> 향기롭게 마음을 전하는 방법, 담화 입니다.

프론트엔드 개발은 Android와 iOS 두 플랫폼을 통해 개발했으며, 내부에 Webview를 사용하여 하이브리트 형식으로 만들었습니다. 아래 정확한 테크스택을 적어두겠습니다.



## Android

### ✔️Android Studio IDE Setup

For development, the latest version of Android Studio is required. 



### 🛠 Teck Stack

- Foundation 
  - AppCompat
  - Android KTX
  - Jetpack Navigation
  - Fragment
  - ViewPager2
- Architecture
  - Data Binding
  - Lifecycles
  - ViewModel
- Third party and miscellaneous libraries
  - Glide
  - Retrofit
  - OkHttp
  - Firebase
  - RxJava, RxAndroid, RxKotlin
  - CarouselRecyclerView
  - Kakao SDK
  - Lottie

### MAD Scorecard

Modern Android Development(MAD)는 더 나은 애플리케이션을 구축하는데 도움을 주는 Blueprint입니다. 현재 저희 팀의 Android 프로젝트가 얼마나 최신 Android 플랫폼, 라이브러리, 기술을 사용하는지 확인합니다.

![jetpack](README.assets/summary.png)

![jetpack](README.assets/jetpack-3600462.png)



### 🪜 Architecture

아키텍처의 경우 MVVM 및 Repository 패턴을 사용하였습니다.

또한, DI 라이브러리를 사용하지 않았기 때문에 의존성의 경우 따로 DamhwaInjection 오브젝트를 만들어 주입해주는 형식으로 사용했습니다.

![image](https://user-images.githubusercontent.com/22849063/132246469-3bcc36b3-70f3-4ee2-b32d-851bd77dcadd.png)

### 📷 ScreenShots

#### 1. 서신쓰기 > 추천

<img src="README.assets/image-20211007183807733.png" alt="image-20211007183807733" style="zoom:50%;" /><img src="README.assets/image-20211007183816052.png" alt="image-20211007183816052" style="zoom:50%;" /><img src="README.assets/image-20211007183826115.png" alt="image-20211007183826115" style="zoom:50%;" />



#### 2. 기분쓰기 > 추천

<img src="README.assets/image-20211007183947746.png" alt="image-20211007183947746" style="zoom:50%;" /><img src="README.assets/image-20211007183921086.png" alt="image-20211007183921086" style="zoom:50%;" />



#### 3. 꽃 달력 -> 상세보기 (Vue.js)

<img src="README.assets/image-20211007184004338.png" alt="image-20211007184004338" style="zoom:50%;" />

## iOS

### ✔Swift5 with Xcode12


### 🛠 Teck Stack

- Swift Packeges
  - ACarousel
  - Lottie
- Firebase 
- KakaoSDK
- Alamofire

### 구현 내용

- SwiftUI를 통한 UI 구현을 진행하였습니다.
- 소셜 로그인 기능구현 (Kakao, Apple), 로그인없이 사용가능 (배포 심사) 
- WebView 연동 및 네이티브에서 JS 함수 호출
- API 통신을 위하여 Alamofire 사용
- KakaoSDK 사용하여 메세지 공유기능 구현



## Web

웹의 경우 웹뷰를 구현하기 위해 사용하였습니다.

Calendar와, 서신보는 페이지 및 감정기록 보는 페이지 총 3개의 페이지로 구성되어있습니다.

### ✔️Visual Studio Code IDE Setup

For development, the latest version of Visual Studio Code is required. 



### 🛠 Teck Stack

- Vue.js 
- Vue-router 
- Boostrap5 



### 📷 ScreenShots



