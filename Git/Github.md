# 원격 저장소 (Github)

지역 저장소와 대비됨

* 자신이 커밋하는 곳 - 지역 저장소
* 지역저장소와 동기화 되는 곳 - 원격 저장소



### 명령어

* `git init --bare`  --> 원격 저장소를 직접 만들 때 사용!
  * `.git` 에 해당하는 내용만 존재하는 저장소를 생성
  * 작업이 불가능하게 하는 저장소를 만들때 사용
  * 저장소로만! 사용하는 것
* `git remote -v`
  * 해당 Repo가 어디에 Remote 되어있는지 확인하는 것
  * `git remote remove [name]` remote 삭제
* `git push [origin] [branch name] ` 
  * 원격 저장소에 넣을 때 사용! (Push)
  * Option
    * `--set-upstream` master에서 Origin에 Push할때 자동으로 해준다
      * `git push` 만으로 master to origin으로 원격 저장소로 전송 가능
* `git pull`
  * push 된 Commit을 받는 것



## PR (Pull Request)

* 협업할 때 주로 사용함
* Branch를 따로 만들어서 작업하고 해당 작업 내용을 원본 저장소의 관리자에게 보내 관리자가 검토 후 Merge를 수행하도록 하는 것
* 코드 리뷰를 위함
* Push 권한이 없는 오픈 소스 프로젝트에 기여할 때



#### 진행과정

1. `git clone [github Repository 주소]` 
   * Repo 내용을 받아옴
   * clone 하면 자동으로 remote 되는 듯함!
2. `git remote add [name]`
   * 만약 Clone 할 때 자동으로 remote 되지 않는다면 추가
   * `git remote -v` 로 확인
3. `git checkout -b [branch]`
   * Branch 생성
4. `git add [수정된 것] / git commit -m [message]`
   `git push [origin] [branch]`
   * Branch 수정 내역을 [origin] (기본적으로 origin 으로 되어있음)
5. Push 받은 관리자가 Pull Request에서 코드 변경내역을 확인하고 Merge 여부 결정
6. `git branch -d [branch]`
   * Merge된 branch는 더 이상 쓸 일이 없으므로 삭제시킨다.

7. `git pull [origin]`
   * 끝난 뒤에 Local에서 merge 된 내역을 받는다.



