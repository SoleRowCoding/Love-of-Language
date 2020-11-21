# 언어의 사랑 프로젝트 파일 :: 안드로이드 환경
이 branch는 안드로이드 환경에서 '언어의 사랑'을 구동하기 위해 개발된 프로젝트 파일을 제공합니다. PC 등으로 강제 빌드는 가능하나, 정상적으로 동작한다고 보장 할 수 없습니다. 

리드 프로그래머 : 김학인 (PC빌드 대상 프로젝트 구축)
서브 프로그래머 : 이원진 (안드로이드 대응 및 최종 배포)

Ren'py자체 apk빌드 툴을 사용하여 빌드하며, 현재 API수준 29입니다.

# 버전관리
별도 개발 버전별, 기능별 브랜치는 생성하지 않으며 해당 브랜치에 커밋하며 원할 때 버전을 선언합니다.
체계적인 버전관리 방식을 택해야 하는 경우, 이 레포지토리를 수정하지 말고 fork후 별도의 레포지토리에서 진행하시면 됩니다.

# 소스 업데이트 규칙
* 업데이트를 하는 분은 본인이 작성한 코드에 버그가 있는지 면밀히 살펴야 할 의무가 있습니다. 별도의 코드리뷰나 풀리퀘스트 과정을 거치지 않고, 바로 커밋하기 때문입니다.
* 깃허브에 올라와있는 내용과, 배포된 빌드의 내용이 일치하는지 잘 살펴주세요. 

# 사용설명
스토리, 그리고 게임진행에 관여하는 모든 스크립트는 'script.rpy'에 있습니다. 별도 파일로 빼거나, 다른 기본파일에 포함된 내용은 없습니다. 단, '제작정보'(크레딧)은 screen.rpy에 있습니다. 이 외에는 모두 script.rpy에 포함되어있습니다.


개발에 관한 내용이 필요하시면 렌파이 메뉴얼을 참고하셔서 문제를 해결하시면 됩니다.
