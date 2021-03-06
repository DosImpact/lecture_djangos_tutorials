# 장고를 프로젝트를 정리합니다.

## 1. Django elections
- 선거자 추가 -> 선거일 추가 

- 후보자들의 목록을 보여준다.
- 해당 선거일 기간내라면, 해당 국적의 후보자들을 보여주고 투표버튼을 누른다.
- 해당 선거일의 해당 후보자의 투표수가 증가한다.

- 처음 맛보는 DB이고, 3개의 모델이 엉켜있는데 처음에 어려웠음

1. HttpResponse HI 띄우기
2. HttpResponse 후보자 리스트 띄우기
3. render 후보자 리스트 띄우기
4. 후보자 지역구 선택 띄우기
5. DB 투표수 올리기
6. 결과 페이지 만들기


## 2. Django Tube

## 3. Django OpenCV WebApp

## 4. Django FucouOnMe

## 5. Django 웹크롤링 and 엑셀아웃풋


## x. github 사용방법 by생활코딩

1. 버전관리 하기

- git init 나는 여기 폴더를 버전관리를 할꺼야.
<br>

- git config --global user.name “Dos”
- git config --global user.email “ypd03008@gmail”
- git status 지금 상태를 보자 : 뭐가 버전관리가 안되는지 / 뭐가 수정 및 생성 인지/
<br>

- git add --all . working tree에서 버전관리 Staging Area로 추가하기
- git commit -m “first” 버전 업 및 메세지 노트,
- git log --stat :기록보기 간단하게 줄이 + 됬는지 - 됬는지만.
<br>

- git diff : 지금까지 커밋한 버전과 비교해서 달라진 점을 본다.
- git diff --stat :
- git reset --hard : 마지막 커밋 이후로 파일을 수정하는데 맘에 안들어서 마지막 커밋으로 되돌릴때.
- git log -p : 패치된 기록들을 본다. 수정된 줄이 +,-뿐만아니라 어떤 내용으로 바뀌었는지도.
<br>

- git log : 버전들의 기록을 본다.
- git checkout <버전> : 해당 버전으로 HEAD를 옮긴다.
- git checkout master : 최신 버전으로 HEAD를 옮긴다.


2. 백업하기

- git remote add origin https://github.com/DosImpact/djangos.git : 처음 한번만 등록을 하면 된다.
- git remote show origin : 리모트 현황 보기
- git push origin master : push하자 origin으로 master 브랜치를.
<br>

3. 협업하기
- git clone https://github.com/DosImpact/djangos.git : 처음 한번 땡겨오고 master 브런치가 생기면
- git pull : 그 다음부터는 pull로 동기화만 해주면 된다.

### x. 참고사항

pip freeze > requirements.txt : 요구되는 패키지 리스트 추출
pip install -r requirements.txt : 해당 리스트 패키지 설치하기.

DateBase : git clone 후 마이그레이션 꼭 하기, 그리고 DB에 쌓인 정보가 초기화 되므로.
media파일 관리도 처음부터 해야된다.(media 및 static은 파일 백업을 해 둘 것인데.. DB연동은 안됨.)

### x. 참조 사이트
장고 공식 문서를 하나씩 읽어가며 익히여랴 . Course Extends가 된다. 책,강의는 한계가 있음...
[Django Docs!](https://docs.djangoproject.com/ko/2.0/howto/static-files/)
[MDB Docs ~ ](https://mdbootstrap.com/docs/jquery/css/animations/)

Http스트리밍
[참고](https://stackoverflow.com/questions/49680152/opencv-live-stream-from-camera-in-django-webpage)
``` python

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        (self.grabbed, self.frame) = self.video.read()
        threading.Thread(target=self.update, args=()).start()

    def __del__(self):
        self.video.release()

    def get_frame(self):
        image = self.frame
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()

    def update(self):
        while True:
            (self.grabbed, self.frame) = self.video.read()


cam = VideoCamera()


def gen(camera):
    while True:
        frame = cam.get_frame()
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@gzip.gzip_page
def livefe(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace;boundary=frame")
    except:  # This is bad! replace it with proper handling
        pass

```