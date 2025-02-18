CEOS 14기 백엔드 스터디 모델링 및 drf 연습을 위한 레포

## 2주차 <hr>

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

<br>

## 3주차 <hr>

#### MySQL 설치
환경 변수 설정 안하면 mysql 명령어 에러남   
시스템 속성 > 환경 변수 > 시스템 변수 > Path  
```C:\Program Files\MySQL\MySQL Server 8.0\bin``` 추가

<br>

### 인스타그램 데이터 모델링

![다운로드](https://user-images.githubusercontent.com/81256252/161230387-f2a8c3bd-4715-4dea-85ca-4b5034a5fe9b.png)

#### User
장고에서 기본으로 제공하는 유저 모델
* 사용자 이름, 비밀번호, 이름, 성, 이메일 주소 필드


#### Profile
장고 기본 User Model OneToOne 확장   
* 전화번호 _중복 방지하기 위해 `unique=True` 추가_
* 프로필 사진 _ImageField 대신 url 링크 넣을 수 있는 CharField로 변경_
* 웹사이트
* 소개
* 팔로워, 팔로잉
  * Profile 모델(self)과 N:M 관계
  * 팔로워, 팔로잉 0인 경우 존재하기 때문에 blank=True   
  ```    follower=models.ManyToManyField('self', blank=True)```   
    ```following=models.ManyToManyField('self', blank=True)```

#### Post
게시글 모델   
사진이나 영상 파일은 1:N으로 연결하기 위해 별도 모델로 관리
* 유저 아이디 Foreign Key로 사용 1(유저):N(게시글) 
* 내용
* ~~업로드 시간~~
* 댓글
  * 댓글 수만 카운트, 댓글 상세 내용은 Comment 모델에서 관리
* 좋아요
  * 좋아요 수만 카운트, 좋아요 상세 내용은 Like 모델에서 관리

#### File
글과 함께 올라가는 사진 및 영상 파일 모델    
게시글과 1(글):N(파일)
* 포스트 아이디 Foreign Key로 사용 1(글):N(파일)
* 해당 글에 업로드할 파일 _FileField 대신 url 링크 넣을 수 있는 CharField로 변경_

#### Comment
글에 달린 댓글 관련 상세 내용 관리   
게시글과 1:N 관계
* 포스트 아이디 Foreign Key로 사용 1(글):N(댓글)
* 유저 아이디 Foreign Key로 사용 1(댓글 작성한 유저):N(댓글)
* ~~업로드 시간~~
* 댓글 내용

#### Like
글에 달린 좋아요 관련 상세 내용 관리   
게시글과 1:N 관계
* 포스트 아이디 Foreign Key로 사용 1(글):N(댓글)
* 유저 아이디 Foreign Key로 사용 1(좋아요 한 유저):N(댓글)
* ~~업로드 시간~~


#### + Base Model
다른 모델이 상속받아 사용할 수 있도록 created_at, updated_at 필드 따로 작성한 모델   
`class Meta: abstract = True`
* 최초 업로드 시간 `auto_now_add=True`
* 수정 시간 `auto_now=True`

<br>

#### ORM 적용해보기
1. 데이터베이스에 객체 넣기      
![post create+all](https://user-images.githubusercontent.com/81256252/161230476-c8351705-7f1d-4902-b842-f051b9955735.PNG)

2. 삽입한 객체 조회하기    
![post get](https://user-images.githubusercontent.com/81256252/161230495-a151b3a8-b51c-432f-9f26-4d6840dfc615.PNG)

3. filter 함수 사용해보기     
![post filter](https://user-images.githubusercontent.com/81256252/161230522-8e201d53-ef61-4dcc-920b-d14504a88a67.PNG)

<br>

#### 회고
기존에 설치되어있던 MariaDB와 충돌하여서인지 MySQL 초기 세팅을 하는데 시간이 걸렸다.      
MariaDB를 삭제하고 MySQL을 새로 설치하였고 MySQL 파일 위치를 환경 변수에 추가하여 mysql 관련 명령어가 실행되지 않던 오류를 해결하였다.    

ERD 모델링을 먼저 하고 models.py 코드를 작성하였는데 그 과정에서 초기에 생각했던 모델에 문제가 있다는 것을 발견하였다.   
덕분에 모델 Relation 관련 개념을 다시 한 번 정리하고 공부할 수 있었다.

팔로우 관련 기능을 구현할 때 N:M 관계를 이용하였는데 해당 기능을 Profile 모델에 넣었더니 Profile 모델에 너무 많은 필드가 들어가게 되었다.
팔로우 관련 기능은 별도로 관리할 수 있게 following과 follower 필드는 따로 빼 모델을 수정할 예정이다.

<br>

## 4주차 <hr/>
#### 데이터 삽입
Post 모델  
```
class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    like_count = models.PositiveIntegerField(default=0)
    comment_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.content[:50]

class Like(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='like', on_delete=models.CASCADE)

    def __str__(self):
        return self.post.content[:50]+" / "+self.user.username

class Comment(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='comment', on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.post.content[:50]+" / "+self.user.username
```
데이터 삽입 결과    
![image](https://user-images.githubusercontent.com/81256252/162493664-ff7b9505-a489-4eb7-b638-edf7d8541e02.png)

<br>
        
#### 모든 데이터 가져오는 API
* URL : api/post/
* Method : GET
```
[
    {
        "id": 1,
        "comment": [
            {
                "id": 1,
                "created_at": "2022-04-04T00:37:19.719049+09:00",
                "updated_at": "2022-04-04T00:52:54.935482+09:00",
                "content": "hihi",
                "user": 3,
                "post": 1
            }
        ],
        "like": [
            {
                "id": 1,
                "created_at": "2022-04-04T00:37:07.577675+09:00",
                "updated_at": "2022-04-04T00:37:07.577675+09:00",
                "user": 1,
                "post": 1
            }
        ],
        "file": [
            {
                "id": 1,
                "url": "asdasd",
                "post": 1
            }
        ],
        "created_at": "2022-04-04T00:35:09.855194+09:00",
        "updated_at": "2022-04-09T02:37:37.044732+09:00",
        "content": "Ut hendrerit arcu facilisis erat molestie, et egestas sem blandit. Ut mattis ligula sed nulla efficitur ullamcorper. Sed tellus sem, consectetur ac laoreet vitae, aliquet vel metus. Quisque sed turpis malesuada, sodales ex ut, semper tellus. Aenean dapibus nec neque id dapibus. Aenean hendrerit lorem eu volutpat efficitur. Sed pulvinar finibus lorem, ac pharetra metus finibus vel. Cras sit amet arcu luctus, feugiat nibh a, blandit mi. Pellentesque rutrum mi molestie, pellentesque felis ut, rutrum metus. Phasellus fringilla dignissim nisl, sed molestie orci vehicula vitae. Nulla facilisi. Aenean sed maximus massa. Mauris vel pellentesque nulla. Curabitur ut posuere purus. Maecenas elementum est ex.",
        "like_count": 2,
        "comment_count": 2,
        "user": 1
    },
    {
        "id": 2,
        "comment": [
            {
                "id": 2,
                "created_at": "2022-04-04T00:46:32.936881+09:00",
                "updated_at": "2022-04-04T00:46:32.936881+09:00",
                "content": "asd",
                "user": 1,
                "post": 2
            },
            {
                "id": 3,
                "created_at": "2022-04-04T00:52:43.022380+09:00",
                "updated_at": "2022-04-04T00:52:43.022380+09:00",
                "content": "abc",
                "user": 2,
                "post": 2
            }
        ],
        "like": [
            {
                "id": 2,
                "created_at": "2022-04-04T00:52:26.776129+09:00",
                "updated_at": "2022-04-04T00:52:26.776129+09:00",
                "user": 2,
                "post": 2
            }
        ],
        "file": [],
        "created_at": "2022-04-04T00:46:20.295188+09:00",
        "updated_at": "2022-04-04T00:51:05.388888+09:00",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pellentesque lorem sed lorem posuere tincidunt. Sed finibus metus sed ante eleifend consectetur. Curabitur interdum nisl eu urna semper ornare. Curabitur varius sodales aliquet. Aliquam a elementum magna. Nam commodo auctor fermentum. In semper gravida est, ut condimentum risus consequat nec. Proin dapibus pellentesque rutrum. Morbi tincidunt nulla in porta convallis.",
        "like_count": 0,
        "comment_count": 0,
        "user": 2
    },
    {
        "id": 3,
        "comment": [],
        "like": [],
        "file": [],
        "created_at": "2022-04-04T00:48:42.437394+09:00",
        "updated_at": "2022-04-09T02:38:15.035626+09:00",
        "content": "Nulla iaculis auctor pretium. Phasellus nec nisl ut diam sodales viverra et sed sem. Pellentesque vestibulum euismod ligula, nec pretium sem ultricies sodales. Nulla id quam interdum, dapibus ex ut, feugiat est. Vestibulum congue condimentum ligula, sed ultricies est rutrum at. Phasellus vulputate magna a dolor tincidunt, vel tempus quam accumsan. Etiam dignissim ut purus scelerisque ultrices. Nullam viverra vulputate dui, a commodo nisi tempor condimentum. Nulla facilisi. Vivamus consectetur magna egestas mauris volutpat, vitae vestibulum tellus accumsan. Morbi eu purus tempor, vehicula mi tempor, feugiat mauris.",
        "like_count": 1,
        "comment_count": 1,
        "user": 3
    }
]
```

<br>

#### 새로운 데이터 생성하는 API
* URL : api/post/
* Method : POST   
* Body : ```{ "id":6, "content":"post", "user":3 }```  

![image](https://user-images.githubusercontent.com/81256252/162494842-e6b14197-79b2-4660-bdd5-bd8b482545e0.png)   

![image](https://user-images.githubusercontent.com/81256252/162494896-1103aaea-6451-4fdb-b8d7-b4a95c23e980.png)


#### 회고
3주차 과제 피드백을 반영하여 의미가 불분명한 모델의 필드명을 수정하였고 사진이나 영상 파일을 받을 때 사용한 ImageField, FileField를 CharField로 수정하였다. 
모델마다 중복 사용된 업로드 시간, 수정 시간 필드는 추상 모델인 BaseModel 안에 시간 관련 필드를 작성해 다른 모델들이 이를 상속받을 수 있게 히였다.

4주차 과제 중 모든 데이터를 가져오는 API가 외래키로 연결된 모델의 내용을 제대로 가지고 오지 못하는 문제가 발생하였다. 모델에 ```'related_name'```을 추가하지 않아 발생한 문제임을 알게되었고 가져와야 하는 내용을 담고있는 모델 필드에 ```related_name```을 설정해 해결할 수 있었다. 

view의 경우 이전에 ViewSet을 사용하였을 때 코드를 간결하게 작성했던 기억이 있어 viewset을 가져와 사용하였고 url은 라우터를 이용하여 연결해주었다.

<br>

## 5주차 <hr>

### 모든 list를 가져오는 API
* URL : api/posts/
* Method : GET
```
[
    {
        "id": 1,
        "comment": [
            {
                "id": 1,
                "created_at": "2022-04-04T00:37:19.719049+09:00",
                "updated_at": "2022-04-04T00:52:54.935482+09:00",
                "content": "hihi",
                "user": 3,
                "post": 1
            }
        ],
        "like": [
            {
                "id": 1,
                "created_at": "2022-04-04T00:37:07.577675+09:00",
                "updated_at": "2022-04-04T00:37:07.577675+09:00",
                "user": 1,
                "post": 1
            }
        ],
        "file": [
            {
                "id": 1,
                "url": "asdasd",
                "post": 1
            }
        ],
        "created_at": "2022-04-04T00:35:09.855194+09:00",
        "updated_at": "2022-04-09T02:37:37.044732+09:00",
        "content": "Ut hendrerit arcu facilisis erat molestie, et egestas sem blandit. Ut mattis ligula sed nulla efficitur ullamcorper. Sed tellus sem, consectetur ac laoreet vitae, aliquet vel metus. Quisque sed turpis malesuada, sodales ex ut, semper tellus. Aenean dapibus nec neque id dapibus. Aenean hendrerit lorem eu volutpat efficitur. Sed pulvinar finibus lorem, ac pharetra metus finibus vel. Cras sit amet arcu luctus, feugiat nibh a, blandit mi. Pellentesque rutrum mi molestie, pellentesque felis ut, rutrum metus. Phasellus fringilla dignissim nisl, sed molestie orci vehicula vitae. Nulla facilisi. Aenean sed maximus massa. Mauris vel pellentesque nulla. Curabitur ut posuere purus. Maecenas elementum est ex.",
        "like_count": 2,
        "comment_count": 2,
        "user": 1
    },
    {
        "id": 2,
        "comment": [
            {
                "id": 2,
                "created_at": "2022-04-04T00:46:32.936881+09:00",
                "updated_at": "2022-04-04T00:46:32.936881+09:00",
                "content": "asd",
                "user": 1,
                "post": 2
            },
            {
                "id": 3,
                "created_at": "2022-04-04T00:52:43.022380+09:00",
                "updated_at": "2022-04-04T00:52:43.022380+09:00",
                "content": "abc",
                "user": 2,
                "post": 2
            }
        ],
        "like": [
            {
                "id": 2,
                "created_at": "2022-04-04T00:52:26.776129+09:00",
                "updated_at": "2022-04-04T00:52:26.776129+09:00",
                "user": 2,
                "post": 2
            }
        ],
        "file": [],
        "created_at": "2022-04-04T00:46:20.295188+09:00",
        "updated_at": "2022-04-04T00:51:05.388888+09:00",
        "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pellentesque lorem sed lorem posuere tincidunt. Sed finibus metus sed ante eleifend consectetur. Curabitur interdum nisl eu urna semper ornare. Curabitur varius sodales aliquet. Aliquam a elementum magna. Nam commodo auctor fermentum. In semper gravida est, ut condimentum risus consequat nec. Proin dapibus pellentesque rutrum. Morbi tincidunt nulla in porta convallis.",
        "like_count": 0,
        "comment_count": 0,
        "user": 2
    },
    {
        "id": 3,
        "comment": [],
        "like": [],
        "file": [],
        "created_at": "2022-04-04T00:48:42.437394+09:00",
        "updated_at": "2022-04-09T02:38:15.035626+09:00",
        "content": "Nulla iaculis auctor pretium. Phasellus nec nisl ut diam sodales viverra et sed sem. Pellentesque vestibulum euismod ligula, nec pretium sem ultricies sodales. Nulla id quam interdum, dapibus ex ut, feugiat est. Vestibulum congue condimentum ligula, sed ultricies est rutrum at. Phasellus vulputate magna a dolor tincidunt, vel tempus quam accumsan. Etiam dignissim ut purus scelerisque ultrices. Nullam viverra vulputate dui, a commodo nisi tempor condimentum. Nulla facilisi. Vivamus consectetur magna egestas mauris volutpat, vitae vestibulum tellus accumsan. Morbi eu purus tempor, vehicula mi tempor, feugiat mauris.",
        "like_count": 1,
        "comment_count": 1,
        "user": 3
    },
    {
        "id": 4,
        "comment": [],
        "like": [],
        "file": [],
        "created_at": "2022-04-08T20:04:52.259136+09:00",
        "updated_at": "2022-04-09T02:37:49.522306+09:00",
        "content": "new post",
        "like_count": 4,
        "comment_count": 2,
        "user": 2
    },
    {
        "id": 5,
        "comment": [],
        "like": [],
        "file": [],
        "created_at": "2022-04-09T02:20:22.027060+09:00",
        "updated_at": "2022-04-09T02:38:04.400624+09:00",
        "content": "새 글",
        "like_count": 0,
        "comment_count": 0,
        "user": 1
    },
    {
        "id": 6,
        "comment": [],
        "like": [],
        "file": [],
        "created_at": "2022-04-09T02:48:47.092571+09:00",
        "updated_at": "2022-04-09T02:48:47.092571+09:00",
        "content": "post",
        "like_count": 0,
        "comment_count": 0,
        "user": 3
    }
]
```

### 특정 데이터를 가져오는 API
* URL : api/posts/2/
* Method : GET
```
{
    "id": 2,
    "comment": [
        {
            "id": 2,
            "created_at": "2022-04-04T00:46:32.936881+09:00",
            "updated_at": "2022-04-04T00:46:32.936881+09:00",
            "content": "asd",
            "user": 1,
            "post": 2
        },
        {
            "id": 3,
            "created_at": "2022-04-04T00:52:43.022380+09:00",
            "updated_at": "2022-04-04T00:52:43.022380+09:00",
            "content": "abc",
            "user": 2,
            "post": 2
        }
    ],
    "like": [
        {
            "id": 2,
            "created_at": "2022-04-04T00:52:26.776129+09:00",
            "updated_at": "2022-04-04T00:52:26.776129+09:00",
            "user": 2,
            "post": 2
        }
    ],
    "file": [],
    "created_at": "2022-04-04T00:46:20.295188+09:00",
    "updated_at": "2022-04-04T00:51:05.388888+09:00",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed pellentesque lorem sed lorem posuere tincidunt. Sed finibus metus sed ante eleifend consectetur. Curabitur interdum nisl eu urna semper ornare. Curabitur varius sodales aliquet. Aliquam a elementum magna. Nam commodo auctor fermentum. In semper gravida est, ut condimentum risus consequat nec. Proin dapibus pellentesque rutrum. Morbi tincidunt nulla in porta convallis.",
    "like_count": 0,
    "comment_count": 0,
    "user": 2
}
```

### 새로운 데이터를 생성하는 API
* URL : api/posts/
* Method : POST
```
{
    "user" : 3,
    "content" : "새로운 글 추가하기"
}
```

```
{
    "id": 8,
    "comment": [],
    "like": [],
    "file": [],
    "created_at": "2022-05-07T02:29:30.093374+09:00",
    "updated_at": "2022-05-07T02:29:30.093374+09:00",
    "content": "새로운 글 추가하기",
    "like_count": 0,
    "comment_count": 0,
    "user": 3
}
```
### 특정 데이터를 업데이트하는 API
* URL : api/posts/5/
* Method : PUT
```
{
    "user" : 3,
    "content" : "기존 글 수정하기"
}
```

```
{
    "id": 5,
    "comment": [],
    "like": [],
    "file": [],
    "created_at": "2022-04-09T02:20:22.027060+09:00",
    "updated_at": "2022-05-07T02:30:55.446895+09:00",
    "content": "기존 글 수정하기",
    "like_count": 0,
    "comment_count": 0,
    "user": 3
}
```

### 특정 데이터를 삭제하는 API
* URL : api/posts/4/
* Method : DELETE

![데이터 삭제](https://user-images.githubusercontent.com/81256252/167183338-536382fb-7173-47c6-bda5-b7877a9d418e.PNG)


### 정리 
* FBV는 HTTP 메소드 조건문으로 구분
* CBV는 HTTP 메소드 클래스 내에서 각각 처리 가능
* CBV 확장 및 재사용 용이하지만 FBV 완전 대체 불가
* 403, 404, 500 에러 핸들링에는 FBV 사용
* `serializer.data` 유효성 검사 통과하고 save까지 완료된 애
  * `serializer.initial_data`는 유효성 검사 전에 접근할 때
  * `serializer.validated_data`는 유효성 검사 통과한 애한테 접근할 때


### 회고
CBV를 이용해 코드를 작성하니 가독성이 좋다. 클래스 내에 HTTP 메소드에 해당하는 함수를 만들고 이를 호출해서 사용하는 것이 HTTP 메소드를 if 문으로 구분하여 사용하는 것 보다 더 직관적이라는 생각이 들었다. 지난 주에 FBV를 제대로 사용하지 않고 바로 CBV를 사용한 것이 아쉬워 다음 과제 전에 FBV를 사용해보고 CBV와 FBV를 비교해 보아야겠다.  


<br>

## 6주차 <hr>

### FBV
```
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
```
viewset 리팩토링에 앞서 기존에 작성한 클래스 기반 뷰를 함수 기반 뷰로 리팩토링

### Viewset 리팩토링
views.py
```
class PostViewSet(viewsets.ModelViewSet):
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    
class ProfileViewSet(viewsets.ModelViewSet):
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
```
urls.py
```
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet)
router.register('profiles', ProfileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
```

### Filter
```
class PostFilter(FilterSet):
    user = filters.NumberFilter(field_name='user')
    like_count = filters.NumberFilter(field_name='like_count', lookup_expr='gt')

    class Meta:
        model = Post
        fields = ['user', 'like_count']
```
* 특정 유저가 작성한 포스트 필터링
* 좋아요 수 기준으로 포스트 필터링
```
class ProfileFilter(FilterSet):
    username = filters.CharFilter(field_name='user__username', lookup_expr='contains')
    image = filters.BooleanFilter(field_name='image_url', method='filter_image')

    class Meta:
        model = Profile
        fields = ['username', 'image']

    def filter_image(self, queryset, name, value):
        if value:
            filtered_queryset = queryset.exclude(image_url__exact='')
        else:
            filtered_queryset = queryset.filter(image_url__exact='')
        return filtered_queryset
```
* 유저 네임 필터링
* 프로필 사진 유무 필터링

### Permission
```
class PostPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user
```
* SAFE_METHODS (GET, OPTIONS, HEAD) : 누구나 접근 가능
* 이외 : 해당 포스트 작성자만 접근 가능

### Validation
```
def validate_phone(self, value):
        for char in value:
            if not char.isdigit():
                raise ValidationError("잘못된 형식입니다.")
        return value
```
* phone 필드에 숫자 이외의 문자 입력하면 에러

### 정리
* 필터 관련 문서 https://django-filter.readthedocs.io/en/stable/ref/filters.html
* permission
  * has_permission : 해당 요청 들어오면 항상 실행 
  * has_object_permission : 특정 유저와 대상 모두 확인하여 실행 
  * has_permission 실행 후 권한 확인되면 has_object_permission 실행
* validation
  * field level validation : 특정 필드 하나만 검사
  * object level validation : 필드 여러개 대상으로 검사 가능


### 회고
그동안 작성한 코드를 왕창 갈아엎었다. 처음 모델을 만들 때 공백 입력을 허용할 필드에는 null=True, blank=True를 모두 넣어주었다.
그렇게 조건을 넣어주니 공백이 null과 blank 두 가지로 저장되는 문제가 발생하였다. null=True는 제거하고 blank=True만 남겨 해결하였다.
또 프로필 시리얼라이저는 __all__로 모든 필드를 다 가져왔는데 자세히 보니 User 필드의 속성은 가져오지 못하고 있다는 것을 알았다.
프로필 시리얼라이저에 유저 이름을 가져오는 함수를 만들어 추가하였고, 프로필의 id 필드는 user 필드로 대체 가능하므로 id 필드는 가져오지 않는 것으로 수정하였다.
  
장고에서 제공하는 FilterSet에 다양한 기능이 내재되어 있어 비교적 편하게 필터 관련 기능을 구현할 수 있었다. 다만 포스트 permission은 제대로 작동하는데 
프로필 permission은 제대로 작동하지 않는 문제가 발생해 일단 해당 부분 주석 처리하였다. 프로필은 모든 메소드에 대해 해당 유저만 접근할 수 있도록 함수를 작성하였는데
확인해보니 다른 메소드들은 모두 다른 유저의 접근이 안되는데 DELETE 메소드는 해당 유저가 아니어도 접근 가능하다. ㅜㅜ 수정 필요
