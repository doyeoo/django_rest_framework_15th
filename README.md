CEOS 14기 백엔드 스터디 모델링 및 drf 연습을 위한 레포

### 2주차 <hr>

### 도커

#### 컨테이너
소프트웨어 실행 환경 독립적으로 제공하는 가상화 기술<br>
운영체제 전체를 새로 설치하는 것이 아니므로 가볍고 빠르다!
* 컨테이너 삭제 == 컨테이너에서 생성한 파일이 모두 삭제되는 것
* 한 서버에 여러 개의 컨테이너가 존재 가능 각각의 컨테이너는 독립적으로 실행

#### 도커
컨테이너 단위로 서버 구동, 컨테이너를 실행하기 위한 별도 환경 제공<br>
* Dockerfile 서버 운영 기록 코드화 한 것
* 도커 이미지는 Dockerfile로부터 만들어짐

#### 도커 이미지
운영에 필요한 프로그램, 코드, 라이브러리, 실행 파일 등을 모두 묶은 것<br>
이미지 실행하여 컨테이너 생성, 이미지 정보 이용해 항상 동일한 환경 제공 가능
* 용량 크지만 가상머신에 비해서는 매우 작은 편
* 하나의 이미지로부터 여러개의 컨테이너 생성 가능 
* 컨테이너가 삭제되어도 이미지는 보존

> 도커가 도커 파일 실행시키면 도커 이미지가 만들어지고 도커 이미지로부터 컨테이너가 생성된다

#### Docker Compose
여러 컨테이너로 구성된 서비스 관리 도와주는 기능<br>
1. 컨테이너의 Dockerfile 생성
2. docker-compose.yml 작성하여 컨테이너 실행 정의
3. ```docker-compose up``` docker-compose.yml에 정의한 컨테이너 시작

#### docker-compose.yml
도커 컨테이너 실행 옵션 작성한 파일
* docker-compose.yml 컨테이너 정의된 파일 (db, web)
* docker-compose.prod.yml github actions가 서버에서 실행할 파일
* 서버에 DB를 바로 띄우면 위험하고 비효율적이므로 docker-compose.prod.yml 파일에는 db 대신 nginx 컨테이너가 있음
* ```docker-compose -f docker-compose.yml up --build``` docker-compose.yml 대신 다른 파일 실행할 때에는 옵션 ```-f``` 사용해야 함

#### nginx
웹 서버 소프트웨어, 가볍고 동시 접속에 특화되어 있음
정적 데이터 처리 많은 서비스에 적합
* 리버스 프록시 : 서버와 클라이언트 중계, 보안 강화
* 로드밸런싱 : 부하 분산, 무중단 배포 가능

#### .env
환경에 대한 env 파일 별도 작성<br>
RDS, EC2, 장고 관련 정보 

### Github Action

#### Github Action
Github 저장소를 바탕으로 개발 workflow를 자동화하는 도구   
Github에서 바로 등록하거나 .github/workflows 폴더 내에 .yml 파일 추가하여 등록

#### Workflow
자동화 된 전체 프로세스   
하나 이상의 job으로 구성, 이벤트에 의해 실행

#### Event
워크플로우를 실행하는 활동이나 규칙   
push, pull request 등

#### Job
워크플로우의 기본 단위

#### deploy.yml
1. github actions는 deploy.yml 파일로부터 deploy.sh 파일을 만들어 실행
2. 만들어진 deploy.sh가 docker-compose 실행
3. docker-compose가 컨테이너 빌드하여 실행
