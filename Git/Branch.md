# Git Branch

* 작업하고 있었던 소스코드를 그대로 두면서, Customizing에 해당하는 기능들을 추가할 때 사용
* 어떤 기능을 개발해달라했을 때, 필요없다고 나중에 버려질 것 같을 때 사용
* 서버에 반영할 때 Test, main 작업을 분리할 때 사용.. 그 외 여러가지 상황에서 사용

* 어떤 branch에 속해있는지에 따라 코드랑 소스파일 자체도 다름

## 명령어

* `git branch`

  * 현재 사용하고 있는 Branch 를 나타냄
  * master : 
  * `git branch [Branch name]`
    * Branch 생성
  * Branch를 생성했을 때 그때 현재 상태를 그대로 복사함
  * Option
    * `git branch -d [branch name]` : Branch 삭제

* `git checkout [branch name]`

  * Branch 변경

* `git log --branches --graph`

  * Branch들의 log를 볼 수 있다.
  * --graph 는 Branch의 graph를 볼 수 있음

  * --oneline 옵션은 한 줄로 표기

* `git log master..[branch]` 

  * master에는 없고 Exp에 있는 것을 비교해서 보여줌
  * -p 를 통해 소스코드까지 알아낼 수 있음

* `git merge [branch]`

  * 현재 branch에 특정 Branch와 merge(병합) 하는 것

  * Conflict 발생시 처리해주어야함.

  * Fast Forward

    * Merge를 하면 별도의 Commit을 생성하는 것이 아닌 Master가 가리키는 Commit을 바꾸기만 한다는 것!
    * 이 경우에는 Master는 변경사항이 없고 어떠한 Branch만 변경이 되었다면 이 현상이 일어남
    * 그 후 어떤 Branch를 삭제해주면 Master

  * Merge made by the "recursive" Strategy

    * 어떤 Branch가 Master가 변경되기 전 독립을 했고, Master가 Update가 된 경우에는 Fast Forward가 되지 않는다.

    * Git 은 Master와 해당 Branch와의 공통 Commit을 찾는다. 그리고 3 Way Merge 라는 내부적인 원리에 의해서..

      변경된 Commit과 어떤 Branch에서 있는 Commit을 합치고 새로운 Commit을 만든다.

### Branch 충돌 해결

* 같은 부분의 내용을 수정할 때, Merge 를 할 경우 Conflict가 발생한다.
  * Both Modified -> 병합하려는 브랜치 모두에 수정이 되었기 때문에 Merge가 불가한다 라는 뜻
  * ======= 를 중심으로 HEAD 는 현재 Checkout 한 Branch 
  * `>>>>>>>>> branch`  Branch에 해당하는 코드
  * 해당 정보를 바탕으로 직접 수정해야함!



### Git Stash

* 다른 Branch에서 작업을 하다가 Add 를 하지 않고 Master로 Checkout 시에 다른 Branch에서 수정한 내용이 Master에까지 영향을 준다.
* 따라서 add 하기 전 내용을 감추고 Master에 작업을 하고 다시 브랜치에 돌아와서 하고 싶을 때 Git stash를 사용한다.
* Stash는 버전관리를 하고 있는 파일에 대해서만 Stash가 적용 된다. (Untracked 되는 파일은 Add를 하고서)

#### 명령어

* `git stash save`
  * working directory, index state가 해당 Branch 에 Save 되었다! (WIP : 작업 중인 변경사항 등등....)
* `git stash apply`
  * save했던 작업이 살아남!
* `git stash list`
  * 우리가 명시적으로 삭제하지 않는 이상 해당 내용은 계속 살아있다..!
  * Stack 구조로 되어있고 Apply 했을 때 top에 있는 내용을 apply 한다.

