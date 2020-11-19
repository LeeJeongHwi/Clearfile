# Appendix1. React-Dock

* react-dock은 사이드바 독을 의미함

```react
npm install react-dock
```

* 설정해줄 수 있는 인자
  * position
    * `[left , right, ,top , bottom]` , default : left
    * 말그대로 dock의 위치를 말한다.
  * fluid
    * window 사이즈(페이지 사이즈) 에 따라 크기를 자동 조절 되게 하는 기능 
  * size
    * dock Panel의 사이즈
    * 이 prop이 설정되면 Dock을 컴포넌트 처럼 사용가능
  * defaultSize
    * 말 그대로 default 사이즈를 의미 
  * isVisible
    * true 이면 dock이 보임
  * dimMode
    * none : dock요소가  dimmed 하지 않음 (우리는 이걸 쓰는 것이 맞는듯)
    * transparent : pointer event 들이 disable 됨
    * opaque : dock 외에 것(dim area)을 클릭시 dock을 close함
  * duration
    * animation의 Duration
  * dimStyle
    * dim Area의 Style (dock 외의 영역)
  * dockStyle
    * dock Area의 Style (dock 영역)
  * zIndex
    * Z-index (3차원)
  * onVisibleChange
    * dock의 isVisible을 바꾸고 싶을 때 사용
  * onSizeChange
    * 위와 동일하게 size를 바꾸고 싶을 때 사용
  * chdilren
    * ^^...모르겠음

