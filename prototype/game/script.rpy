image bg house_players = "images/house_players.jpg"
image bg black = "#000"
image phoneclock = "images/prologue_phone.jpg"
image bg campus_lectureBuilding_day = "images/campus_lectureBuilding_day.jpg"
image bg campus_ally_day = "images/campus_ally_day.jpg"
image bg campus_newBuilding_day= "images/campus_newBuilding_day.jpg"
image bg campus_etcBuilding_aisle="images/campus_etcBuilding_aisle.jpg"
image bg campus_otherClubroom="images/campus_otherClubroom.jpg"
image bg campus_newBuilding_hall="images/campus_newBuilding_hall.jpg"
image bg campus_clubroom ="images/campus_clubroom.jpg"
image bg campus_classroom_1_indoor = "images/campus_classroom_1_indoor.jpg"
image bg campus_classroom_1_outdoor = "images/campus_classroom_1_outdoor.jpg"


image bg loading_1 ="images/loadingScreen/ch01.png"
image bg loading_2 ="images/loadingScreen/ch02.png"
image bg loading_3 ="images/loadingScreen/ch03.png"
image bg loading_4 ="images/loadingScreen/ch04.png"


image senbai ="images/senbai_who.png"

image mirae general ="images/mirae_general.png"
image harin general ="images/harin_general.png"

image extra1="images/other_black_1.png"
image extra2="images/other_black_2.png"
image extra3="images/player_black.png"
image extras="images/others_black.png"


define harin_count=0
define mirae_count=0

define callignore=False
define playername="주인공"
define extraname="Player"
define m = Character("playername",dynamic=True, who_suffix = '@:~$',color="#4B89DC",who_text_align=-17.0)
define system = Character("system",color="#000000",who_suffix = '@:~$',who_text_align=-17.0)
define extra = Character("extraname",dynamic=True,color="#000000",who_suffix = '@:~$',who_text_align=-17.0)
define h1 = Character("윤미래",color="#8D43CA",who_suffix = '@:~$',who_text_align=-17.0)
define h2 = Character("유하린",color="#3e499d",who_suffix = '@:~$',who_text_align=-17.0)
define pauses = Pause(.5)

label start:
    stop music fadeout 1.0
    jump chapter2_2
    #prologue scene start
    $quick_menu = False
    scene bg loading_1 with dissolve
    $renpy.pause(4,hard=True)
    scene bg house_players with fade
    $quick_menu = True
    $renpy.pause(0.5,hard=True)
    play sound "audio/prologue_alarm.mp3"
    system "띠디디디.. 띠디디디..."
    m "커튼 사이로 줄기줄기 비춰오는  햇빛이 따스하게 마루바닥을 쬐고 있었다."
    m "창문을 열어논 탓인지 커튼이 흔들거리며 어서 일어나기를 재촉하였다."
    m "나는 손을 뻗어 옆에 요란하게 움직이는 자명종을 껐다." 
    stop sound
    m "이른 봄의 바람은 아직 겨울을 품고 있는 듯 찬 공기가 내 뺨을 스쳤다."
    m "나는 파묻힌 배개에서 얼굴을 들어 시간을 보았다."
    m "「아 씨.. 졸라 피곤하네 아직 8시 밖에 안됐네?」"
    m "「아침 수업이 9시까지 였던가? 5분만 더자볼까..」"
    m "「딱 5부 5분만 더자는ㄱㅓ....」"
    m "오늘 아침따라 유난히 더 피곤하다 어제 늦게잔 탓인가.."
    m "아아, 얼굴이 배개위로 멋대로 움직이고 있다.." 
    m "나는 스르륵 이불로 빨려 들어갔다." 
    m "zzzzz…"
    scene bg black with fade 
    $renpy.pause(2.0,hard=True)
    play sound "audio/prologue_alarm2.ogg"
    system "띠리링.. 띠리링..."
    m "눕는것도 잠시, 또 다시 시끄러운 소리가 들려온다."
    m "핸드폰의 비상 알람소리다.... 나는 눈이 떠졌다."
    m "「아 씨.. 시끄러워 죽겠네」"
    m "「벌써 5분 지난거냐??」" 
    m "「하아 졸라 피곤하네 진짜..」"
    m "나는 침대에서 반쯤 일어난 상태로, 휴대폰을 확인했다."
    $renpy.pause(1.0,hard=True)
    play sound "audio/prologue_surprise.mp3"
    m "!!!!!!!!!!!!!" with vpunch
    scene bg house_players with dissolve
    play music "audio/prologue_busy_bgm.mp3"
    show phoneclock at truecenter with dissolve
    m "'8시 50분'" 
    hide phoneclock with dissolve
    m "으아아아아아아아!" with vpunch
    m "5분만은 무슨, 이미 한참 지났네 미친놈아..!"
    m "수업 시작까지 10분전"
    m "다행히 지금부터 졸라 뛰면 출석 부르기전까지는 도착할만한 거리다."
    m "비몽사몽 하고 있을 시간이 없다 빨리 나갈 준비나하자."
    m "나는 빠르게 옷을 갈아입고 대충 씻은 채로 급하게 가방을 들고 나왔다."
    m "「첫날 부터 지각이라니 교수가 한소리하겠구만..」"
    stop music fadeout 1.0
    play sound ["audio/prologue_door.mp3","audio/prologue_runstep.wav"]
    scene bg black with fade 
    $renpy.pause(2.0,hard=True)
    system ".\/nameset"
label namechk:
    $playername=renpy.input("Enter name(less than 5) :",length=4)
    $namecheck=renpy.input("Is your name [playername]? (y/n) :")
    if namecheck == "y":
        jump namepass
    jump namechk
label namepass:
    m "내 이름은 [playername].\n{w}나이 23세 컴퓨터 공학부 2학년{w} 몇달전 군대에서 전역한 복학생이다."
    m "지금은 군대에서 받은 월급으로 대학 근처에 있는 원룸에서 자취중이다."
    m "군대에서는.. 나름대로 시간을 알차게 활용했다고 생각한다." 
    m "일과가 끝나면 틈틈히 시간나는대로 전공 서적도 읽고 스마트폰으로 코딩문제도 풀면서 지냈다."
    m "그래서 전역하고나면 열심히 공부해서 과탑이 되는 망상도 종종하곤 했는데"
    m "이게, 자유란걸 다시 맛보니까 사람이 생각보다 급속도로 나태해져버렸다."
    m "규칙적인 생활패턴 같은건 이미 초기화된지 오래, 군대가서 사람이 \n바뀐다는건 개소리다 얼마 못간다."
    m "당장 어제도 게임하느라 밤늦게 잤지?"
    m "뭐 결국에는 첫날 부터 최악의 시작이구만.."
    m "하아.."
    m "나는 인생을 곱씹으며 학교로 달려갔다."
    window hide
    #prologue scene end
label chapter1:
    #chapter 1 scene start
    $renpy.pause(3.0,hard=True)#챕터 넘어가는로딩
    scene bg campus_lectureBuilding_day with dissolve
    play music "audio/general_1.mp3"
    m "「휴 드디어 끝났다~」"
    m "첫 날 수업부터 지각할 뻔 했지만, 아슬아슬하게 제 시간에 출석했다." 
    m "첫 날이라 교수님들이 OT만 하고 일찍 수업을 마쳐주셨다."
    m "오후 수업까지는 시간이 남아 학교를 이리저리 둘러보았다. "
    m "「학교가 많이 변했구나」"
    m "저기 보이는 큰 건물은 입대 전만 해도 텅 빈 공터였다."
    m "친구들끼리 저기에 건물이 하나 있으면 좋을거라 이야기 하고는 했었는데"
    m "거짓말 같이 큰 강의동으로 바뀌어 있었다."
    m "그리고 운동장도 최근에 보수했는지 기구들이 새 것들로 교체되어 있었다."
    m "캠퍼스에 벤치도 없었는데, 곳곳에 벤치가 설치된 것을 보면, 학생회에서 일을 잘 해주고 있었구나 하는 생각도 들었다."
    m "그러고 보니 오전 수업 2개를 들을동안 어떤 여자애가 날 쳐다보는거 같았는데..."
    m "혹시? 이거 그린라이트..!"
    m "..."
    m "뭐 그냥 내 착각이겠지.."
    m "혼자서 시덥잖은 농담이나 하며 학교 주위를 무의미하게 걷고 있을 때였다."
    play sound "audio/chap1_phone.mp3"
    system "위이이이잉-"
    m "「음? 나한테도 전화란게 오긴 하는구나」"
    m "「역시 모르는 번호네」"
    m "핸드폰 화면에 생소한 전화번호가 떠있었다. 이걸 받아야 하나?"
    menu:
        "{color=#066de2}Act{/color}({color=#63a35c}\"그래 전화 걸어준게 어디야. 누군지는 모르지만 일단 받아 보자.\"{/color});":
            jump chapter1_1_1
        "{color=#066de2}Act{/color}({color=#63a35c}\"광고전화나 설문조사겠지. 그냥 무시하자.\"{/color});":
            $callignore=True
            jump chapter1_1_2
            
    label chapter1_1_1:
            stop sound
            stop music fadeout 1.0
            play music "audio/what.mp3" 
            play sound "audio/chap1_phone_answer.mp3"
            m "「여보세요...?{w} 누구신가요?」" 
            m "나름대로 정중한 말투로 물었다." 
            m "내 전화번호를 아는 사람이라니, 누구지?"
            #show senbai who at truecenter with fade
            $extraname="???"
            extra "「와~ 네가 받을까 긴가민가 하며 걸었는데{w}\n아직 핸드폰 번호가 그대로구나!」"
            m "수화기 너머 예상치 못한 활기찬 목소리에 내 머리속의 생각회로가 빠르게 굴러가기 시작했다."
            m "그리고 내린 결론은...."
            m "「….? 누구세요?」"
            m "순간적인 고민끝에 내놓은 대답에 잠깐 목소리가 끊겼다"
            m "장난스럽게 흐느끼는 목소리가 들려왔다."
            extra "「힝~~ 이 누님의 목소리를 잊다니 좀 섭섭한걸?」"
            extra "「설마 잠깐 못본 사이에 나를 기억 못하는 거니?!」"
            m "「저기, 죄송하지만 전화 잘못거신것 같아요..」"
            extra "「[playername]」"
            m "...내 이름을 아네..!?"
            extra "「[playername]씨 휴대폰 아닌가요?」"
            m "「아, 네 제가 [playername]맞습니다만.」"
            extra "「뭐야 그럼, 제대로 걸은거 맞네~!」"
            extra "「너 진짜로 내목소리 기억안나는구나??」"
            m "「네 그렇습니다만..」"
            extra "「풉ㅋ」"
            extra "「언어 마술사 동아리 방알지?」"
            extra "「내가 누군지 궁금하면 언어 마술사 동아리 방으로 와줄래?」"
            extra "「기다리고 있을테니까, 도망가면 안된다??~」"
            m "「예? 그게 무슨 말...」"
            play sound "audio/chap1_phone_answer.mp3"
            system "뚝-"
            m "물어보기가 무섭게 그녀의 전화는 의문만을 남기며 끊어졌다..."
            m "이 사람.. 누구였지?"
            m "군대에서 기억상실증이라도 걸린건가."
            m "내 이름이랑 동아리를 아는거보면 나를 아는건 맞는거같은데.."
            m "혹시..."
            m "음."
            m "일단 동아리실로 가볼까?"
            m "나는 동아실로 향했다."
            window hide
            jump chapter1_1

    label chapter1_1_2:
            stop sound
            m "뭐 전역해도 연락해주는 친구하나 없는데 통화 걸어준건 고맙네"
            m "맞다, 입대하기 전까지 활동하던 ‘언어 마술사 동아리'는 어떻게 되었을까?"
            m "동아리실 건물이 어디였더라..?"
            m "나는 동아실로 향했다."
            window hide
            jump chapter1_1

    label chapter1_1:
            stop music fadeout 1.0 
            $renpy.pause(0.4,hard=True)
            scene bg campus_ally_day with fade
            play music "audio/general_1.mp3" 
            m "'언어의 사랑'. 뭔가 촌스러운 이름을 가진 이 동아리는."
            m "내가 이 학교에 입학하고 나서 뜻 맞는 컴퓨터 관련학과 학부생들이 만들었다."
            m "아, 고딩때는 대학교 동아리에 대한 환상이 있었는데 깨진지 오래다."
            m "보통 동아리가 그렇듯이, 가끔 술이나 한잔 하면서 지내는 동아리나 다름없었다."
            m "물론 나는 회장이기도하고 그런쪽이기 보다는 구석에서 쳐박혀서 코딩이나했지만.."
            m "그런데 전역하니까 전혀 다른 소문을 듣게 되었는데" 
            m "내가 없는 동안 수많은 프로젝트를 진행했고, 대회에 나갔다 하면 상을 휩쓸어가는 전혀 딴판인 동아리가 되어있었다"
            m "게다가 코딩을 전혀 할 줄 모르는 사람도 가르쳐주고 있어서"
            m "학점 잘따려는 애들이나 코딩에 관심있는 사람들이 줄을 서고 있다고 한다."
            m "대체 술이나 마시던 동아리가 어떻게 제대로 돌아가게 된건지 궁금하구만."
            m "나는 가벼운 발걸음으로 동아실로 향했다."
            window hide
            jump chapter1_2

label chapter1_2:
    # Chapter 1 - section 2 script.
###############################

# 브금 루프 시작 : 기본_1
# 배경그림 전환 : (none) -> 학교 신축건물앞 낮
# 등장 : 주인공 : 왼쪽
#chapter 1 scene start 
$renpy.pause(0.4,hard=True)
scene bg campus_newBuilding_day with fade
          
m "...."
m "동아리방이 이렇게 큰 건물에 있다고?"
m "원래 낡아빠진 건물 구석에 있어야 할 우리 동아리가 왜 여기에.."
m "들어가보면 어떤 모습일지 상상이 안되네"

#퇴장 : 주인공
m "신축 건물앞에서 한참동안 입을 다물지 못했다"
m "1층 출입문 안쪽을 보니, 큼직한 편의점과 식당이 들어서 있었다."
m "우리 학교 건물이라 하기에는 너무 크다는 느낌을 받았다."
m "낯선 느낌이 드는 출입문을 젖혀 안으로 들어갔다"
#전환 : 학교 신축건물앞 낮-> (none)
window hide
stop music fadeout 1.0 
scene bg black with fade 
system "20분 전"
$renpy.pause(1.5,hard=True)
#루프 종료 : 기본_1

###############################

#브금 루프 시작 : 기본_2
#배경그림 전환 : (none) -> 학교 기타건물 복도
scene bg campus_etcBuilding_aisle with dissolve
play music "audio/general_2.mp3" 
m "동아리방을 오래도록 가보지 못했지만, 어디인지 단번에 알 수 있었다."
#효과음 재생 :knock
m "동아리방 문에 노크를 몇 차례 했다. 안에 사람들이 있었다."
#배경그림 전환 : 학교 기타건물 복도 -> 학교 다른 동아리방
#등장 : 주인공 : 왼쪽
scene bg campus_otherClubroom with dissolve
m "「안녕하세요」"
m "… ? "
m "문을 열고 들어가자 아는 사람이 한 명도 없었다. 동기 선배들은 어디에?"
#등장 : 엑스트라_1: 오른쪽
show extra1 at center with dissolve
$extraname="학생A"
extra "「새로 입부하러 오신분이세요? 기타동아리 온 것 맞으시죠?」"
m "기타 동아리? 그 새에 동아리 주제를 바꿔버린건가?"
m "「아, 저는 입부하러 온건 아니에요」"
m "「동아리 부원이었다가 군대를 갔는데, 이번에 복학하게 돼서 인사하려고 한 번 찾아와봤어요」"
m "「여기 ‘언어의 사랑' 맞죠?」"
extra "「아~ ‘언어의 사랑' 이요? 군대 다녀오셨다니 모르실만 했네요.」"
extra "「여기는 언어의 사랑은 아니고, 기타동아리에요.」"
m "순간 놀랐지만, 먼저 미안하다는 말을 건넸다."
m "혹시 ‘언어의 사랑'은 어디로 갔는지 알고 있느냐고 물었다."
extra "「언어의 사랑이 어디있냐면요. 저기 새롭게 지어진 건물 보이시죠? 여기서 천천히 걸어서 10분정도 걸려요」"
extra "「5~10층이 동아리방인데, 찾으시는 동아리는 7층에 있어요. 있는게 아니라, 7층을 전부 차지하고 있다는게 더 맞겠네요.」"
m "「알려주셔서 정말 감사합니다. 신축건물에 들어갔을 거라고는 생각도 못하고 있었어요.」"
m "「윗층들은 전부 게스트하우스가 될거라 들었었는데, 중간에 계획이 바뀌었나보네요.」"
hide extra1 with dissolve
#퇴장 : 엑스트라_1
#등장 : 엑스트라_군중 : 오른쪽 ** 한명짜리 검은색 아니고, 군중 검은색이에용.
show extras at center with dissolve
$extraname="학생B"
extra "「총학생회 친구 한테 듣기로는, ‘누군가'..의 입김이 불었다고 하더라구요. 확실한건 아녜요」"
extra "「계획이 변경되면서 온전히 강의실이나 연구실같은 시설만 들어서게 됐는데, 강의실이 생각외로 많이남았대요. 그 남는 자리로 동아리들이 많이 옮겨갔어요.」"
$extraname="학생A"
extra "「건물 보셨겠지만, 큰 매장이 하나 들어오는 줄로 착각하는 사람이 있을 정도로 정말 커요.」"
extra "「그 큰 건물 한 층 전부를 ‘언어의 사랑'이 차지한다고 오피셜이 떴을 때, 동아리 회장들이 정말 부러워했죠」"
extra "「부원이 아무리 많아도 그렇지,, 한 층을 쓰는건 전례가 없는 일이잖아요.」"
extra "「‘동아리에 학교에 영향을 줄만한 금수저가 있는게 아니냐’하는 이야기까지도 나온 적이 있어요.」"
extra "「이제 동아리로 곧장 가실거죠?」"
m "「네 바로 가보려구요. 자세히 알려주셔서 정말 감사합니다.」"
hide extras with dissolve
#퇴장 : 주인공
#퇴장 : 엑스트라_군중
#배경그림 전환 : 학교 다른 동아리방-> 학교 골목길 낮
window hide 
scene bg black with fade 
$renpy.pause(1.5,hard=True)
scene bg campus_ally_day with dissolve
m "건물 용도나 동아리실 배정이 어느 한 사람이 벌인 일이라니, 대체 무슨 소리야?"
m "소문이 이따금 말이 안되는 이야기이긴 하지만, 너무 뜬구름 잡는 이야기야."
m "시간이 조금 지체되어 마음이 급해졌다. 새로운 동아리실로 발걸음을 재촉했다."
#루프 종료 : 기본_2
stop music fadeout 1.0 

############################
window hide 
scene bg black with fade 
$renpy.pause(2.0,hard=True)
scene bg campus_newBuilding_hall with dissolve
play music "audio/general_1.mp3" 
#브금 루프 시작 : 기본_1
#배경그림 전환 : 학교 골목길 낮  -> 학교 신축건물 홀
m "그렇게 찾아온 건물 안에 들어서자 엘레베이터가 바로 눈에 들어왔다."
#효과음 재생 : 엘레베이터 종
m "7층의 동아리로 가기위해 홀수층 엘레베이터를 잡았다."
#효과음 재생 : 엘레베이터 문 여닫힘
m "버튼을 누르고 벽에 기댔다. 너무 오랜만에 동아리에 가는 탓인지 조금 떨렸지만, 이내 설렘으로 뒤덮였다."
window hide 
scene bg black with fade 
#배경그림 전환 : 학교 신축건물 홀  -> (none)
#재생 : 엘레베이터 종
#재생 : 엘레베이터 문 열림
#배경그림 전환 : (none)  -> 학교 언어의사랑 동아리방
m "..."
m "…?"
m "여기가 ‘언어의사랑' 이라고?"
$renpy.pause(2.0,hard=True)
scene bg campus_clubroom with dissolve
m "회사 사무실을 방불케하는 넓은 책상과 컴퓨터, 칸막이가 쳐있는 회의실, 그리고 한쪽에 쌓여있는 간식."
m "「대체 이게 다 뭐야?」"
m "그 순간 누군가 손을 흔들며 내 이름을 불렀다"
# 등장 : 선배_츄리닝_웃음 : 오른쪽
h1 "「여기야 여기 [playername] ! 오랜만이야 !」"
m "츄리닝을 입고 의자에 앉아 여유로이 돌고있는 모습"
m "밝은 목소리와 둥실둥실한 말투"
if callignore==False:
    m "나에게 전화를 걸었던 사람이 확실하다."
#등장 : 주인공 : 왼쪽
m "오랜만에 보는 얼굴이네."
m "「선배? 선배가 전화한거였어요?」"
m "「그리고 왜 여기계신거에요? 학생회장이 학생회는 어쩌구요?」"
show mirae general at center with fade
h1 "「학생회장? 끝난지가 언젠데 아직까지 학생회타령이야? 그 동안 총학이 두 번이나 바뀌었는데 말이야.」"
#전환 : 선배_츄리닝_웃음 -> 선배_츄리닝_기본
m "윤미래 , 2학년이 전례없이 학생회장이 된 것으로 큰 주목을 받았다.\n이에 더해 기존의 총학들이 해결하지 못하던 일들을 척척 해결해내며 학생들의 압도적인 지지를 받았다."
m "학생회의 높은 성과, 항상 놓치지 않는 과탑, 그러면서도 인간관계도 넓고원만한 사람."
m "흔히 말하는 '완벽하다' 라는 말을 붙이기에 딱인 사람이었다."
m "「그럼, 총학 임기 끝나시고 이제 우리 동아리에 붙어계시는거에요?」"
h1 "「임기 끝나고 바로 휴학했어. 다른 일 하다가 작년에 복학했는데 마땅히 갈 곳도 없어서 여기에 눌러앉았지.」"
h1 "「그 때가 너 면회갔을 즈음이었지.」"
m "나는 순간 주변을 돌아보았다. 방금 이야기는 아무도 못들은 것 같다."
m "미래 선배가 면회를 왔다는 이야기를 누군가 들었다가는.. 분노에 찬 시선으로 나를 바라봤을 것이었다."
h1 "「연말에 동아리 운영진 새로 꾸릴 시즌에, 네 친구가 나보고 회장 하겠냐고 물어오길래 그대로 대장이 되어버렸고」"
m "친구가 믿을만한 사람에게 회장을 줬다더니. 그게 미래 선배였어?"
m "「그래서.. 이제 천천히 설명을 들어보죠. 대체 동아리가 어쩌다가 이렇게 커진거에요? 이럴 곳이 아니었는데?」"
#전환 : 선배_츄리닝_기본 -> 선배_츄리닝_부끄럼
h1 "「당연히... 귀엽고 예쁜 내 얼굴 때문이지!」"
#전환 : 선배_츄리닝_부끄럼 -> 기본
m "「아..예」"
m "실없는 소리를 해도, 총학생회를 이끌던 능력은 어디 가지 않은 것 같다." 
m "동아리를 이렇게 키워내다니. 동아리가 예상보다 좋은 모습으로 남아있어 다행이라 생각했다."
m "「선배는 고등학교 때랑 달라진게 하나도 없네요?」"
m "선배는 나를 보고 옅은 미소를 지었다"
#전환 : 선배_츄리닝_기본 -> 선배_츄리닝_웃음
h1 "「음~ 너도 마찬가지야 [playername].」"
if callignore==False:
          h1 "「내 목소리 일부로 모르는척 하더라?ㅎ」"
else:
          h1 "「아까 내 전화 무시했지?ㅎ」"

m "「아니 그게 그건 그러려고 그런게 아니고」"
m "「죄송합니다..」"
m "나의 반응이 재미있었는지, 선배는 웃으며 말했다"
h1 "「장난이야 장난. 반응이 항상 재미있어서 놀리게되잖아.」"
#전환 : 선배_츄리닝_웃음 -> 선배_츄리닝_기본
h1 "「네가 온 걸 보니 다들 수업은 끝났을텐데, 첫 날이라 늦나보네. 좀 있으면 다들 올거야」"
h1 "「복학생이니 모르는 애들도 많을거야. 인사좀 나눠봐」"
h1 "「아 [playername] 회장님, 이젠 그냥 부원이네. 기분이 좀 색다르겠어?」"
m "「뭐 어차피 바지 회장이였는데. 부원이 오히려 편하겠네요」"
m "「거의 음주 친목 동아리였죠」"
m "「뭐 그때랑은 많이 변한거 같은데..\n요즘 동아리에서는 뭐해요? 제가 낄데가 있어요?」"
h1 "「벌써 일거리를 찾는거야? 아주 열의에 차있구만. 좋아.」"
h1 "「하지만 아직은 할 일이 없단다. 아직은 말이야.」"
m "아직은?"
m "어떤 의미인지 몰라 고개를 갸우뚱거렸다. 이내 선배가 내 마음을 읽은듯 대답했다."
h1 "「이 누나가 할 일을 주는건, 네가 아직도 전공지식들을 기억하고 있다는게 증명 된 뒤다!」"
m "선배는 서랍을 열어 종이뭉치를 꺼냈다. 작은 문제집 정도의 분량이었다."
m "「...이.. 이게뭐죠?」"
h1 "「혹~시 네 실력이 벌써 죽어버린건 아닌지 테스트 해볼 수 있는 문제지.」"
h1 "「그리 어렵지도 않아. 엄~청 기초적인 내용들이라구?」"
h1 "「내가 친히 직접 만들었다구. 얼마나 푸는지 한 번 보자.」"
m "나는 종이에 빼곡히 적힌 내용을 바라보았다. 고민하며 써내려간 흔적이 선배의 필체에 스며있었다."
m "「하아.. 귀찮은데 너무 무시하는거 아닙니까?」"
m "「..맞춰볼테니, 어서 문제나 주세요.」"
h1 "「그런 자세 좋은걸? 여기 문제지!」"

hide mirae with dissolve

m "좋아 그럼 풀어볼까?"
$isanswer=0
system "문제1.{w}\nCPU는 무엇의 약자인가?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"Central Park Ubiquitous\"{/color});":
     $isanswer
 "{color=#066de2}Answer{/color}({color=#63a35c}\"Central Processing Unit\"{/color});":
     $isanswer+=1
     

system "문제2.{w}\n부동소수점의 의미는?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"움직이는 소수점\"{/color});":
     $isanswer+=1
 "{color=#066de2}Answer{/color}({color=#63a35c}\"고정된 소수점\"{/color});":
     $isanswer

system "문제3.{w}\nC언어를 만든 사람으로 가장 적절한 답은?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"데니스리치\"{/color});":
     $isanswer+=1
 "{color=#066de2}Answer{/color}({color=#63a35c}\"비아르네 스트로우스트루프\"{/color});":
     $isanswer
system "문제4.{w}\n데드락은 서로다른 프로세스가 자원을 점유한 상태에서 상호배제 정책에 의해 나타나는 현상이다. 이를 대표적으로 설명하는 모델은?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"테스트 점유 모델\"{/color});":
     $isanswer
 "{color=#066de2}Answer{/color}({color=#63a35c}\"식사하는 철학자들\"{/color});":
     $isanswer+=1
system "문제5.{w}\nOSI 7 Layer에서 가장 낮은 계층에 존재하는 단은?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"Physical\"{/color});":
     $isanswer+=1
 "{color=#066de2}Answer{/color}({color=#63a35c}\"Application\"{/color});":
     $isanswer
system "문제6.{w}\nStack 자료구조에서 데이터를 넣는 동작을 이르는 말은?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"Push\"{/color});":
     $isanswer+=1
 "{color=#066de2}Answer{/color}({color=#63a35c}\"Pop\"{/color});":
     $isanswer
system "문제7.{w}\n정렬된 정수(intager)배열에서 특정 원소를 찾고자 할 때 가장 빠를 것으로 예상되는 알고리즘은?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"넓이우선탐색\"{/color});":
     $isanswer
 "{color=#066de2}Answer{/color}({color=#63a35c}\"이진탐색\"{/color});":
     $isanswer+=1
system "문제8.{w}\nC언어에서 변수를 생성하고 메모리 주소를 할당하는 행위는?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"선언(Declaration)\"{/color});":
     $isanswer
 "{color=#066de2}Answer{/color}({color=#63a35c}\"정의(Definition)\"{/color});":
     $isanswer+=1
system "문제9.{w}\n 튜링기계의 구성요소로 맞는 것은?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"누산기\"{/color});":
     $isanswer
 "{color=#066de2}Answer{/color}({color=#63a35c}\"제어기\"{/color});":
     $isanswer+=1
system "문제10.{w}\n다중프로그래밍에서 '페이징'기법에 맞는 설명은?"
menu:
 "{color=#066de2}Answer{/color}({color=#63a35c}\"Frame이라는 일종의 섹션으로 메모리를 나누어 관리\"{/color});":
     $isanswer+=1
 "{color=#066de2}Answer{/color}({color=#63a35c}\"프로그램을 View와 일치하는 Segment로 나누어 메모리에 탑재\"{/color});":
     $isanswer

m "후~ 끝이네."
h1 "「뭐야 다풀었어? 채점하자!」"

window hide
$renpy.pause(1.5,hard=True)


show mirae general at center with dissolve
if isanswer <= 3:
    h1 "「너.. [playername] 맞아?」"
    h1 "「충격인데 군대 가더니 머리가 많이 굳었나보네.」"
    m "「크음..{w} 원래 그런 전공 내용들은 자주 안보면 까먹는게 정상이라구요..」"
    h1 "「하아.. 신입 부원들좀 가르칠려 했는데 너부터 공부시켜야겠네.」"
elif isanswer <= 6:
    h1 "「뭐야 어느정도 기억하고 있는데? 신입 부원들 가르치기에 차고넘치는 변함없는 실력이야.」"
elif isanswer > 6:
    h1 "「군대에서도 공부 열심히 했나본데? 하나도 안잊어버렸잖아.」"
    m "「이 정도는 기본적으로 기억하고 있죠.」"
    h1 "「이 누나가 보는 눈이 틀리지 않았다. 당장 신입 부원들 가르칠 준비를 하자구!」"
m "「신입생들을 가르친다니요?」"
h1 "「학기초 동아리 가두모집 시기에 신입생들 대상으로 OT를 하고있어. 아직 누가 할지 정하진 못했는데, 네가 해보는건 어때?」"
h1 "「다들 어떻게 생각해?」"
m "「문제 푸느라 정신없는 사이, 부원들이 하나 둘 들어와 제 할일을 하고 있었다.」"
#퇴장 : 선배_츄리닝_기본
#등장 : 엑스트라_군중 : 오른쪽
show extras at left with dissolve
$extraname="부원A"
extra "「1대 회장님이라면서요. 잘 하시겠죠.」"
$extraname="부원B"
extra "「회장님이 골랐으면 믿을만한 사람이겠죠. 신입부원도 아니고 전 상관없어요.」"
$extraname="부회장"
extra "「그럼 OT계획은 회장님이 계획하시는 대로 확정지을게요」"
m "짜고 치는듯한 이 분위기.."
#퇴장 : 엑스트라_군중
#등장 : 선배_츄리닝_기본 : 오른쪽
m "선배는 내 표정을 읽더니 웃었다."
m "「저기요.. 제 의사는..」"
h1 "「이제 눈치챘어? OT를 도맡을 사람은 이미 정해져있었지!!」"
h1 "「바로 우리 컴공과 수재 [playername]씨!」"
h1 "「잘 부탁해 1대 회장님~~」"
hide extras with dissolve
hide mirae with dissolve
m "「잠깐! 거기서 ㅆ..」"
m "선배는 빠르게 내시야에서 사라졌다."
#퇴장 : 선배_츄리닝_기본
m "「하아 당했다..」"
#퇴장 : 주인공
#브금 루프 종료 : 기본_1
#배경그림 전환 : 학교 언어의 사랑 동아리방  -> (none)
window hide
stop music fadeout 1.0
scene bg black with fade 

label chapter1_3:
# Chapter 1 - section 3 script.
###############################
$renpy.pause(1.5,hard=True)
play music "audio/general_2.mp3" 
scene bg campus_classroom_1_indoor with dissolve
# 브금 루프 시작 : 기본_2
# 배경그림 전환 :  (none) -> 학교 강의실 1 안
# 등장 : 주인공 : 왼쪽
m "1주일 정도 지나고. 여러 자료들을 수집하고 이것저것 부원들한테 물어보면서 OT를 준비한 상태로 동아리 강의실에서 대기하고 있었다."
# 등장 : 선배_츄리닝_기본 : 오른쪽
m "선배는 동아리 입구 앞에서 부원들은 발 빠르게 돌아다니면서 관심 있는 신입생들 한테 이것저것 나눠주면서 설명하고 있었다."
m "나중에 취업할 때 포트폴리오 작성에 유리 할 것이다, 유명 대기업에 취업한 후기들도 들을 수 있다는 등등 다양하게 설명하는 것이 눈에 들어왔다"
# 퇴장 : 선배_츄리닝_기본
# 등장 : 엑스트라 군중 : 오른쪽
show extras at left with dissolve
show extra1 at center with dissolve
$extraname="학생A"
extra "「이거 다 사실인가요? 기분 나쁘게 들으실 수 있지만 보통 하는 척만 하고 노는 곳으로 변질되는게 대다수라고 들어서요.」"
$extraname="부원A"
#등장 : 엑스트라_1 : 가운데
extra "「친구가 걱정하는 것도 당연해요. 저도 처음에 들어올 때 그 생각을 했거든요. 친구들의 노력에 따라 다르기는 하겠지만 프로젝트와 다른 여러 활동에 성실히 참여하면 좋은 결과를 낼 수 있을 거에요」"
extra "「그리고 친구가 컴퓨터 공학과 아니에요? 그러면 포트폴리오 작성에도 이득인 부분이 많을 거고요. 또한 스터디룸도 존재하니 도서관에 자리가 없을 경우 이곳으로 와도 됩니다.」"
extra "「모르면 물어볼 수 있게 공부 잘하는 부원들이 대기하고 있어요. 한 번 생각해 보세요~」"
$extraname="학생B"
extra  "「야야 이거 우리 할만한데? 어때?」"
$extraname="학생C"
extra "「일단 OT 강의도 있으니 한번 들어보고 해보자.」"
hide extras with dissolve
hide extra1 with dissolve
m "하아.. 갑자기 발표라니 정말 귀찮아 죽겠네.."
#퇴장 : 엑스트라_군중
#퇴장 : 엑스트라_1
#등장 : 선배_츄리닝_기본 : 오른쪽
show mirae general at center with dissolve
h1 "「오이오이! [playername]~ 준비는 잘 해 왔어~?」"
m "이 인간 진짜.."
m "옆에서 히죽히죽 거리는 선배를 보니 머리가 지끈지끈해졌다."
#등장 : 주인공
m "「이렇게 중요한 역할을 왜 나한테 맡긴 거죠?! 그리고 회장이면 오늘만큼은 추리닝은 아니잖아요!」"
h1 "「그치만 이게 편한걸~ 게다가…. 이 차림도 나쁘지 않잖아?」"
m "나는 다시 선배를 다시 바라보았다."
m "찰랑이는 갈색 머리결, 뚜렷한 갈색 눈동자, 그리고 보라색 츄리닝이 은근 조화를 이루고 있었다."
m "「입만 좀 다물면 참 이쁠텐데」"
m "..!?{w} 말이 헛나왔다."
h1 "「응? 너 방금 뭐라고 했어?」"
m "선배의 목소리에 나는 퍼뜩 정신을 차렸다."
m "「아니 그.. 선배는 옛날이나 지금이나 이..이쁘시네요 하하하...」"
h1 "……"
hide mirae with dissolve
m "선배가 화났는지 고개를 돌리며 아무 말도 하지 않았다. 이건 위기다!"
m "「맞아 이번에 와플가게가 새로 생겼다고 하던데 다음에 같이가요! 평도 4.3으로 좋고 후기들도 나쁘지 않아요!」"
show mirae general at center with dissolve
h1 "「그…그래….」"
m "부원들은 이제 시간이 되었는지 강의실로 안내하였고 신입생들은 강의실에 모여 자리를 잡고 있었다."
$extraname="부원B"
extra "「자 이제 곧 OT 강의 할 시간이니 준비 하세요~!」"
m "부원중 1명이 나를 보며 이제 시간이 되었다는 것을 알렸다."
h1 "「이제 할 시간인가 보네 홧팅~!」"
m "다시 돌아온 발랄한 목소리에 나는 내심 안심하면서 대답하였다."
m "「예예~」"
hide mirae with dissolve
window hide 
scene bg black with fade 
$renpy.pause(1.5,hard=True)
m "「여러분이 나중에 커서 어떤 일을 하시게 될지 미래가 분명하지 않습니다. 하지만 여러분은 1학년 이므로 여러 경험을 할 기회가 넓습니다. 동아리 체험 느낌으로 오셔도 되니 경험 해 보시고 입부하셔도 됩니다.」"
m "「일단 체험하고 싶으신 분은 밖에 비치된 이 종이를 작성해주세요. OT를 마치겠습니다. 감사합니다!」"
scene bg campus_classroom_1_indoor with dissolve
m "발표를 마치자 신입생들은 자리에 일어서 나가기 시작하였다. 나는 조용히 숨을 돌리며 물을 마셨다. 그러나 아직 안나간 한 사람이 보였다."
#등장 : 후배_검은색 : 오른쪽
m "「제가 준비한 OT 는 끝났고요 혹시 저한테 개인적으로 물어보실 말씀이라도 있나요?」"
$extraname="???"
show harin general at center with dissolve :
    xzoom -1
extra "………"
m "「아 혹시 말로 꺼내기 어려우시면 동아리 톡도 있으니 그곳에서 익명으로 대화하시면…」"
m "긴머리를 하고 있는 학생이 내쪽으로 오고있다."
m "「..저기?」"
extra "「찾았다….」"
m "「..예?」"
m "그녀는 고개를 들더니 내얼굴을 똑바로 마주 보았다."
extra "「진짜로 이학교에 계셨네요!!」"
extra "「오랜만이네요 [playername] 오빠…」"
m "「오빠요??!!」"
m "모르는 여자애가 갑자기 아는 척을 한다. 나 또 기억상실증 걸린건가?"
m "「저기 미안한데 누군지 기억이..」"
m "이사람 갑자기 싸늘한 표정으로 변했다.."
extra "「아무리 중학교때 이후로 본적 없다지만 우리 사이에 아예 기억도 없는건」"
extra "「사람으로써 좀 아니라 생각되네요.」"
m "중학교라..{w}중학교때 알던여자애.."
m "「혹시 하…린이?」"
#전환 : 후배_검은색-> 후배_츄리닝_웃음
#루프 종료 : 기본_2
stop music fadeout 1.0
#루프 시작 : 기본_3
play music "audio/general_3.mp3" 
h2 "「드디어 알아채셨네요 오빠!」"
m "이 녀석 태새전환 무서워..."
m "유하린, 어릴때 부터 알고지낸던 동생인데  중학교때까지 같은 학교 다니다가 갑작스럽게 해외로 이사를 가 그 이후로 얼굴을 볼 수 없었다."
m "가끔씩 이메일을 주고 받았지만 어렸을 적의 모습과 많이 달라져 있는 그녀를 보니 새로워진 느낌을 받았다."
m "못본사이에 많이 변했네? 못알아볼만했다."
#전환 : 후배_츄리닝_웃음 -> 후배_츄리닝_기본
m "「그래서 외국 생활은 할만했어?」"
m "그녀는 그동안 외국에서 어떻게 지냈는지,이 학교는 어떻게 들어온건지 대해 이야기하였다."
h2 "「별거 아니야 그냥 공부해서 들어온 것일 뿐이야.」"
h2 "「나같은 사람들도 입학할수있는 제도가 다 있거든」"
m "「원래 이쪽 분야로 들어올려고 한 거였어?」"
h2 "「뭐…그렇지…. 일단 오빠, 난 이거 작성하고 올게..」"
m "「어..그래 좀 이따가 못한 이야기 하자!」"
hide harin with fade
#퇴장 : 후배_츄리닝_기본
m "휴 뒷정리는 이쯤이면 된거같다. 몸이 구석구석 쑤신다, 피로해.. 빨리 쉬러가자"
#루프 종료 : 기본_3
#전환 : 학교 강의실 1 안 -> 학교 강의실 1 문밖
#등장 : 선배_츄리닝_기본 : 오른쪽
stop music fadeout 1.0
scene bg campus_classroom_1_outdoor with dissolve
show mirae general at right with dissolve
h1 "「음 [playername], 저런 귀여운 여자친구가 있었네~」"
h1 "..."
hide mirae with dissolve

window hide 
scene bg black with fade 
$renpy.pause(2.0,hard=True)

label chapter2_1:
$quick_menu = False
scene bg loading_2 with dissolve
show harin general at right with dissolve
$renpy.pause(4,hard=True)
hide harin with dissolve
scene bg campus_clubroom with fade
$quick_menu = True
play music "audio/general_3.mp3" 

m "OT 강의를 마친 이후 선배로부터 기분 좋은 소식이 담긴 문자를 받게 되었다."
h1 "「그거 알아? 작년 보다 입부한 학생이 거의 2배가 2배! 역시 내가 고른 사람은 틀림없이 잘된다니까 후후~」"
m "이런 뒷문장을 넣을 필요가 없어 보이는데….. 그리고 밑줄에 추신형식으로 자유롭게 동아리 활동 해도 된다고 하였다."
m "그리고 하린이한테도 동아리에 입부 한다고 문자가 왔다. 여튼 귀찮은 일들이 잘풀려서 다행이다."
m "단지.."
# 등장 : 후배 츄리닝 기본 : 오른쪽
show harin general at center with dissolve 
h2 "「선배, 오후엔 저랑 같이 수업… 옆자리에서 같이 들으실래요?」"
hide harin with dissolve
# 퇴장 : 후배 츄리닝 기본
# 등장 : 선배 츄리닝 기본 : 오른쪽
show mirae general at center with dissolve
h1 "「[playername]! 내일 오전 수업에 보자!」" 
hide mirae with dissolve
# 퇴장 : 선배 츄리닝 기본

m "빠르게 수강신청을 올클했는데 아이러니하게도 오전에는 미래 선배와 같은 수업을 오후에는 하린이와 같은 수업을 듣게 된 것이였다.."
m "뭐 이런 우연이 있을수도 있지."
m "「그런데 너희들 눈빛이 왜그러냐 앙?」"
$extraname="깝쭉이"
extra "「너가 우리 학교의 여신하고 같은 수업인거야? 여신이 너한테 무슨 잘못 했어?」"
$extraname="여미새"
extra "「이번에 온 신입생 중에 청순한 여자애 잇던데 걔랑 아는 사이야? 나 좀 소캐시켜봐바.」"
$extraname="오타쿠"
extra "「오이오이, [playername]쿤! 이 녀석 복학하니까 아예 하렘만드는 거야?. 거의 라노벨 급이야.」"
# 등장 : 주인공 : 왼쪽
m "「하아.. 그니까 말이야 그 두사람은 오랫동안 알고 지내온 사람들이라고 뭐가 불만인건데?」"
$extraname="친구들"
extra "넌 우리 연합을 배신했다!"
extra "이 기만자 녀석.."
# 퇴장 : 엑스트라 군중
m "하아.. 내친구들이지만 어째 정상적인 녀석이 한놈도 없는것같냐.."
m "오늘도 수업이 끝나고 나중에 만나서 무슨 말을 할지 상상하고 있었다."
m "뭐, 정작 2명은 아무 상관도 안하는 눈치지만."
window hide 
scene bg black with fade 
$renpy.pause(1.5,hard=True)
scene bg campus_lectureBuilding_day with dissolve
# 배경그림 전환 : 학교 언어의사랑 동아리방 -> 학교 강의동앞 낮
# 등장 : 후배 츄리닝 기본 : 오른쪽
h2 "….배 선배!"
m "나는 소리가 나는 방향으로 고개를 돌렸다. 하린이가 나보고 오라고 하는 손짓을 보내고 있었다."
show harin general at center with dissolve 
m "「아 벌써 다음 수업이 시작되나? 빨리 가자.」"
h2 "「그게 아니라… 다음주 축제 때 무엇을 할지 [playername] 선배는 정하셨어요?」"
m "하린이는 건물 앞에 있는 게시판을 가리키며 말을 꺼냈다."
m "게시판에는 다양한 학과들이 무엇을 할 것인지 홍보하는 문구가 붙여져 있었다. 그 중에서 술을좋아하는 내가 관심이 가는 건 칵테일 쇼 였다."
m "「나는 복학생이니 즐길려고 해. 이번에 가볼만한건 칵테일 쇼..려나?」"
h2 "「그러면 제가 하는 부스에 구경하러 오신다는 거네요! [playername]선배 오기만을 기대해도 되는거죠?」"
m "하린이는 활짝 웃으며 나를 바라보았다. 얘가 칵테일쇼? 뭔가 오버렙이 되지 않았다."
m "「이런걸 너가 배웠다고 음…. 사고 안나는지 내가 지켜 봐야겠는데.」"
h2 "「제가 이걸 위해 자격증을 땃다고요! 게다가 [playername] 선배가 술을 좋… 아니 관심 많은걸 아니 여러가지 가르쳐 줄려고 이 축제를 얼마나 기대했는데!」"
m "「음? 내가 그런걸 말했었나? 그걸 어떻게 알았어?」"
h2 "「아….그게….아 프로필 사진에 뒤에 술들이 가득한 것을 봤죠! 그걸 보고 [playername] 선배가 술 좋아하는걸 바로 유추 한 거에요.」"
m "하린이는 약간 내 시선을 피하면서 대답을 하였다. 나의 취미를 어떻게 아는지 좀 더 물을려고 할 때였다."
$extraname="여학생"
extra "「하린아~ 이제 준비하러 사러 가야될 시간이야! 애들 다 모였어!」"
h2 "「아 그래 바로 갈께! 선배 저 이제 가야 될 거 같아요 축제 때 제 부스에 꼭 와줘요!」"
m "「그래 그래 너도 어서 가.」"
m "그나저나 어느새 나한테 선배 선배 존댓말 쓰네.."
m "뭐 나야 좋지~"
hide harin with dissolve
# 퇴장 : 후배 츄리닝 기본
m "축제가 벌써 일주일로 다가온 가운데 학교 거리를 걷다보니 벌써 부스 장소가 정해졌는지 정해진 곳에서 분주하게 준비하는 학생들이 보였다."
# 등장 : 선배 츄리닝 기본 : 오른쪽
m "입구에서 선배의 모습이 보였다. 주변에 있는 사람들은 학생회 옷을 입고 있었다. 아마 학생회가 바뀐지 얼마 안돼서 선배한테 물어보는 듯 하였다."
h1 "「여기서는 사람들이 많이 모이기 때문에 집중적인 케어가 필요한 부분이야. 사람 대략 6명 정도 배치해서 안내하면 될꺼야.」"
$extraname="학생회A"
extra "「그럼 학생회 인원이 대략 20명이니 2교대하면서 해야겠네요. 나중에 궁금한게 있으면 또 물어볼께요.」"
h1 "「오케오케, 동아리에 있으니 직접 와도 되고 이야기 길거 같으면 공물도 가져와야되!」"
$extraname="학생회B"
extra "「하하하하 알겠어요. 오늘은 어디 가면 안되요!」"
m "학생회 부원들은 서둘러 다른 곳으로 항하였고 선배는 옆에 있는 상자를 들어올리다가 나랑 눈이 마주치게 되었다."
show mirae general at center with dissolve
m "「어, 안녕하세..」"
h1 "「[playername]! 마침 잘 됐다 여기서 상자 들고 기다려봐!」"
m "「네? 저기요 잠만..」"
m "선배는 내 말이 끝나기 전에 학생회 건물에서 다른 상자를 들고 나왔다. 이 상자들을 봐도 대충 게임할 때 쓰는 기기들 같은데…."
h1 "「마침 만나서 다행이야! 아니였으면 이 누님이 직접 2번 왔다갔다 해야 했어!」"
m "「어째서 제가 상자를 든다는 전제가 깔려 있는 거죠?」"
m "어느 순간 나도 모르게 상자를 들고 선배와 같이 동아리실로 향하고 있었다. 선배는 나의 씁쓸한 표정에 약간 볼을 부풀렸다."
h1 "「뭐야~ 내 일 도와주는게 그렇게 싫은 거야? 게다가 내가 너한테 좋은 걸 알려주려고 하는데.」"

####
# 분기 2_1_1
m "이건 분명히 부탁할 때 쓰는 표현이다. 이걸 어캐 받아쳐야 하지?"

menu:
 "{color=#066de2}Say{/color}({color=#63a35c}\"보통 진짜 좋은 거면 남한테 잘 알려주지 않는데…\"{/color});":
     h1 "「내가 [playername]이니까 막 알려줄려고 하는거지! 힌트는 이 박스야!」"
     m "「이 박스로 무언가 할 예정인가요?」"
     h1 "「그래! 이걸로 우리의 동아리 행사를 너한테 총괄할꺼야!」"
 "{color=#066de2}Say{/color}({color=#63a35c}\"아 잠만 제가 먼저 대답할께요. 정답은 이 박스에 있는 거죠?\"{/color});":
     h1 "「오 뭐야~ 눈치 야아아악간 부족한 [playername]이 바로 알아채다니!」"
     m "「선배 옆에 있으면 이건 늘수 밖에 없죠. 이 박스로 무엇을 할려는 건가요?」"
     h1 "「응응 이번에 너한테 2개 박스와 함께 동아리 활동의 운명을 맡길꺼야!」"


m "결국 또 이렇게 걸려드는 구만.."
m "그나저나  이 기기들, 자세히 보니 꽤나 비싸보이는데 이렇게 박스로 대강 챙겨와도 되는건가."
m "「잠만, 이거 비싸보이는데  대강 들고 가도 되는 건가요?」"
h1 "「응 이거 vr 체험 기기들인데?」"
m "나는 깜짝 놀라 하마타면 이 금덩어리들을 놓칠 뻔 했다."
m "자세히보니 싸구려 스마트폰 vr이 아니라 제대로된거다..."
m "「이걸 여러개나?!?!??! 대체 돈이 어디서..」"
h1 "「응, 이번 동아리 활동비 다 털어서 산거야. 근데 부피 자체가 커서 한꺼번에 옮겨올 수가 없더라고. 아 참, 이건 부원들한테 동의 구해서 산거다?」"
m "「이렇게 귀한걸 선배가 부스 관리를 해야죠. 왜 제가 그걸 굳이 해야 되는 건데요?」"
m "그 뒤에 선배가 내 반응을 예상했듯이 대답하였다."
h1 "「이번에는 학생회 일을 도와줘야 할거 같아. 무수한 SOS 요청이 지금 날라 들어오거든.」" 
h1 "「게다가 이번에 동아리에서 VR 체험을 위해 작년부터 진행해 만들어 놓은 게임들이 있어.」"
h1 "「이걸로 VR 체험을 다른 사람한테 진행 시키면 되는거야. 뭐 간단한 거라 3개 밖에 없긴 한데 뭐 재밌으면 되지 않을까?」"
m "「그래도 이걸 위해서 예산을 쓰는건 좀….」"
h1 "「끝나고 나서도 동아리 부스에서 설치해 계속 쓸수 있잖아? 게다가 다른 곳에가서 체험하려면 1시간에 2-3만원 주는 것보단 여기서 마음껏 쓰는게 부원들한테는 좋을꺼야.」"
m "「복학생인 저보다는 다른 사람한테 맡기는게 낫지 않을까요? 전 막 복학한 참이라 많이 까먹었을거 같고 게다가 서기들도 있잖아요?」"
h1 "「음 그것도 일리 있네.」"
h1 "「하지만 그들도 다른 일들이 있어 바쁘다고 연락을 받아서. 다음으로 동아리 활동에 대해서 잘 아는 너가 적격이라고 생각해.」"
h1 "「별거 아니야 너가 부스 관리만 해주면 되 나머지는 개발한 친구들이 설명할꺼니까.」"
m "「선배의 진지한 목소리에는 오랫동안 고심하여 결정을 내린 선배의 마음이 배어나왔다.」"
m "그 모습을 본 나는.."
m "「네 알겠습니다.. 관리만 하는 거라면 맡겨 주세요.」"
m "이번이 마지막이야.. 정말!"
h1 "「오키! 그러면 다음주에 잘 부탁한다고! 오전만 하면 되니까 금방 끝날꺼야!」"
m "선배는 내가 일을 맡은 것에 기쁜 건지 평상시의 둥실한 표정으로 돌아왔다. 그렇게 난 다음주의 축제 준비를 위해 선배와 같이 빠른 걸음으로 동아리 실로 향하였다."
hide mirae with dissolve
window hide 
scene bg black with fade 
stop music fadeout 1.0
$renpy.pause(2.0,hard=True)

label chapter2_2:
scene bg campus_clubroom with dissolve
play music "audio/travel.mp3"
# Chapter 2 - section 2 script.
###############################

# 브금 루프 시작 : 여행
# 배경그림 전환 : none -> 학교 언어의사랑 동아리방
m "학교 축제 당일, 축제로 유명한 학교답게 철저히 준비하려는 학생들이 많았다."
m "축제를 즐기려는 외부 학생들도 많이 찾아와 입구에서 줄을 서며 기다리고 있었다."
m "선배는 새벽부터 학생회 일을 도와주고 있었고 후배도 분주하게 부스 준비하느라 바쁜게 눈에 보였다."
m "우리 부스도 바쁘게 준비하여 막바지에 이르고 있었다. 나는 학생회 사람들과 이야기 하면서 문서를 작성하고 있었다."

m "이야기가 끝나고 일을 마치고 난 뒤 나는 부스로 되돌아 왔다. 부원 3명이 설치가 끝나고 의자에 앉아 쉬고 있었다."
m "나도 책상 옆의 의자에 앉았다."
# 등장 : 주인공 : 왼쪽
m "「내가 관리 감독 한다고 해도 거의 도와주는게 없긴 하네. 얘들아 내가 큰 도움이 못돼서 미안하다.」"
# 등장 : 엑스트라 군중 : 오른쪽
show extras at center with dissolve
$extraname="부원 A"
extra "「에이 괜찮아. 너도 바쁘게 일하는데 뭘. 너도 회장한테 붙잡혀서 하는 거잖아?」"
$extraname="부원 B"
extra "「나도 놀고 싶었는데 하필이면 제비뽑기에서 흑흑, 새벽부터 하다니 이게 나라냐!」"
$extraname="부원 C"
extra "「어차피 나중에 교대하는데 무슨 걱정이야. 그냥 잔말 말고 우리 아침밥이나 사와!」"
$extraname="부원 B"
extra "「이거에도 가위바위보를 지네 인생..」"
m "축제 개방하기에는 잠깐 시간이 남아 휴대폰을 꺼내 문자들을 보았다."
h1 "「축제 오전조는 다 준비 된거 내가 지나가면서 봤으니까 굳이 답장 안해도 돼! 오후조는 교대하는거 잊지 말고! 그러면 애들아! 재밌게 돌자! /ㅇㅂㅇ/」"
$extraname="서기"
extra "「난 왜 오후조인데????」"
$extraname="부원"
extra "「제비뽑기에서 진 사람은, 아무 말도 하지 마라!」"
$extraname="서기"
extra "「[playername]과 교대하면서 총괄 하라고?! 너무 빡센거 아니야?」"
$extraname="부원"
extra "「회장 스타일 알잖아, 그냥 적당히 오전에 즐기고 오라고~」"
# 퇴장 : 엑스트라 군중
m "그렇게 동아리방이 시끌벅적한 문자로 난무한 가운데 후배한테도 문자가 온 걸 보았다."
h2 "「선배! 저 부스에 오후부터 있으니까 그 때 와줘요~ 기다리고 있을게요.」"
m "아무리봐도 전혀 매칭이 안되는데. 사고나는건 아닌지 모르겠네.."

#효과음 재생 : 방송 시작전 차임벨
$extraname="안내방송"
extra "「이제 축제가 시작됩니다. 부스에 있는 학생들은 이제 준비 해 주시길 바랍니다.」"
# 등장 : 엑스트라 군중 : 오른쪽
$extraname="부원 A"
extra "「이제 슬슬 우리도 위치로 돌아가자. 얼른 끝내고 오후에 놀자고!」"
$extraname="부원 B"
extra "「뭐야?! 밥사왔는데 먹을 시간은 줘야지..!!」"
m "그렇게 부원들의 기대와 성난 외침들을 들으며 나도 축제 준비를 하기 시작하였다."
hide extras with dissolve
window hide 
scene bg black with fade 
$renpy.pause(1.5,hard=True)
# 퇴장 : 주인공
# 퇴장 : 엑스트라 군중

scene bg campus_newBuilding_day with dissolve
m "축제가 한창 진행되고 우리는 오전 마지막 한팀을 체험 시키고 난 뒤 부스 입구에 가림막을 하였다."
# 등장 : 엑스트라 군중 : 오른쪽
show extra3 at center with dissolve
show extra2 at right with dissolve
extra "「후, 이제 끝났다. 왜 이렇게 커플들이 많지? 짜증나게..」"
extra "「그럴 수 밖에. 애초에 이 게임들이 2명이서 같이 하는 건데 남자 2명이서 하거나 여자 2명이서 하기엔 장르가 좀…」"
# 등장 : 주인공 : 왼쪽
m "vr이라.."
m "vr에는 평소에도 관심있었다. 인터넷에 여러 스트리머들이 vr게임을 하는걸 보면 무척 실감난다고 한다."
m "진짜로 리얼한지 궁금하단 말이야.."
m "「잠깐 시간 남았으니 우리도 해볼까?」"
$extraname="부원 B"
extra "「단호히 거절 하겠습니다. 우리끼리 하다간 내 멘탈이 남아나지 않을 것 같아. 게다가 이 게임 내용들 보면 더더욱 그러고 싶은 마음이 사라지는걸.」"
$extraname="부원 A"
extra "「그러면 우리중에 주변에 여자가 있는 사람이 있냐?」"
m "「부원들은 그말을 하면서 주변을 둘러보다가 시선이 나한테로 향하였다. 나는 당황하면서 고개를 내저었다.」"
m "「왜 다들 나를 쳐다보는데? 너희들 다 여사친 있잖아?」"
$extraname="부원 B"
extra "「다들 남친들이 있어서 축제때 나랑 같이 이 게임을 하면…. 뒷말은 무슨 말인지 알지?」"
$extraname="부원 A"
extra "「우리 둘은 어차피 여자가 없으니 적임자는 너라고」"
m "「저는 딱히 없는데 무슨 소리를 하시는겁니까..」"
$extraname="부원 B"
extra "「시치미 떼기는 너 요즘 회장하고 또, 여자애 한명이랑 자주 붙어다니잖아」"
m "「하아 그니까 그건..」"
m "그냥 말을 말자.."
m "「이제 곧 점심이고 부르는건 실례인거 같은데"
$extraname="부원 A"
extra "「뭐 어때 불러서 ok 하면 잠깐 같이 하는 거고 아니면 그냥 우리가 겜 한다. 콜?」"
$extraname="부원 B"
extra "「잠깐? 나는 왜 너랑 해야되냐??!」"
m "그래 이건 그냥 vr이 아니다"
play sound "audio/prologue_surprise.mp3"
m "무려 러쿨랴스 리프트!!!" with vpunch
m "대학생이 이런 몇백만원 짜리 언제 써보겠냐!"
m "「그럼, 만약 안나오면 너희 2명이서 하는거다?」"
hide extra3 with dissolve
hide extra2 with dissolve

label  chapter2_3:
m "그러면 이제 누구한테 전화를 해야 하는 거냐인데…. 흠 누구한테 전화해야 하는 거지?"
menu:
   "{color=#066de2}Choice{/color}({color=#63a35c}\"윤미래\"{/color});":
    m "나는 조심스레 선배의 전화번호를 눌렀다. 수화기에서 받는 소리가 나고 선배의 목소리가 들렸다."
    h1 "「이제 곧 점심이니 난 잠깐 숨 좀 돌리고 올께~ 오케이 이따 봐. 오 [playername] 아니야?!」"
    h1 "「무슨 일이야?」"
    m "「선배도 바쁘시네요 그러면 나중에 전화…..」"
    h1 "「아니야 아니야 이제 쉬러 가는 일인걸, 게다가 [playername]이 감독하는 도중에 전화했으니 당연히 받아야지.」"
    m "「선배의 시간 난다는 말을 들은 나는 흘깃 부원들을 보았다. 부원들은 희망이 가득한 눈으로 날 쳐다보고 있었다. 나는 조용히 한숨을 쉬고 말을 이어나갔다.」"
    m "「그게 아니라……」"
    m "나는 지금까지 전화하게 된 경위를 이야기 하게 되었다."
    m "「그래서 만약 힘들다면 애들한테 이야기 해서 안된다고….」"
    h1 "「할래!」"
    m "「네?!」"
    m "나는 선배의 시원스런 대답에 잠깐 멈칫하였다. 원래 선배는 힘들면 나중으로 미루고 보는 성격인데 선배의 목소리에는 기대의 톤이 흘러나왔다."
    m "「나는 순간 어벙벙 해서 말을 못이어나갔다. 」"
    h1 "「한다고! 잠깐 하는건데 무슨 상관이야 게다가 나도 보기만 하고 해본적은 없거든! 게다가 [playername]의 부탁인데 가봐야지!」"
    m "「그럼 지금 오시는 건가요?"
    h1 "「어차피 얼마 안걸려! 금방 갈께!」"
    m "그러고 나서 바로 전화가 끊어졌다."
    show extra3 at center with dissolve
    show extra2 at right with dissolve
    $extraname="부원 A"
    extra "「온대 온대?」"
    m "「오…오신다는데 지금 당장.」"
    $extraname="부원 B"
    extra "「뭐하냐 애들아 회장님이 오신단다! 바로 키고 준비하자!」"
    hide extra3 with dissolve
    hide extra2 with dissolve
    # 퇴장 : 엑스트라 군중
    m "애들은 신나서 분주하게 준비하고 있었다. 선배의 바로 나온 쿨한 대답에 약간 당황하였는 나였지만 선배가 오는걸 발견하자마자 생각이 거기서 끊겼다."
    # 등장 : 선배 츄리닝 기본  : 오른쪽
    show mirae general at center with dissolve
    h1 "「[playername]! 내가 왔어!」"
    m "「급하게 올 필요가 없는데…」"
    h1 "「아니야~ 그런 생각 할 필요 없어~ [playername]과 게임하는거 고등학교 이후로 처음인가?」"
    m "선배가 나를 보면서 활기차게 말하는 소리에 나는 괜한 걱정을 했나는 생각이 들었다."
    m "「아마 그럴거에요. 조원들이 다 준비 했으니 한번 해보죠!」"
    h1 "「알겟어!」"
    m "그렇게 나는  점심시간 전까지 선배와 게임을 하게 되었다."
    window hide
    hide mirae with dissolve
    $renpy.pause(1.0,hard=True)
    # 퇴장 : 주인공
    # 퇴장 : 선배 츄리닝 기본
    # 등장 : 후배 츄리닝 기본 : 가운데
    show harin general at center with dissolve
    $extraname="여학생 A"
    extra "「이번 점심 뭐 먹을까?」"
    $extraname="여학생 B"
    extra "「난 제육 볶음 먹을꺼야!」"
    h2 "「그건 어제도 먹었잖아.」"
    extra "「아잉 그래도 맛있잖아.」"
    $extraname="여학생 A"
    extra "「어 저거 전 학생회장 선배 아니야? 선배가 게임 좋아한다는게 사실이었네.」"
    $extraname="여학생 B"
    extra "「그런데 옆에 하는 사람이 그 너랑 같이 수업 듣던 [playername] 선배 아니야?」"
    $extraname="여학생 A"
    extra "「하린아?」"
    h2 "「아… 아 잠깐 딴 생각 하느라 미안. 응 맞아 같이 수업 듣는 [playername] 선배. 일단 얼른 밥이나 먹으러 가자!」"
    $extraname="여학생 B"
    extra "「그래그래 어서 밥이나 먹으러 가자!」"
    # 퇴장 : 후배 츄리닝 기본


   "{color=#066de2}Choice{/color}({color=#63a35c}\"유하린\"{/color});":
    m "하린이에게 첫 축제를 방해하고 있지 않을까라는 걱정을 하면서 조심스레 전화를 하였다."
    m "통화음이 한동안 이어지고 후배가 전화를 받았다."
    h2 "「[playername] 선배, 미안해요. 아까 화장실 갔다 와서 받기가 그랬어요.」"
    m "「아 그래? 친구랑 놀고 있겠네. 그럼 나중에 전화할…」"
    m "내가 말을 끝마치기 전에 후배가 급하게 말을 끊고 급하게 대답하였다."
    h2 "「괜찮아요! 아직 친구들이 각자 점심 먹기 전에 다른 부스에서 뭐하고 온다고 해서 잠깐 떨어진 거에요! 그…. 아직 시간 있어요! 무슨 일에요 [playername] 선배?」"
    m "「아 그게…."
    m "후배에게 지금까지 전화하게 된 사정을 이야기 하였다."
    m "「그래서 만약 하기 힘들면 거절해도 돼.」"
    h2 "「안그러면 [playername] 선배가 난처해지는 거죠? 그럼 전 갈게요!」"
    m "후배의 시원스런 대답에 나는 약간 멈칫 하였다."
    m "「아니 딱히 그런건 아닌데..」"
    h2 "「아..아니에요! [playername] 선배와 있는게 유학 간 이후로 오랜만이고.. 게다가 게임만 하는 거잖아요? 같이 해요!」"
    m "「아.. 그러면 기다릴께.」"
    m "나는 기대의 눈빛을 보는 그들한테 조심히 대답을 하였다."
    m "「그…내가 아는 후배가 온대…」"
    show extra3 at center with dissolve
    show extra2 at right with dissolve
    $extraname="부원 A"
    extra "「여자인 거지?」"
    $extraname="부원 B"
    extra "「당연한거 아니냐 이 바보야 통화 소리도 못들었어? 당장 준비해!」"
    hide extra3 with dissolve
    hide extra2 with dissolve
    # 퇴장 : 엑스트라 군중
    m "그렇게 친구들은 바쁘게 준비하기 시작하였다." 
    m "후배가 거절할 거라고 생각하였는데 긍정의 대답이 나오니 갑자기 걱정이 들기 시작하였다."
    m "나한테 무슨 할 이야기가 있어서 온다고 하는 것인가? 그런 생각은 후배가 멀리서 보이는 순간 끊겼다."
    # 등장 : 후배 츄리닝 기본 : 오른쪽
    show harin general at center with dissolve
    h2 "「선배! (후우) 저 왔어요.」"
    m "「그렇게 급하게 올 필요 까진 없는데…..」"
    h2 "「선배가 불러서 바로 달려왓죠! 그나저나 게임은 어디 있어요?」"
    m "반짝반짝하는 눈을 보자 괜한 걱정을 했다고 생각하였다."
    m "「이리로 오면 돼. 준비는 다 됬으니 재밋게 즐겨보자.」"
    h2 "「네~!」"
    m "그렇게 나는  하린이와 게임을 하게 되었다."
    window hide
    hide harin with dissolve
    $renpy.pause(1.0,hard=True)
    show mirae general at center with dissolve
    $extraname="학생회 A"
    extra "「수고하셨어요. 선배! 있다가 봬요!」"
    # 등장 : 선배 츄리닝 기본 : 가운데
    h1 "「오케이오케이! 점심먹고 또 도와줄께~!」"
    $extraname="학생회 B"
    extra "「도와주신 보답으로 점심은 제가 쏘게 해주세요! 같이 식당 가요!」"
    $extraname="학생회 A"
    extra "「오 이번에 회장님이 맡으신 부스에도 마지막까지 커플이 게임하네요.」"
    $extraname="학생회 B"
    extra "「이번년도 행사도 성공적이군요. 그렇지 않나요 선배?」"
    h1 "「그…그렇네! 역시 내가 테마를 잘 정했어! 배고프다 빨리 밥 먹으러 가자!」"
# 분기 2_3_1 종료 -------------------


# 배경 전환 :  학교 신축건물앞 낮 -> (none)
# 브금 루프 종료 : 행복