image bg house_players = "images/bg/house_players.jpg"
image bg black = "#000"
image phoneclock = "images/prologue_phone.jpg"
image bg campus_lectureBuilding_day = "images/bg/campus_lectureBuilding_day.jpg"
image bg campus_ally_day = "images/bg/campus_ally_day.jpg"
image bg campus_ally_night = "images/bg/campus_ally_night.jpg"
image bg campus_newBuilding_day= "images/bg/campus_newBuilding_day.jpg"
image bg campus_etcBuilding_aisle="images/bg/campus_etcBuilding_aisle.jpg"
image bg campus_otherClubroom="images/bg/campus_otherClubroom.jpg"
image bg campus_newBuilding_hall="images/bg/campus_newBuilding_hall.jpg"
image bg campus_clubroom ="images/bg/campus_clubroom.jpg"
image bg campus_classroom_1_indoor = "images/bg/campus_classroom_1_indoor.jpg"
image bg campus_classroom_1_outdoor = "images/bg/campus_classroom_1_outdoor.jpg"
image bg campus_backgate_day= "images/bg/campus_backgate_day.jpg"
image bg campus_backgate_night= "images/bg/campus_backgate_night.jpg"
image bg campus_bench_day="images/bg/campus_bench_day.jpg"
image bg campus_bench_night="images/bg/campus_bench_night.jpg"
image bg campus_classroom_2="images/bg/campus_classroom_2.jpg"
image bg campus_newBuilding_day="images/bg/campus_newBuilding_day.jpg"
image bg campus_maingate_day="images/bg/campus_maingate_day.jpg"
image bg restaurant="images/bg/restaurant.jpg"

image bg loading_1 ="images/loadingScreen/ch01.png"
image bg loading_2 ="images/loadingScreen/ch02.png"
image bg loading_3 ="images/loadingScreen/ch03.png"
image bg loading_4 ="images/loadingScreen/ch04.png"

image bg ENDING_BG = "images/credit/ENDING_BG.png"
image bg CREDIT_HAKIN = "images/credit/credit_hakin.png"
image bg CREDIT_SANGHYUN = "images/credit/credit_sanghyun.png"
image bg CREDIT_CHANGEUN = "images/credit/credit_changeun.png"
image bg CREDIT_WONJIN = "images/credit/credit_wonjin.png"
image bg CREDIT_TEAM = "images/credit/credit_team.png"

image senbai ="images/illust/senbai_who.png"

image mirae general ="images/illust/mirae_general.png"
image mirae dark ="images/illust/mirae_sweat_dark.png"
image harin general ="images/illust/harin_general.png"
image harin dark ="images/illust/harin_sweat_dark.png"

image extra1="images/illust/other_black_1.png"
image extra2="images/illust/other_black_2.png"
image extra3="images/illust/player_black.png"
image extras="images/illust/others_black.png"


define harin_count=0
define mirae_count=0

define callignore=False
define playername="나"
define extraname="Player"
#define m = Character("playername",dynamic=True, who_suffix = '@:~$',color="#4B89DC",who_text_align=-17.0)
#define system = Character("system",color="#000000",who_suffix = '@:~$',who_text_align=-17.0)
#define extra = Character("extraname",dynamic=True,color="#000000",who_suffix = '@:~$',who_text_align=-17.0)
#define h1 = Character("윤미래",color="#8D43CA",who_suffix = '@:~$',who_text_align=-17.0)
#define h2 = Character("유하린",color="#3e499d",who_suffix = '@:~$',who_text_align=-17.0)
define m = Character("playername",dynamic=True, color="#E75952")
define system = Character("",color="#000000")
define extra = Character("extraname",dynamic=True,color="#000000")
define h1 = Character("윤미래",color="#8D43CA")
define h2 = Character("유하린",color="#3e499d")
define pauses = Pause(.5)

label start:
    stop music fadeout 1.0
    #jump test_endBranch
    #jump chapter4_1
    #prologue scene start
    $quick_menu = False
    scene bg loading_1 with dissolve
    $renpy.pause(4)
    scene bg house_players with fade
    $quick_menu = True
    $renpy.pause(2.0)
    play sound "audio/alarm_1_beep.mp3"
    #system "띠디디디.. 띠디디디..."
    m "커튼 사이로 줄기줄기 비춰오는 햇빛이 따스하게 마루바닥을 쬐고 있었다."
    m "창문을 열어놓은 탓인지 커튼이 흔들거리며 어서 일어나기를 재촉하였다."
    m "나는 손을 뻗어 요란하게 울려대는 알람을 껐다."
    stop sound
    m "이른 봄의 바람은 아직 겨울을 품고 있는 듯 찬 공기가 내 뺨을 스쳤다."
    m "나는 파묻힌 배개에서 얼굴을 들어 시간을 보았다."
    m "「... 아직 8시 밖에 안됐네?」"
    m "「아침 수업이 9시까지 였던가? 5분만 더자볼까..」"
    m "「딱 5부 5분만 더자는ㄱㅓ....」"
    m "오늘 아침따라 유난히 더 피곤하다 어제 늦게 잔 탓인가.."
    #m "아아, 얼굴이 배개위로 멋대로 움직이고 있다.."
    m "나는 스르륵 이불로 빨려 들어갔다."
    m "zzzzz…"
    scene bg black with fade
    $renpy.pause(2.0)
    play sound "audio/alarm_2_ring.mp3"
    #system "띠리링.. 띠리링..."
    m "눕는것도 잠시, 또 다시 시끄러운 소리가 들려온다."
    m "핸드폰의 비상 알람소리다.... 나는 눈이 떠졌다."
    m "「아 씨.. 시끄러워 죽겠네」"
    m "「벌써 5분이나 지났어??」"
    m "「너무... 피곤해.. 진짜...」"
    m "나는 침대에서 반쯤 일어난 상태로, 휴대폰을 확인했다."
    $renpy.pause(1.0)
    #play sound "audio/prologue_surprise.mp3"
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
    m "「첫 날 부터 지각이라니 교수가 한소리하겠구만..」"
    stop music fadeout 1.0
    play sound "audio/openclose_door.mp3"
    scene bg black with fade
    $renpy.pause(2.0)
    #system ".\/nameset"

screen set_name(title, init_name):
    frame:
        xpadding 50
        ypadding 50
        xalign 0.5
        yalign 0.5
        vbox:
            spacing 20
            text title xalign 0.5
            input default init_name xalign 0.5

label namechk:
    #$playername=renpy.input("내 이름은? :",length=20)

    $ playername = renpy.call_screen("set_name",title="내 이름은?", init_name="나")

    m "[playername], 이게 내 이름이던가?"
    menu:
        "{color=#4d4d4d}Remember{/color}({color=#E75952}\"내 이름이 맞다\"{/color});":
            jump namepass
        "{color=#4d4d4d}Remember{/color}({color=#E75952}\"아니다! 다른 이름이다!\"{/color});":
            $callignore=True
            jump namechk
label namepass:
    m "내 이름은 [playername].\n{w}나이 23세 컴퓨터 공학부 2학년{w} 몇 달 전 군대에서 전역한 복학생이다."
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
    $renpy.pause(3.0)#챕터 넘어가는로딩
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
    play sound "audio/alarm_3_buzz.mp3"
    system "위이이이잉-"
    m "「음? 나한테도 전화란게 오긴 하는구나」"
    m "「역시 모르는 번호네」"
    m "핸드폰 화면에 생소한 전화번호가 떠있었다. 이걸 받아야 하나?"
    menu:
        "{color=#4d4d4d}Act{/color}({color=#E75952}\"그래 전화 걸어준게 어디야. 누군지는 모르지만 일단 받아 보자.\"{/color});":
            jump chapter1_1_1
        "{color=#4d4d4d}Act{/color}({color=#E75952}\"광고전화나 설문조사겠지. 그냥 무시하자.\"{/color});":
            $callignore=True
            jump chapter1_1_2

    label chapter1_1_1:
            stop sound
            stop music fadeout 1.0
            play music "audio/what.mp3"
            #play sound "audio/chap1_phone_answer.mp3"
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
            m "「저기, 죄송하지만 전화 잘못거신 것 같아요..」"
            extra "「[playername]」"
            m "...내 이름을 아네..!?"
            extra "「[playername]씨 휴대폰 아닌가요?」"
            m "「아, 네 제가 [playername]맞습니다만.」"
            extra "「뭐야 그럼, 제대로 건거 맞네~!」"
            extra "「너 진짜로 내목소리 기억안나는구나??」"
            m "「네 그렇습니다만..」"
            #extra "「풉ㅋ」"
            extra "「언어의사랑 동아리방알지?」"
            extra "「내가 누군지 궁금하면 '언어의 사랑' 동방으로 와줄래?」"
            extra "「기다리고 있을테니까, 도망가면 안된다??~」"
            m "「예? 그게 무슨 말...」"
            #play sound "audio/chap1_phone_answer.mp3"
            system "뚝-"
            m "물어보기가 무섭게 그녀의 전화는 의문만을 남기며 끊어졌다..."
            m "이 사람.. 누구였지?"
            m "군대에서 기억상실증이라도 걸린건가."
            m "내 이름이랑 동아리를 아는거보면 나를 아는사람인 것 같은데.."
            m "신종사기는 아니겠지?"
            m "일단 동아리실로 가볼까?"
            window hide
            jump chapter1_1

    label chapter1_1_2:
            stop sound
            m "뭐 전역해도 연락해주는 친구하나 없는데 통화 걸어준건 고맙네"
            m "맞다, 입대하기 전까지 활동하던 ‘언어의사랑'은 어떻게 되었을까?"
            m "동아리실 건물이 어디였더라..?"
            m "나는 동아리실로 향했다."
            window hide
            jump chapter1_1

    label chapter1_1:
            stop music fadeout 1.0
            $renpy.pause(0.4)
            scene bg campus_ally_day with fade
            play music "audio/general_1.mp3"
            m "'언어의 사랑'. 뭔가 촌스러운 이름을 가진 이 동아리는."
            m "내가 이 학교에 입학하고 나서 뜻 맞는 컴퓨터 관련학과 학부생들이 만들었다."
            m "아, 고딩때는 대학교 동아리에 대한 환상이 있었는데 깨진지 오래다."
            m "언어의 사랑은 컴퓨터 학술동아리라는 대외적인 명분을 내세우고 있었지만..."
            m "허구한 날 술이나 퍼마시는 동아리나 다름없었다."
            m "나는 구석에서 쳐박혀서 코딩이나했지만.."
            m "전역하고 나서는 전혀 다른 소문을 듣게 되었는데"
            m "내가 없는 동안 수많은 프로젝트를 진행했고, 대회에 나갔다 하면 상을 휩쓸어가는 전혀 딴판인 동아리가 되어있었다"
            m "게다가 코딩을 전혀 할 줄 모르는 사람도 가르쳐주고 있어서"
            m "학점 잘따려는 애들이나 코딩에 관심있는 사람들이 줄을 서고 있다고 한다."
            m "대체 술이나 마시던 동아리가 어떻게 제대로 돌아가게 된건지 궁금하구만."
            m "나는 가벼운 발걸음으로 동아리실로 향했다."
            window hide
            jump chapter1_2

label chapter1_2:
    # Chapter 1 - section 2 script.
###############################

# 브금 루프 시작 : 기본_1
# 배경그림 전환 : (none) -> 학교 신축건물앞 낮
# 등장 : 주인공 : 왼쪽
#chapter 1 scene start
$renpy.pause(0.4)
scene bg campus_newBuilding_day with fade

m "...."
m "동아리방이 이렇게 큰 건물에 있다고?"
m "원래 낡아빠진 건물 구석에 있어야 할 우리 동아리가 왜 여기에.."
m "들어가보면 어떤 모습일지 상상이 안되네"

#퇴장 : 주인공
m "신축 건물앞에서 한참동안 입을 다물지 못했다"
m "1층 출입문 안쪽을 보니, 큼직한 편의점과 식당이 들어서 있었다."
m "우리 학교 건물이라 하기에는 너무 크다는 느낌을 받았다."
m "낯선 느낌이 드는 출입문을 밀어 안으로 들어갔다"
#전환 : 학교 신축건물앞 낮-> (none)
window hide
stop music fadeout 1.0
scene bg black with fade
system "20분 전"
$renpy.pause(1.5)
#루프 종료 : 기본_1

###############################

#브금 루프 시작 : 기본_2
#배경그림 전환 : (none) -> 학교 기타건물 복도
scene bg campus_etcBuilding_aisle with dissolve
play music "audio/general_2.mp3"
m "동아리방을 오래도록 가보지 못했지만, 어디인지 단번에 알 수 있었다."
#효과음 재생 :knock
play sound "audio/knock.mp3"
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
$renpy.pause(1.5)
scene bg campus_ally_day with dissolve
m "건물 용도나 동아리실 배정이 어느 한 사람이 벌인 일이라니, 대체 무슨 소리야?"
m "소문이 이따금 말이 안되는 이야기이긴 하지만, 너무 뜬구름 잡는 이야기야."
m "시간이 조금 지체되어 마음이 급해졌다. 새로운 동아리실로 발걸음을 재촉했다."
#루프 종료 : 기본_2
stop music fadeout 1.0

############################
window hide
scene bg black with fade
$renpy.pause(2.0)
scene bg campus_newBuilding_hall with dissolve
play music "audio/general_1.mp3"
#브금 루프 시작 : 기본_1
#배경그림 전환 : 학교 골목길 낮  -> 학교 신축건물 홀
m "그렇게 찾아온 건물 안에 들어서자 엘레베이터가 바로 눈에 들어왔다."
#효과음 재생 : 엘레베이터 종
play sound "audio/elevator_bell.mp3"
m "7층의 동아리로 가기위해 홀수층 엘레베이터를 잡았다."
#효과음 재생 : 엘레베이터 문 여닫힘
play sound ["audio/elevator_open.mp3", "audio/elevator_close.mp3"]
m "버튼을 누르고 벽에 기댔다. 너무 오랜만에 동아리에 가는 탓인지 조금 떨렸지만, 이내 설렘으로 뒤덮였다."
window hide
scene bg black with fade
#배경그림 전환 : 학교 신축건물 홀  -> (none)
#재생 : 엘레베이터 종
play sound "audio/elevator_bell.mp3"
#재생 : 엘레베이터 문 열림
play sound "audio/elevator_open.mp3"
#배경그림 전환 : (none)  -> 학교 언어의사랑 동아리방
m "..."
m "…?"
m "여기가 ‘언어의사랑' 이라고?"
$renpy.pause(2.0)
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

#label test2:

hide mirae with dissolve

m "좋아 그럼 풀어볼까?"
$isanswer=0
system "문제1.{w}\nCPU는 무엇의 약자인가?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"Central Park Ubiquitous\"{/color});":
     $isanswer
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"Central Processing Unit\"{/color});":
     $isanswer+=1


system "문제2.{w}\n부동소수점의 의미는?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"움직이는 소수점\"{/color});":
     $isanswer+=1
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"고정된 소수점\"{/color});":
     $isanswer

system "문제3.{w}\nC언어를 만든 사람으로 가장 적절한 답은?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"데니스리치\"{/color});":
     $isanswer+=1
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"비아르네 스트로우스트루프\"{/color});":
     $isanswer
system "문제4.{w}\n데드락은 서로다른 프로세스가 자원을 점유한 상태에서 상호배제 정책에 의해 나타나는 현상이다. 이를 대표적으로 설명하는 모델은?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"테스트 점유 모델\"{/color});":
     $isanswer
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"식사하는 철학자들\"{/color});":
     $isanswer+=1
system "문제5.{w}\nOSI 7 Layer에서 가장 낮은 계층에 존재하는 단은?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"Physical\"{/color});":
     $isanswer+=1
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"Application\"{/color});":
     $isanswer
system "문제6.{w}\nStack 자료구조에서 데이터를 넣는 동작을 이르는 말은?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"Push\"{/color});":
     $isanswer+=1
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"Pop\"{/color});":
     $isanswer
system "문제7.{w}\n정렬된 정수(integer)배열에서 특정 원소를 찾고자 할 때 가장 빠를 것으로 예상되는 알고리즘은?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"넓이우선탐색\"{/color});":
     $isanswer
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"이진탐색\"{/color});":
     $isanswer+=1
system "문제8.{w}\nC언어에서 변수를 생성하고 메모리 주소를 할당하는 행위는?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"선언(Declaration)\"{/color});":
     $isanswer
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"정의(Definition)\"{/color});":
     $isanswer+=1
system "문제9.{w}\n 튜링기계의 구성요소로 맞는 것은?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"누산기\"{/color});":
     $isanswer
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"제어기\"{/color});":
     $isanswer+=1
system "문제10.{w}\n다중프로그래밍에서 '페이징'기법에 맞는 설명은?"
menu:
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"Frame이라는 일종의 섹션으로 메모리를 나누어 관리\"{/color});":
     $isanswer+=1
 "{color=#4d4d4d}Answer{/color}({color=#E75952}\"프로그램을 View와 일치하는 Segment로 나누어 메모리에 탑재\"{/color});":
     $isanswer

m "후~ 끝이네."
h1 "「뭐야 다풀었어? 채점하자!」"

window hide
$renpy.pause(1.5)


show mirae general at center with dissolve
h1 "「점수는.. 10점 만점에...」"
h1 "「10점 만점에 [isanswer]점!」"

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
$renpy.pause(1.5)
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
$renpy.pause(1.5)
m "「여러분이 나중에 커서 어떤 일을 하시게 될지 미래가 분명하지 않습니다. 진로를 정하기 위해서는 다양한 경험이 있어야 하는 법이잖아요. 새로움에 다가설 초석을 저희가 쌓아드릴 수 있을거에요.」"
m "「수습부원으로 오셔서 한 번 체험해보시고 입부를 결정하시는거니까, 부담없이 지원해주시면 되겠습니다.」"
m "「수습으로 활동하고 싶으신 분은 밖에 비치된 지원서를 작성해주세요. OT를 마치겠습니다. 감사합니다!」"
scene bg campus_classroom_1_indoor with dissolve
m "발표가 끝나자 신입생들은 자리에 일어서 나가기 시작했다. 나는 조용히 숨을 돌리며 물을 마셨다. 고개를 돌려보니 아직 남아있는 한 사람이 보였다."
#등장 : 후배_검은색 : 오른쪽
m "「제가 준비한 OT는 끝났고요 혹시 저한테 개인적으로 물어보실 것이라도 있나요?」"
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
m "가끔씩 이메일을 주고 받았지만 어렸을 적의 모습과 많이 달라져 있는 하린이를 보니 새로워진 느낌을 받았다."
m "「못본사이에 많이 변했네? 못알아볼만했다.」"
#전환 : 후배_츄리닝_웃음 -> 후배_츄리닝_기본
m "「그래서 외국 생활은 할만했어?」"
m "하린이는 그동안 외국에서 어떻게 지냈는지,이 학교는 어떻게 들어오게 됐는지 이야기를 풀기 시작했다."
h2 "「그래서 이 학교로 원서를 넣었지. 수시에 재외국민전형이 대학마다 다 있잖아」"
h2 "「그 전형으로 넣었는데 다행히도 서류평가가 좋게 나왔나보더라구.」"
m "「원래 컴퓨터공학과를 오고싶었던거야?」"
h2 "「뭐…그렇지…. 일단 오빠, 난 이거 작성하고 올게..」"
m "「그래 이따가 시간 되면 밥이나 한 번 먹자」"
hide harin with fade
#퇴장 : 후배_츄리닝_기본
m "휴 뒷정리는 이쯤이면 된 것 같다. 몸이 구석구석 쑤신다, 피곤해.. 빨리 쉬러가자"
#루프 종료 : 기본_3
#전환 : 학교 강의실 1 안 -> 학교 강의실 1 문밖
#등장 : 선배_츄리닝_기본 : 오른쪽
stop music fadeout 1.0
scene bg campus_classroom_1_outdoor with dissolve
show mirae general at right with dissolve
h1 "「음 [playername], 저런 귀여운 친구가 있었네~」"
h1 "..."
hide mirae with dissolve

window hide
scene bg black with fade
$renpy.pause(2.0)

label chapter2_1:
$quick_menu = False
scene bg loading_2 with dissolve
show harin general at right with dissolve
$renpy.pause(4)
hide harin with dissolve
scene bg campus_clubroom with fade
$quick_menu = True
play music "audio/general_3.mp3"

m "OT 강의를 마친 이후 선배로부터 기분 좋은 소식이 담긴 문자를 받게 되었다."
h1 "「그거 알아? 신규입부가 작년대비 거의 2배야 2배! 역시 내가 고른 사람은 틀림없다니까 후후~」"
m "하린이도 지원서를 쓰고 수습으로 입부했다. 걱정했던 OT가 잘 해결돼서 다행이다."
m "단지.."
# 등장 : 후배 츄리닝 기본 : 오른쪽
show harin general at center with dissolve
h2 "「선배, 자료구조 수업… 옆자리에서 같이 들으실래요?」"
hide harin with dissolve
# 퇴장 : 후배 츄리닝 기본
# 등장 : 선배 츄리닝 기본 : 오른쪽
show mirae general at center with dissolve
h1 "「[playername]! 내일 고급C 수업에 보자!」"
hide mirae with dissolve
# 퇴장 : 선배 츄리닝 기본

m "따로 맞춘 것도 아닌데, 오전에는 미래 선배와 같은 수업을, 오후에는 하린이와 같은 수업을 듣게 됐다."
m "뭐 이런 우연이 있을수도 있지."
m "「그런데 너희들 눈빛이 왜그러냐 앙?」"

show extras at left with dissolve

$extraname="깝쭉이"
extra "「회장님이랑 같은수업이라고? \n약점이라도 잡은 것 아냐?」"
$extraname="여미새"
extra "「이번에 온 신입생 중에 청순한 여자애 있던데 걔랑 아는 사이야? \n나 좀 소개시켜줘봐.」"
#$extraname="오타쿠"
#extra "「오이오이, [playername]쿤! 이 녀석 복학하니까 아예 하렘만드는 거야?. 거의 라노벨 급이야.」"
# 등장 : 주인공 : 왼쪽
m "「아니라고... 아니라고.. 제발 다 나가줘 혼자있게」"
$extraname="친구들"
extra "넌 우리 연합을 배신했다!"
extra "이 기만자 녀석.."

hide extras with dissolve
# 퇴장 : 엑스트라 군중
m "하아.. 내친구들이지만 어째 정상적인 녀석이 한놈도 없는것같냐.."

window hide
scene bg black with fade
$renpy.pause(1.5)
scene bg campus_lectureBuilding_day with dissolve
# 배경그림 전환 : 학교 언어의사랑 동아리방 -> 학교 강의동앞 낮
# 등장 : 후배 츄리닝 기본 : 오른쪽
h2 "….배 선배!"
m "소리가 나는 방향으로 고개를 돌렸다. 하린이가 나보고 오라고 하는 손짓을 보내고 있었다."
show harin general at center with dissolve
m "「벌써 다음 수업 시작할 시간이야? 빨리 가자.」"
h2 "「그게 아니라… 다음주 축제 때 뭐 할지 [playername] 선배는 정하셨어요?」"
m "하린이는 건물 앞에 있는 게시판을 가리키며 말을 꺼냈다."
m "게시판에는 여러 학과들의 축제 홍보포스터가 붙어있었다. 술을 좋아하는 내가 관심이 가는 건 칵테일 쇼 였다."
m "「이번에 가볼만한건 칵테일 쇼..려나?」"
h2 "「그러면 제가 하는 부스에 구경하러 오신다는 거네요! [playername]선배 오기만을 기대해도 되는거죠?」"
m "하린이는 활짝 웃으며 나를 바라보았다. 얘가 칵테일쇼? 잘 상상이 되지 않았다."
m "「너 올해 스물아니야? 음…. 사고나는게 아닌지부터 봐야될 것 같은데..」"
h2 "「저 조주기능사도 땄어요! [playername] 선배가 술을 좋… 아니 관심 많은걸 아니 여러가지 가르쳐 주려고 준비도 많이했죠!」"
m "「음? 내가 그런걸 말했었나? 내가 술 좋아하는건 어떻게 알았어?」"
h2 "「아….그게….아 프로필 사진에 뒤에 술들이 가득한 것을 봤죠! 누가 봐도 [playername] 선배가 술 좋아하는건 알 수 있을걸요.」"
m "하린이는 약간 내 시선을 피하며 대답했다. 어디까지 사찰을 한건지 더 캐물으려 할 때였다."
$extraname="양진호"
extra "「하린아~ 회의하러가자! 애들 다 모였어!」"
h2 "「알았어 잠깐만! 선배 저 이제 가야 될 것 같아요 축제 때 저희 부스에 꼭 와줘요!」"
m "「그래 그래 너도 어서 가」"
m "그나저나 어느새 나한테 선배 선배 존댓말 쓰네.."
m "뭐 나야 좋지~"
hide harin with dissolve
# 퇴장 : 후배 츄리닝 기본
m "축제가 벌써 일주일로 다가온 가운데 학교 거리를 걷다보니 벌써 부스 장소가 정해졌는지 분주하게 준비하는 학생들이 보였다."
# 등장 : 선배 츄리닝 기본 : 오른쪽
m "건물 입구에서 선배의 모습이 보였다. 주변에 있는 사람들은 학생회 옷을 입고 있었다."
m "새로운 학생회가 처음 여는 대형행사라 모르는게 있었는지, 선배한테 여러가지를 물어보는 듯 했다."
h1 "「여기서는 사람들이 많이 모이기 때문에 집중적인 케어가 필요한 부분이야. 사람 대략 6명 정도 배치해서 안내하면 될꺼야.」"
$extraname="정영주"
extra "「그럼 학생회 인원이 대략 20명이니 2교대로 돌리면 되겠네요. 혹시 나중에 궁금한거 생기면 연락드려도 돼요?」"
h1 "「그럼, 동아리에 있으니 직접 와서 얼굴봐도 되고. 오래걸릴 이야기면 뇌물을 좀 가져오도록」"
$extraname="김혁진"
extra "「히히 알겠어요. 맛있는 뇌물로 가져갈게요. 고마워요 선배!」"
m "학생회 부원들은 서둘러 다른 곳으로 항하였고 선배는 옆에 있는 상자를 들어올리다가 나랑 눈이 마주치게 되었다."
show mirae general at center with dissolve
m "「어, 안녕하세..」"
h1 "「[playername]! 마침 잘 됐다 여기서 상자 들고 기다려봐!」"
m "「네? 저기요 잠만..」"
m "선배는 내 말이 끝나기 전에 학생회 건물에서 다른 상자를 들고 나왔다. 담겨있는건 게임할 때 쓰는 기기들 같은데…."
h1 "「마침 만나서 다행이야! 너 아니었으면 이 누님이 직접 2번 왔다갔다 해야 했어!」"
m "「어째서 제가 상자를 든다는 전제가 깔려 있는 거죠?」"
m "어느 순간 나도 모르게 상자를 들고 선배와 같이 동아리실로 향하고 있었다. 선배는 나의 씁쓸한 표정에 약간 볼을 부풀렸다."
h1 "「뭐야~ 내 일 도와주는게 그렇게 싫은 거야? 게다가 내가 너한테 좋은 걸 알려주려고 하는데.」"

####
# 분기 2_1_1
m "이건 분명히 부탁할 때 쓰는 표현이다. 이걸 어떻게 받아쳐야 하지?"

menu:
 "{color=#4d4d4d}Say{/color}({color=#E75952}\"보통 진짜 좋은 거면 남한테 잘 알려주지 않는데…\"{/color});":
     h1 "「내가 [playername]이니까 막 알려줄려고 하는거지! 힌트는 이 박스야!」"
     m "「이 박스로 무언가 할 예정인가요?」"
     h1 "「짜식 눈치가 늘었는데. 축제때 쓸거야. 부스 관리는 네가 제격이지!」"
 "{color=#4d4d4d}Say{/color}({color=#E75952}\"제가 먼저 대답할께요. 정답은 이 박스에 있는 거죠?\"{/color});":
     h1 "「오 뭐야~ 눈치 야아아악간 부족한 [playername]이 바로 알아채다니!」"
     m "「선배 옆에 있으면 이건 늘수 밖에 없죠. 이걸로 뭐하려구요?」"
     h1 "「응응 이번에 축제때 쓸 물건인데. 네가 관리할 부스에서 쓸거야.」"


m "결국 또 이렇게 걸려드는 구만.."
m "그나저나 이 기기들, 자세히 보니 꽤나 비싸보이는데 이렇게 박스에 대충 넣어 챙겨와도 되는건가."
m "「잠시만요, 이거 비싼거 아니에요? 이렇게 대충 들고 가도 되는 건가요?」"
h1 "「응 이거 VR기기들인데? 비싸긴하지.」"
m "나는 깜짝놀라 박스를 떨어뜨릴 뻔 했다."
m "다이소에 파는 박스 VR고글이 아니라 제대로 된 VR기기였다."
m "「러큘라스 로프트? 이게 대체 몇 개에요.. 대체 돈이 어디서..」"
h1 "「응, 이번 동아리 활동비 다 털어서 산거야. 아 참, 이건 부원들한테 동의 구해서 산거다?」"
m "「이렇게 비싼걸 쓰는 부스면 선배가 관리를 해야죠. 왜 제가 그걸 굳이 해야 되는 건데요?」"
m "그 뒤에 선배가 내 반응을 예상했듯이 대답하였다."
h1 "「이번에는 학생회 일을 도와줘야 할거 같아. SOS가 지금 엄~청 날아 들어오거든.」"
h1 "「이번축제에 언어의사랑에서 VR 체험부스를 위해 만들어 놓은 게임들이 있어.」"
h1 "「이걸로 VR 체험부스를 운영하면 되는거지! 어때 쉽지?」"
m "「그래도 이걸 위해서 예산을 쓰는건 좀….」"
h1 "「끝나고 나서도 동방에서 계속 쓰면 되잖아? VR카페 가서 1시간에 2-3만원 주는 것보단 여기서 마음껏 쓰는게 부원들한테는 좋을꺼야.」"
m "「복학생인 저보다는 다른 사람한테 맡기는게 낫지 않을까요? 전 막 복학한 참이라 내용을 잘 모르겠는데요..」"
h1 "「음 그것도 일리는 있지만...」"
h1 "「별거 아니야 네가 부스 관리만 해주면 돼. 나머지는 개발한 친구들이 설명할테니까.」"
h1 "「부스 전부를 맡으라는게 아니고, 운영을 도맡으면서 다시 동아리에 녹아들라는 이 누나의 마음이지」"
m "그 모습을 본 나는.."
m "「네 알겠습니다.. 관리만 하는 거라면 맡겨 주세요.」"
h1 "「오키! 그러면 다음주에 잘 부탁할게!」"
m "선배는 내가 일을 맡아 준 것에 기쁜 건지 평상시의 둥실한 표정으로 돌아왔다. 그렇게 난 다음주의 축제 준비를 위해 선배와 같이 동아리실로 향했다."
hide mirae with dissolve
window hide
scene bg black with fade
stop music fadeout 1.0
$renpy.pause(2.0)

label chapter2_2:
scene bg campus_clubroom with dissolve
play music "audio/travel.mp3"
# Chapter 2 - section 2 script.
###############################

# 브금 루프 시작 : 여행
# 배경그림 전환 : none -> 학교 언어의사랑 동아리방
m "학교 축제 당일, 축제로 유명한 학교답게 철저히 준비하려는 학생들이 많았다."
m "축제를 즐기려는 외부 학생들도 많이 찾아와 입구에서 줄을 서며 기다리고 있었다."
m "선배는 새벽부터 학생회 일을 도와주고 있었고, 하린이도 분주하게 부스를 준비하느라 바쁜게 눈에 보였다."
m "우리 부스의 준비도 막바지에 이르고 있었다. 나는 동아리 연합회 사람들과 이야기 하면서 필요한 서류를 작성하고 있었다."

m "서류 작업을 마치고 난 뒤 부스로 되돌아 왔다. 부원 3명이 설치를 끝내고 의자에 앉아 쉬고 있었다."
m "나도 책상 옆의 의자에 앉았다."
# 등장 : 주인공 : 왼쪽
m "「내가 운영총괄을 한다고 해도 세부적으로 도와줄 수 있는게 없네. 너희들만 고생하게 하는 것 같아 미안해지네.」"
# 등장 : 엑스트라 군중 : 오른쪽
show extras at center with dissolve
$extraname="이창현"
extra "「에이 괜찮아. 너도 바쁘게 일하는데 뭘. 너도 회장한테 붙잡혀서 하는 거잖아?」"
$extraname="최종규"
extra "「나도 놀고 싶었는데 하필이면 제비뽑기에서 흑흑, 새벽부터 일해서그런지 벌써 피곤해」"
$extraname="이원진"
extra "「어차피 나중에 교대하는데 무슨 엄살이야. 그냥 잔말 말고 우리 아침밥이나 사와!」"
$extraname="최종규"
extra "「인생..」"
hide extras with dissolve
m "축제 시작까지 잠깐 시간이 남아 휴대폰으로 단톡방을 살펴보았다."
m "미래 선배가 띄워둔 공지가 먼저 보였다"
h1 "「축제 오전조는 다 준비 된거 지나가면서 봤어. 다들 고생많았어! 오후조는 교대하는거 잊지 말고! 그럼 애들아 재밌게 놀아!」"
m "뒤이어 올라와있는 메시지들을 읽었다"
$extraname="김방방"
extra "「난 왜 오후조야? 오후에 친구들이랑 칵테일 부스 가려고했는데」"
$extraname="금용각"
extra "「제비뽑기에서 진 사람은, 아무 말도 하지 마라!」"
$extraname="이므왕"
extra "「[playername]랑 교대하면서 운영을 보라고?! 우리 둘만? 너무 빡센거 아니야?」"
$extraname="이창현"
extra "「회장 스타일 알잖아, 그냥 적당히 오전에 즐기고 오라고~」"
# 퇴장 : 엑스트라 군중
m "동아리 단톡방에 메시지가 올라오는 가운데, 방송이 나오기 시작했다"

#효과음 재생 : 방송 시작전 차임벨
play sound "audio/chime_bell.mp3"
$extraname="안내방송"
extra "「이제 축제가 시작됩니다. 부스에 있는 학생들은 준비를 마무리 해주시기 바랍니다.」"
# 등장 : 엑스트라 군중 : 오른쪽
show extras at center with dissolve
$extraname="손준규"
extra "「이제 슬슬 우리도 위치로 돌아가자. 얼른 끝내고 오후에 놀자고!」"
$extraname="장선우"
extra "「뭐야?! 밥이 방금왔는데 먹을 시간은 줘야지..!!」"
m "나도 분주히 부스 오픈 준비를 하기 시작했다."
hide extras with dissolve
window hide
scene bg black with fade
$renpy.pause(1.5)
# 퇴장 : 주인공
# 퇴장 : 엑스트라 군중

scene bg campus_newBuilding_day with dissolve
m "바쁜 시간을 지나 오전 마지막 팀을 내보냈다. 잠시 쉬기 위해 부스 입구에 가림막을 쳤다."
# 등장 : 엑스트라 군중 : 오른쪽
show extra3 at center with dissolve
show extra2 at right with dissolve
$extraname="손준규"
extra "「후, 이제 끝났다. 왜 이렇게 커플들이 많지? 짜증나게..」"
$extraname="장선우"
extra "「그럴 수 밖에. 애초에 커플들 꽁냥꽁냥대라고 만든 게임이잖아. 시커먼 남정네 둘이서 하면 이상하잖아.」"


m "「VR이라..」"
m "VR에는 평소에도 관심있었다. 뚜위치에서 스트리머들이 VR게임을 하는걸 보면 무척 재미있어 보였다."
m "진짜로 리얼한지 궁금하단 말이야.."
m "「잠깐 시간 남았으니 우리도 해볼까?」"
$extraname="장선우"
extra "「미친놈아 이 내용을 보고도 남정네끼리 하고싶다고? 어휴..」"
$extraname="손준규"
extra "「우리중에 여사친이랑 썸타는사람없어?」"
m "부원들은 그말을 하면서 주변을 둘러보았다. 순간 나에게 시선이 모였다. 나는 당황하면서 고개를 내저었다."
m "「왜 나를 쳐다보는데? 너희들 다 여사친 있잖아?」"
$extraname="손준규"
extra "「다들 남친들이 있어서 축제때 나랑 같이 이 게임을 하면…. 뒷말은 무슨 말인지 알지?」"
$extraname="장선우"
extra "「우리 둘은 어차피 썸녀도 없으니 적임자는 너라고」"
m "「아니 나는 있어? 왜 나한테그래」"
$extraname="장선우"
extra "「시치미 떼기는. 너 요즘 회장하고 또, 여자애 한명이랑 자주 붙어다니잖아」"
m "「아.. 아니라고 그랬잖아..」"
m "「그냥 말을 말자..」"
m "「이제 곧 점심시간이고 해서 부르긴 뭐한데」"
$extraname="손준규"
extra "「일단 불러나 봐. 오기 싫으면 싫다고 하겠지. 니가 못부르면 우리 둘이 게임하는거 보여줄게」"
$extraname="장선우"
extra "「잠깐? 내가 왜 너랑 저걸해?」"

m "그래 이 비싼 러쿨랴스 리프트!!!" with vpunch
m "내가 이런 좋은 장비를 언제 써보겠냐!"
m "「그럼, 만약 아무도 안온다고 하면 너희 둘이서 하는거다?」"
hide extra3 with dissolve
hide extra2 with dissolve

label chapter2_3:
m "그러면 이제 누구에게 전화를 해볼까.."
menu:
   "{color=#4d4d4d}Choice{/color}({color=#E75952}\"윤미래\"{/color});":
    m "나는 조심스레 선배의 전화번호를 눌렀다. 수화기에서 받는 소리가 나고 선배의 목소리가 들렸다."
    h1 "「 (... 그럼 이제 곧 점심이니 난 잠깐 숨 좀 돌리고 올게~ 오케이 이따 봐. ...) 오 [playername] 아니야?!」"
    h1 "「무슨 일이야?」"
    m "「선배도 바쁘시네요 그러면 나중에 전화…..」"
    h1 "「아니야 아니야 이제 쉬러 가려고. 부스를 맡고계신 [playername]씨가 전화했으니 당연히 받아야지.」"
    m "선배의 쉬러 간다는 말을 들은 나는 부원들을 쳐다봤다. 부원들은 희망이 가득한 눈으로 날 쳐다보고 있었다."
    m "나는 조용히 한숨을 쉬고 말을 이어나갔다."
    m "「그게 아니라……」"
    m "전화하게 된 이유를 잘 요약해 말했다."
    m "「그래서 만약 힘들다면 애들한테 이야기 해서 안된다고 말할게요.」"
    h1 "「할래!」"
    m "「네?!」"
    m "나는 선배의 시원스런 대답에 잠깐 멈칫하였다. 왜 이렇게 적극적이지 이사람?"
    h1 "「한다고! 잠깐 하는건데 무슨 상관이야 게다가 나도 보기만 하고 해본적은 없거든! 게다가 [playername]의 부탁인데 가봐야지!」"
    m "?? 뭐지??"
    m "「언제쯤 오실 수 있으세요?」"
    h1 "「여기서 얼마 안걸려! 금방 갈게!」"
    m "그러고 나서 바로 전화가 끊어졌다."
    show extra1 at center with dissolve
    show extra2 at right with dissolve
    $extraname="장선우"
    extra "「뭐래? 뭐래?」"
    m "「오…오신다는데 지금 당장.」"
    $extraname="손준규"
    extra "「뭐하냐 애들아 회장님이 오신단다! 바로 세팅해드려라!」"
    hide extra1 with dissolve
    hide extra2 with dissolve
    # 퇴장 : 엑스트라 군중
    m "애들은 신나서 분주하게 준비하고 있었다. 뒤를 돌아보니 선배가 빠른걸음으로 걸어오고있었다."
    # 등장 : 선배 츄리닝 기본  : 오른쪽
    show mirae general at center with dissolve
    h1 "「[playername]! 내가 왔어!」"
    m "「급하게 올 필요가 없는데…」"
    h1 "「아니야~ 그런 생각 할 필요 없어~ [playername]. 자 그럼 실제 빌드된 프로젝트가 잘 돌아가나 볼까?」"
    m "선배가 나를 보면서 활기차게 말하는 소리에 나는 괜한 걱정을 했나 하는 생각이 들었다."
    m "「오늘 새로 발견된 버그는 없어요. 조원들이 다 준비 했으니 한번 해보죠!」"
    h1 "「좋아!」"
    m "그렇게 나는  점심시간 전까지 선배와 게임을 하게 되었다."
    window hide
    hide mirae with dissolve
    $renpy.pause(1.0)
    # 퇴장 : 주인공
    # 퇴장 : 선배 츄리닝 기본
    # 등장 : 후배 츄리닝 기본 : 가운데
    show harin general at center with dissolve
    $extraname="김점례"
    extra "「이번 점심 뭐 먹을까?」"
    $extraname="박옥춘"
    extra "「난 제육 볶음 먹을꺼야!」"
    h2 "「그건 어제도 먹었잖아?」"
    extra "「아~~ 그래도 맛있잖아.」"
    $extraname="김점례"
    extra "「어 저거 전 학생회장 선배 아니야? 선배가 게임 좋아한다는게 사실이었네.」"
    $extraname="박옥춘"
    extra "「그런데 옆에 하는 사람이 그 너랑 같이 수업 듣던 [playername] 선배 아니야?」"
    $extraname="김점례"
    extra "「하린아?」"
    h2 "「아… 아 잠깐 딴 생각 하느라 미안. 응 맞아 같이 수업 듣는 [playername] 선배. 일단 얼른 밥이나 먹으러 가자!」"
    $extraname="박옥춘"
    extra "「그래그래 어서 밥이나 먹으러 가자!」"
    # 퇴장 : 후배 츄리닝 기본


   "{color=#4d4d4d}Choice{/color}({color=#E75952}\"유하린\"{/color});":
    m "하린이에게 방해가 되는건 아닌지 걱정 하면서 조심스레 전화를 걸었다."
    m "통화음이 한 동안 이어졌다"
    h2 "「[playername] 선배, 무슨일이에요?」"
    m "「부탁할게 있었는데, 많이 바쁜가보네. 나중에 전화..」"
    m "내가 말을 끝마치기 전에 하린이가 급하게 대답했다."
    h2 "「괜찮아요! 지금 시간 있어요! 무슨 일이에요 [playername] 선배?」"
    m "「아 그게….」"
    m "하린이에게 전화하게 된 사정을 이야기했다."
    m "「그래서 만약 여유가 안되면 그렇게 알고있을게」"
    h2 "「[playername] 선배가 부르는데 어떻게 안가요? 지금 가면 돼요?」"
    m "후배의 시원스런 대답에 나는 약간 멈칫 하였다."
    m "「진짜 괜찮은거 맞아? 거기도 바쁠텐데」"
    h2 "「아니에요! 오래걸리지도 않을텐데. 같이해요!」"
    m "「아.. 그러면 기다릴게.」"
    m "전화를 끊고 뒤를 돌아보니, 부원들이 나를 쳐다보고 있었다"
    m "「... 온다는데?」"
    show extra3 at center with dissolve
    show extra2 at right with dissolve
    $extraname="장선우"
    extra "「여자야?」"
    $extraname="손준규"
    extra "「당연한거 아니냐 이 바보야 통화 소리도 못들었어? 당장 준비해!」"
    hide extra3 with dissolve
    hide extra2 with dissolve
    # 퇴장 : 엑스트라 군중
    m "예정에 없던 게임을 바쁘게 준비하기 시작하였다."
    m "뒤를 돌아보니 서투르게 걸어오는 하린이가 보였다"
    # 등장 : 후배 츄리닝 기본 : 오른쪽
    show harin general at center with dissolve
    h2 "「선배! 저 왔어요!」"
    m "숨을 고르는걸 보니 뛰어온게 분명했다."
    m "「그렇게 급하게 올 필요까지는 없었는데…..」"
    h2 "「선배가 불러서 바로 달려왔죠! 게임은 어디 있어요?」"
    m "반짝거리는 눈동자를 보자 괜한 걱정을 했다는 생각이 들었다."
    m "「이리로 오면 돼. 준비는 미리 다 해놨으니 한 번 해보자구」"
    h2 "「네~!」"
    m "하린이와 한 의자에 앉아 게임시작 버튼을 눌렀다."
    window hide
    hide harin with dissolve
    $renpy.pause(1.0)
    show mirae general at center with dissolve
    $extraname="김쏭쏭"
    extra "「수고하셨어요. 선배! 있다가 봬요!」"
    # 등장 : 선배 츄리닝 기본 : 가운데
    h1 "「오케이오케이! 점심 먹고나서 또 도움필요하면 불러」"
    $extraname="이핑핑"
    extra "「도와주신 보답으로 점심은 제가 쏘게 해주세요! 같이 학식 가요!」"
    $extraname="김쏭쏭"
    extra "「선배 저기 보이는거 언어의 사랑 부스맞죠? 커플들 꽁냥대면서 게임하는거 보니까 화가나려고해요」"
    $extraname="이핑핑"
    extra "「이 좋은날씨에 어그로를 잘 끄는 주제네요. 으... 배가아파...」"
    h1 "「.. 배고프다 빨리 밥 먹으러 가자!」"
    window hide
    scene bg black with fade
    $renpy.pause(2.0)
label chapter3_1:
$quick_menu = False
scene bg loading_3 with dissolve
show mirae general at right with dissolve
$renpy.pause(4)
hide mirae with dissolve
scene bg campus_ally_day with fade
$quick_menu = True
play music "audio/general_1.mp3"
# Chapter 4 - section 1 script.
###############################

# 배경 전환 : (none) -> campus_ally_day
# 브금 루프 시작 : 여행(travel)

m "여름방학이 물 흐르듯 빠르게 지나가고 벌써 2학기가 시작되었다."
m "방학때와는 다르게 사람으로 들어찬 캠퍼스가 어색했다"
m "그동안 미래 선배와 하린이가 놀러가자는 유혹의 손길을 내뻗었지만.."
m "군대도 다녀왔겠다, 이제 시간을 헛으로 쓸 수 없었다.\n둘이서 날 흔들어 놓을때면 공부를 하겠다며 모두 거절했다"
m "첫 날 수업이 끝나고, 방학에 있었던 일을 친구들과 이야기 하며 걷고 있었다."

# 등장 : 엑스트라 군중(others_black) : 가운데
show extras at center with dissolve

$extraname="이명현"
extra "「제정신이냐?, [playername]?」"
m "「아니 또 왜?」"
$extraname="이명현"
extra "「돌았구만... 연애도 못하고 졸업하려고 그러는거야?」"
$extraname="이원진"
extra "「그래 [playername], 니 말도 맞지. 취업도 중요하지.」"
m "「그래그래. 너만큼은 내 마음을 이해하는구나!」"
extra "「근데 이건 아니지..」"
m "「...」"
extra "「여자가 어디 같이 가자는 말을 아무한테나 하는 줄 알아?」"
extra "「정말 친한 사이라서 그럴 수도 있는데, 그게 일반적인지 똑바로 생각해보라고.」"
$extraname="이명현"
extra "「얘 군대갔다오더니 순 고자가 다 돼서 왔는데? 에휴 답답한놈」"
m "「제 걱정 해주셔서 정~말 감사합니다. 난 집이나 간다」"

hide extras with dissolve
# 퇴장 : 엑스트��� 군중(others_black)

scene bg campus_backgate_day with dissolve
# 배경 전환 : campus_ally_day -> campus_backgate_day
m "고백이라. 그 단어는 여자친구가 한 번도 없었던 나에게 생소한 말이였다. 문득 미래선배, 하린과의 관계가 어색하게 느껴졌다."
m "자연스레 받아들이던 일상이 머릿속에서 어그러져 이해할 수 없는 형상이 되어버렸다."
m "조언을 얻기 위해 나는 전화기를 들어 자주 연락하던 전화번호로 전화를 걸었다."
$extraname="???"
extra "「웬일? 네가 전화를 다하고?」"
m "「시간 있냐?」"
extra "「냐야 뭐 언제든 괜찮지. 이 바쁘실 시간에 전화를 다 하네. 또 무슨일이야?」"
m "「……내 마음을 잘 읽는 다니까 너는…」"
extra "「어디서 볼까?」"
stop music fadeout 1.0
window hide
scene bg black with fade
$renpy.pause(2.0)

label chapter3_2:
# chapter 4 - section 2
scene bg campus_bench_night with dissolve
# 배경 전환 : (none) -> campus_bench_night
# 브금 루프 시작 : 슬픔(sad)
play music "audio/sad.mp3"

m "심란하거나 고민이 많을 때 오는 이 벤치…. 벌써 여름이 지나가고 가을이 왔는지, 바닥에 낙엽이 가득했다.."
m "이 경치를 보면 내 마음과 같은 풍경이라 가만히 쳐다보게 된다.」"
m "그런 순간을 느끼면서 멍하니 있으면 어느순간 해결책이 생기기도 하지만….."
m "지금은 어떤 해결책도 떠오르지 않는다."

show extra3 at center with dissolve
extra "「무슨 생각을 그렇게 하고있어?」"
m "이 친구는 남민재. 우연히 초등학교 농구부에서 만나 지금까지 쭉 알고 지낸 소꿉친구이다."
m "사교성도 좋고 경험한 일도 다양해서, 내가 고민이 있을 때 명쾌한 대답을 내놓아주는 길잡이 역할을 해주고 있다"
m "「어… 민재 왔네…」"
$extraname="남민재"
extra "「대체 뭐때문에 그래? 안그래도 심각한 얼굴이 더 험악해보여」"
m "「음… 그게 말이지…」"
m "그동안 미래 선배, 그리고 하린이와 있었던 일들을 이야기 하였다."
extra "「넌 …. 진짜 …. Wls이다…..」"
m "「아니 왜?」"
extra "「[playername], 네가 모솔찐따인건 나도 잘 알겠는데, 이건 너무 심하네.」"
m "「알기 쉽게 이야기좀 해봐」"
m "민재는 음료수를 한 모금 마시더니 설명하기 시작하였다."
extra "「.. 그래서 결국 네 인간관계를 그대로 모두 끌고가긴 어려운 상황을 만나게 될거야」"
extra "「어떤식으로 주변 관계를 정리할지 결정을 해야할거고.」"
extra "「잘 고민해봐. 상황을 애매하게 만들지 말고 잘 정리해야지」"
m "나는 아무말도 못하고 나무 너머의 건물만 바라봤다. 나는 머리가 복잡해져 갔다."
#퇴장 : player_black
m "이야기 들어줘서 고맙다고 이야기하고 난 뒤 일어섰다"

scene bg campus_ally_night with fade
#배경 전환 : campus_bench_night -> campus_ally_night

m "아무 생각없이 길을 걸었다."

stop music fadeout 1.0
window hide
scene bg black with fade
$renpy.pause(2.0)

label chapter4_1:
$quick_menu = False
scene bg loading_4 with dissolve
show harin general at center with dissolve:
    xzoom -1
show mirae general at right with dissolve:
    xzoom -1
$renpy.pause(4)
hide mirae with dissolve
hide harin with dissolve
scene bg campus_classroom_2 with fade
$quick_menu = True
play music "audio/general_1.mp3"
# chapter 5 - section 1

# 배경 전환 : (none) -> campus_classroom_2
# 브금 루프 시작 : 일반_1(general_1)

m "별 특별한 일 없이 2학기가 지나가고있었다."
m "우연히 시간표가 겹친건지, 오전에는 미래 선배와, 오후에는 하린이와 같이 수업을 듣고 있다."
m "뭔가.. 이상한데.. 이렇게 겹칠 수가 있는건가?"
m "중간고사가 끝난지 얼마 되지 않아, 수업 내내 어수선했다. 수업도 비교적 일찍 끝났다."
m "오늘은 유난히 피곤하다. 집에 가서 쉬기 위해 빠르게 가방을 챙겼다."
h1 "「[playername]…[playername]!」"
m "뒤에서 콕콕 찌르는 느낌이 나더니 선배가 나를 불렀다."

show mirae general at center with dissolve
#등장 : 선배(mirae_sweat_general) : 가운데
m "「선배, 무슨 일이에요?」"
h1 "「별건 아니고…..」"
m "강의실에서 학생들이 빠져나가는 것을 본 미래 선배는 뜸을 들였다."
h1 "「잠시만 여기에서 기다려 줄래?」"
m "나는 영문도 모르고 가만히 앉아있었다. 선배가 주위 눈치를 보고 있었다."
m "마지막 학생이 나가자 미래선배는 내 옆자리에 와서 앉았다"
m "가방에서 무언가 주섬주섬 챙기더니, 나한테 종이 한 장을 건네주었다."
h1 "「자 [playername].」"
m "「어라 이게 뭔데요? 이거, 불꽃 축제 티켓?"
m "선배가 건네준 것은 불꽃축제 티켓이었다. 욘세이 대학교-혼긱대학교에 걸쳐 진행되는 큰 스케일을 자랑한다."
m "연예인의 라인업이 굉장해서 예매사이트 접속조차 힘든 표였다."
m "「이 티켓, 한정판 아니에요? 게다가 이거 요즘 핫한 가수 'Hackin Kim'도 오는 축제잖아요? 추첨 경쟁도 되게 빡셌는데.」"
h1 "「역시 [playername], 잘 알고있을 줄 알았어. 어때, 같이 갈래?」"
m "나는 잠깐 고민하다 대답했다."
m "「휴일에 스케쥴이 어떻게 될지 잘 모르겠어요. 일단 확인하고 내일 말씀 드릴께요.」"
m "나의 대답에 미래 선배는 만족스럽지 못한 표정을 지었지만, 이내 웃으며 대답하였다."
h1 "「그러면 내일 꼭 알려주는거다~?」"
m "「네네 알겠어요. 내일 봬요 선배.」"
#퇴장 : 선배(mirae_sweat_general)
hide mirae with dissolve
m "나는 대답을 미루고 강의실을 나왔다."

scene bg campus_newBuilding_day with dissolve
show extras at center with dissolve
# 배경 전환 : campus_classroom_2 -> campus_newBuilding_day
#등장 : 엑스트라 군중(others_black) : 가운데
$extraname="공선우"
extra "「뭐냐 뭐냐, 미래 선배가 뭐라 했어?」"
m "「아니 별거 아니고 축제 구경 가자고.」"
$extraname="공선우"
extra "「축제라면 요즘 엄청 광고때리는 불꽃축제? 키야, 그래서! 간다고 한거야?」"
m "「아니, 아직 휴일날 무슨일이 생길지 모르잖아. 내일 이야기 한다고 했어.」"
$extraname="이준기"
extra "「아니 미친놈아 바로 간다고해야지 뭐하냐? 너 미래 선배가 남들한텐 얼마나 철벽인줄 알어?」"
$extraname="공선우"
extra "「맞아 맞아, 그동안 남자 한 트럭이 와서 미래 선배한테 고백했는데, 예외 하나없이 냉정하게 다 내쳤단 말이야」"
extra "「거의 뭐 무조건반사라고 할수있지」"
$extraname="김윤철"
extra "「그중에서 끈질기게 달라붙었던 사람에게 했던 말이 \n'너같은건 내 스타일 아니니까 제발 꺼져줄래?' 였다니까!」"
m "「저는 남의 연애사는 아무런 관심이 없답니다~\n너희들도 한번 대쉬해 보든지」"
m "「난 잘 모르겠고 집이나 갑니다」"
$extraname="이준기"
extra "「어휴.. 말을 말아야지」"
#퇴장 : 엑스트라 군중(others_black)
hide extras with dissolve


scene bg campus_maingate_day with dissolve
# 배경 전환 : campus_newBuilding_day -> campus_maingate_day
m "친구들의 야유를 뒤로 한 채로 학교 정문을 나섰다. 그리고 선배와 있었던 일들을 되돌아 보았다."
m "그러고 보니 미래 선배가 남자들과 이야기 한 것을 본 적이 없었다."
m "친구들이 이야기 하는 것을 되짚어 보기 시작하자 선배의 행동이 다르게 느껴졌다."
m "오늘 미래 선배가 이야기 하면서 얼굴을 붉힌 것이 이해가 되기 시작하였다. 선배는 용기를 내서 고백한 것이나 다름없는게 아닌가?"
m "여러 상황들이 맞아 떨어지자 나는 선배를 어떤 마음으로 만나야 할지 걱정이 되었다."
m "생소한 생각을 하며 버스를 기다리는데, 갑자기 검은 양복을 입은 사람들이 내 주변을 둘러쌌다."
show extras at center with dissolve
#등장 : 엑스트라 군중(others_black) : 오른쪽
$extraname="검은 양복"
extra "「저기 혹시 [playername] 맞으신가요?」"
m "한 명이 내 이름을 물어오자, 두려움에 순간 휩싸였다. 잠시만, 내 이름은 어떻게 아는 거지?"
m "「네….마…맞는데요?」"
stop music fadeout 1.0

# 브금 루프 종료 : 일반_1(general_1)
# 브금 루프 시작 : 긴급(emergency)
play music "audio/emergency.mp3"
extra "「잠깐 저희와 같이 가주셔야 겠습니다.」"
m "「저 잘못한게 없는…데요? 제가 잘못한게 있으면 바로 고칠게요! 아..아니 이렇게 바로 사과드릴게요!」"
extra "「그런게 아닙니다. 저희만 따라오시면 아무일도 없을 것입니다.」"
m "위협적인 사람들이 내 주변을 더욱이 견고하게 에워싸면서 위압적인 말을 뱉어냈다"
m "그냥 집에 가고싶었는데, 이게 대체 뭐야!!!"
$extraname="???"
extra "「아니 너희들 뭐해!~!!!!!!」"
m "상황을 찢는듯한 높은 목소리에 남자들은 움찔 거렸다. 그리고 소리가 나는 방향을 일제히 바라보았다."
extra "「[playername] 선배를 데려오랬더니, 왜 납치를 하고있어?」"
$extraname="검은 양복"
extra "「아가씨 그게….」"
m "저 우락부락한 경호원들이 아무 말도 하지 못했다."
m "드라마에서나 보았던 부잣집 아가씨 포스가 풍겼다. 근데 아가씨가 어디에서 많이 본거 같은데?"

show harin general at left with dissolve
stop music fadeout 1.0
#등장 : 후배(harin_sweat_general) : 왼쪽
# 브금 루프 종료 : 긴급(emergency)
play music "audio/what.mp3"

# 브금 루프 시작 : 어리둥절(what)
m "「하린아?」"
h2 "「선배 미안해요! 좋은 곳에 같이 가서 밥이나 먹고 싶었는데..」"
h2 "「이런 상황을 의도한건 아니에요 [playername] 선배.. 진짜 미안해요!」"
m "하린은 연신 미안하다고 이야기를 한뒤, 주변의 양복입은 사람들을 둘러보며 얼굴을 찡그렸다."
m "다들 하린이의 눈을 애써 피하고 있었다."
#퇴장 : 엑스트라 군중(others_black)
hide extras with dissolve

m "나는 정신을 가다듬고 괜찮다고 대답을 하였다. 하린이는 마음이 편치 않아 보였다."
h2 "「선배 정말 당황스럽겠지만, 식사자리를 열심히 준비했어요. 한 번만 같이 가줘요. 하고싶은 말도 있구요.」"
m "나는 정신차를 겨를 없이 하린이에게 끌려갔다"
hide harin with dissolve
m "하린이는 옆에 있던 큰 스포츠카에 나를 욱여넣듯이 태웠다.. 그리고는 운전석에 앉아 출발했다."
m "「아니 하린아, 네가 운전한다고? 잠시만..잠시만...」"
h2 "「그럼요. 저 운전잘해요」"
m "「잠시만 이거 너무 빠른거아니야? 하린아!!!」"
m "무서운 속도로 달리는 차에서 안전벨트만을 꼭 붙잡았다. 살아서 내리고 싶었다."


stop music fadeout 1.0
#퇴장 : 후배(harin_sweat_general)
# 브금 루프 종료 : 어리둥절(what)
# 배경 전환 : campus_maingate_day -> (none)
window hide
scene bg black with fade
$renpy.pause(2.0)

label chapter4_2:
play music "audio/happy.mp3"
scene bg restaurant
# Chapter 5 - section 2
# + 에필로그

# 배경 전환 : (none) -> restaurant
# ********************** 레스토랑 배경 새로 만들겠습니다 그냥... 깃허브 / 디코에 720p 사진 올릴 예정입니다.
# 브금 루프 시작 : 행복(happy)


m "하린이가 데리고 온 레스토랑은 낯선 공간이었다."
m "와인셀러를 가득 채운 값비싼 와인, 그냥 보아도 귀해보이는 장식품들.."
m "메뉴판을 보니.. 0이 4개.. 5개.. 6개.. ?"
m "하린이는 내 반응을 읽었는지 메뉴판을 가로채 주문했다."

show harin general at center with dissolve
# 등장 : 후배(harin_sweat_general) : 가운데
h2 "「선배것도 저랑 같은 코스로 했어요. 괜찮죠?」"
m "「아니 그게, 가격이,」"
h2 "「누가 [playername] 선배 아니랄까봐! 신경 쓰지 마요!!」"
h2 "「나오기만을 기다리면 되니까 편하게 있어요.」"
m "하린이는 얼굴을 붉히며 나의 말을 끊었다."
m "익숙치 못한 환경에 나는 고분히 하린이의 말에 따르게 됐다."
m "그러고 보니 하린이가 나한테 할 말이 있다고 했지?"
m "「하린아 그러고 보니…」"
h2 "「잠시만요 선배. 와인은 이걸로 주시고….」"
m "하린이는 내말을 잠깐 멈추게 한 뒤 와인을 시켰다.\n얼마 안되어 직원이 와서 와인을 따랐다."
m "잔을 다 따르자 마자 하린이는 잔을 들어 와인을 원샷 했다."
m "「하린아? 너 차 몰고 왔잖아. 술 마셔도 돼?」"
h2 "「걱정마요. 기사님께 부탁해서 집에 가져가달라 하면 되죠.」"
h2 "「그리고 술이 들어가지 않으면 선배 앞에서 제대로 말을 못할거 같아요.」"
m "???"
m "하린이는 입가를 닦고나서 나를 바라보았다."
m "벌써 술기운이 올라오기 시작하는지 하린이의 얼굴이 달아오르는게 보였다"
m "갑자기 무언가 생각 났는지 가방을 뒤적였다."
m "하린은 은은한 펄이 돌도록 코팅된 종이를 내게 건넸다"
h2 "「자요.」"
m "이번에 새로 개장한 테마 파크 티켓이였다."
m "「이건 어떻게 구한거야??? 그리고 이 티켓은…」"
h2 "「이번에 선배와 같이 가고 싶어서 그래요. 혹시 이번주 토요일에 바빠요?」"
m "「일단 일정이 있는지 봐야 할 것 같은데….」"
h2 "「그러면 내일 아침에는 이야기 해줘요. 꼭!」"
m "하린이가 상기된 표정으로 나의 손을 잡고 말하니 나는 차마 거절을 할 수 없었다."
m "「일단… 손좀 놓고…」"
stop music fadeout 1.0
h2 "「...」"
h2 "「... ...」"
m "순간 하린의 낯빛이 어두워졌다"

hide harin general
show harin dark
with dissolve
$renpy.pause(2.0)
h2 "「왜 대답을 못해주는거에요?」"
m "「응?」"
m "갑작스레 얼어붙은 분위기에, 내 머리도 굳어가기 시작했다"
h2 "「미래 선배한테도 이렇게 대답했어요?」"
m "..."
h2 "「제 마음을 알고도 이러는거에요?\n아니면 정말로 아무것도 모르는거에요?」"
h2 "「...」"
h2 "「그것도 아니면 이미 마음을 굳혀놓고도\n저에게 확답을 주길 망설이고 있는거에요?」"
h2 "「그렇게 [playername]선배가 어중간하게 마음을 내비치면, 저는요?」"
h2 "「저는 어떡하면 좋은거에요?」"
m "그 순간 직원이 음식이 담긴 접시를 들고왔다"
$extraname = "직원"
extra "식사 준비해드리겠습니다."
m "나와 하린의 앞에 각각 접시를 놓아두면서, 우리의 얼굴을 살폈다"
extra "..."
extra "맛있게 드세요. 필요하신 것 있으시면 바로 불러주세요."
m "「네 감사합니다」"
m "직원이 심상찮은 분위기를 읽어낸듯, 음식에 대한 아무런 설명없이 주방 앞으로 돌아갔다"

m "음식이 나오자 하린은 잠시 가만히 있더니 나지막이 말했다."
hide harin dark
show harin general
with dissolve
$renpy.pause(2.0)

h2 "「미안해요 선배, 어떤 기분으로 제 말을 들었을지 저도 잘 알아요.」"
h2 "「하지만 지금이 아니면 이런 말을 할 수 없을 것 같아서 그랬어요… 」"
hide harin general with dissolve
scene bg black with fade

play music "audio/grief.mp3"

$renpy.pause(3.0)
# 퇴장 : 후배(harin_sweat_general)
# 배경 전환 : restaurant -> house_players
scene bg house_players with dissolve
# 브금 루프 종료 : 행복(happy)


m "하린이와 식사를 마치고 집으로 돌아왔다."
m "차로 꼭 데려다 줘야겠다는걸 한사코 거절했다."

scene bg black with fade
$renpy.pause(2.0)

m "불을 끄고 침대에 누웠다"
m "며칠 전 민재가 해주었던 말이 떠올랐다."
m "「 '상황을 애매하게 만들지 말고 잘 정리해야지' 」"

m "핸드폰을 만지작 거리며 생각에 잠겼다"


$renpy.pause(2.0)

######################################################################################################################
#분기 5_2_1 -------------------------------------------------------------

m "나는 내일, 누구에게 내 마음을 전해야 하는걸까"
#label test_endBranch:
menu:
    "{color=#4d4d4d}Ending{/color}({color=#E75952}\"윤미래\"{/color});":
        m "그래. 마음은 이미 확실했다."
        m "미래 선배에게 내 확고한 마음을 전해야한다."
        m "심란한 마음을 껴안고 내일이 밝기를 기다렸다."
# 배경 전환 : house_players -> (none)
        m "……………………….."
        m "…………………………"
# 배경 전환 : (none) -> house_players
        stop music fadeout 1.0
        scene bg house_players with fade
        m "금요일 아침. 일어나자 마자 선배에게 문자를 보냈다."
        m "「선배, 오늘 잠깐 시간 내줄 수 있어요?」"
# 배경 전환 : house_players -> (none)
        scene bg black with fade
        m "…………………….."
        m "………………………"
# 배경 전환 : (none) -> campus_ally_day

        play music "audio/sad.mp3"
        scene bg campus_ally_day with fade
        m "학교 산책로에서 선배가 기다리고있었다."
        show mirae general at center with dissolve
        m "다행히 우리 둘 다 금요일에는 오전강의가 없어 시간을 낼 수 있었다."
        m "「선배!」"
# 등장 : 선배(mirae_sweat_general) : 가운데
        m "미래 선배는 나를 보자 잠깐 멈칫하더니 이내 웃으면서 나한테 손을 흔들었다."
        h1 "「[playername], 왔어?」"
        m "내가 다가가자 선배는 다시 얼굴이 조금씩 빨개지는게 보였다."
        stop music fadeout 1.0

        h1 "「그래서… 어떻게 할 생각인데?」"
        m "「선배 할 말이 있어요」"

        window hide
        hide mirae general
        show mirae dark
        with dissolve

        m "예상치 못한 말에 선배가 놀랐는지 다른곳으로 잠시 고개를 돌렸다."
        $renpy.pause(2.0)
        m "그리고 이내 나를 응시하며 고개를 끄덕였다."
        m "「저도 용기를 한 번 내봤어요. 선배.」"
        m "「선배, 선배는 저에게 정말 과분한 사람이라고 생각해요. \n그래서 정말 많이 고민했어요.」"
        m "「 '어설프게 내 마음을 전해서 미래 선배와 멀어지면 어쩌나' 」"
        m "「저는 아직 직면하지도 않은 그 상황을 걱정하고 있었던 것 같아요」"
        window hide
        $renpy.pause(2.0)
        hide mirae dark
        show mirae general
        with dissolve

        $renpy.pause(2.0)
        m "「이젠 그러지 않을게요, 미래선배.」"
        m "「내일 불꽃죽제, 지금의 저로 선배와 마주하고 싶지않아요.」"
        m "「내일은 제가 선배의 남자친구였으면 좋겠어요.」"
        m "「미래 선배는 어떻게 생각해요?\n괜찮다면 저, 한 번 만나주실래요?」"

        window hide
        $renpy.pause(2.0)
        hide mirae general
        show mirae dark
        with dissolve
        m "미래 선배는 나의 얼굴을 잠시동안 쳐다보더니 갑자기 눈물을 흘리기 시작했다."
        m "나는 조용히 선배를 안으면서 아무말도 하지 않았다."
        h1 "「... ... ...」"
        h1 "「... ... ... ...」"
        m "한참 뒤 선배의 조용한 목소리가 들려왔다."
        h1 "「...」"
        h1 "「당연한건 ...」"
        h1 "「... 물어보지마」"
        h1 "「... ... ...」"
        m "선배는 민망했는지 눈을 길게 감았다 떴다"
        window hide
        $renpy.pause(2.0)
        hide mirae dark
        show mirae general
        with dissolve

        h1 "「좋아 이 누나가 한 번 만나주지!」"
        play music "audio/title.mp3"
        h1 "「밥이나 먹으러 가볼까 [playername]!」"
        hide mirae general with dissolve
        window hide

# 브금 루프 시작 : 갬동(title)
        m "산책로에 핀 단풍나무들이 유독 예뻤다."
# 퇴장 : 선배(mirae_sweat_general)
# 배경 전환 :  campus_ally_day -> (none)
        scene bg black with fade

# 에필로그 섹션 ############
# 배경 전환 : (none) -> campus_maingate_day
        scene bg campus_maingate_day with fade
        m "2학기 기말고사가 끝나고, 올 것 같지 않던 종강이 다가왔다."
        m "마지막 시험을 마치고 학교 정문으로 향했다."
        m "저 멀리 입김으로 손을 녹이고 있는 미래 선배가 보였다."
        m "「미래 선배~!」"
        show mirae general at center with dissolve
        m "기다리던 미래 선배는 나를 보더니 행복한 표정으로 다가왔다."
        h1 "「빨리 왔네, [playername]? 원래 지금쯤 수업 끝나서 나오고 있어야 되는거 아니야?」"
        m "「오늘 선배 만나러 가라고 교수님이 빨리 끝내주셨나봐」"
        h1 "「그으래애~? 좋아 그럼 빨리 밥먹으러 가자!」"
        m "미래 선배는 내 손을 잡고 빠르게 식당으로 향했다."
        m "바람에 날린 샴푸향이 풍겨왔다."
        hide mirae general with dissolve




#------------- '2. 유하린' 을 고를경우 ------------------------------------------------------------------------------
    "{color=#4d4d4d}Ending{/color}({color=#E75952}\"유하린\"{/color});":
        m "그래. 마음은 이미 확실했다."
        m "하린이에게 내 확고한 마음을 전해야한다."
        m "심란한 마음을 껴안고 내일이 밝기를 기다렸다."
        # 배경 전환 : house_players -> (none)
        m "……………………….."
        m "…………………………"
        # 배경 전환 : (none) -> house_players
        stop music fadeout 1.0
        scene bg house_players with fade
        m "금요일 아침. 일어나자 마자 하린이에게 문자를 남겨두었다."
        m "「오늘 잠깐 볼 수 있을까, 하린?」"
        # 배경 전환 : house_players -> (none)
        scene bg black with fade
        m "…………………….."
        m "………………………"

        # 배경 전환 : (none) -> campus_bench_day
        scene bg campus_bench_day with fade
        play music "audio/sad.mp3"
        m "벤치에서 캔커피를 마시고 있었다. 멀리서 하린이가 걸어오는 것이 보였다."
        # 등장 : 후배(harin_sweat_general) : 가운데
        show harin general at center with dissolve
        m "손을 흔들자 하린이는 나를 보더니 잠깐 멈칫 하였다. 그러고 이내 내 건너편에 앉았다."
        m "주머니에 넣어 열기를 지켜둔 캔커피를 꺼내들었다"
        m "어디로 가야할지 망설이는 하린이의 손을 잡아, 캔커피를 쥐여주었다"
        m "「오는데 추웠지. 마시면서 이야기하자.」"
        h2 "「...」"
        h2 "「고마워요 잘마실게요」"
        stop music fadeout 1.0
        h2 "「...」"
        h2 "「어제는 죄송해요… 제가 술기운에 그만… 그 어제 일은..」"
        m "「하린아.」"
        m "내가 말을 끊어내자 하린이는 멈칫하며 놀란 기색을 보였다."

        window hide
        hide harin general
        show harin dark
        with dissolve

        $renpy.pause(2.0)
        m "하린이는 알 수 없는 표정으로 신발 앞코로 눈길을 돌렸다"
        m "이내 나와 눈이 마주쳤다."

        window hide
        $renpy.pause(2.0)

        m "「하고싶은 말이 있어」"
        m "하린이에게 좀 더 가까이 붙어 앉았다."
        m "「나한테 넌 정말 과분한 사람이라고 생각해.」"
        m "「그리고 내게 호감을 가져준 것 만으로 정말 고맙게 생각해….」"
        m "하린이는 심각한 표정으로 내 말을 듣기 시작했다"
        m "「어제 하린이 네 말을 듣고 정말 생각을 많이 해봤어.」"
        h2 "「...」"
        m "「정말 잘못 생각하고 있던거지.\n만나보지도 못한 상황에 지레 겁먹고있었어」"
        m "「지금 내가 하린이, 너와 함께 지내는 일상을 잃고 싶지 않았었나봐」"
        m "「내가 새로운 결정을 했을 때 널 잃어버릴까봐.」"
        m "「그걸 가장 무서워했었다는 생각을 해」"
        window hide
        $renpy.pause(2.0)
        m "「이젠 내가 잘못했다는걸 알아.」"
        m "「이제 확실한 사람이 될게」"
        window hide
        $renpy.pause(2.0)
        hide harin dark
        show harin general
        with dissolve

        window hide
        $renpy.pause(2.0)
        h2 "「...」"
        m "「하린아」"

        window hide
        $renpy.pause(2.0)
        m "「괜찮다면, 나랑」"
        m "「한 번 만나볼래?」"

        window hide
        $renpy.pause(2.0)
        hide harin general
        show harin dark
        with dissolve

        $renpy.pause(2.0)
        m "그 순간 하린이는 갑자기 내 품으로 얼굴을 파묻더니 울기 시작했다."
        m "나는 조용히 하린이를 감싸 안았다."

        window hide
        $renpy.pause(2.0)
        m "한참 뒤 하린의 목소리가 들려왔다."

        window hide
        hide harin dark
        show harin general
        with dissolve
        $renpy.pause(2.0)

        h2 "「[playername] 선배….」"
        h2 "「...」"
        h2 "「... 고마워요」"


        play music "audio/title.mp3"
        window hide
        $renpy.pause(2.0)

        # 브금 루프 시작 : 갬동(title)
        m "의자 사이로 감돌던 바람이 멎었다. 시간이 멈춘듯 정적으로 온 공간이 가득찼다."
        hide harin general with dissolve
        # 퇴장 : 후배(harin_sweat_general)
        # 배경 전환 :  campus_bench_day -> (none)
        scene bg black with fade

        # 에필로그 섹션 ####################3
        # 배경 전환 : (none) -> campus_maingate_day
        scene bg campus_maingate_day with fade
        m "2학기 기말고사가 끝나고 겨울방학이 다가오고 있었다. 오후 수업이 끝나고 학교 정문으로 향했다."
        m "경차가 한 대 주차돼있어 지나치려고 하는데, 다급한 목소리가 나를 불러세웠다"
        # 등장 : 후배(harin_sweat_general) : 가운데
        show harin general at center with dissolve
        h2 "「선배! 선배! 어디가요!」"
        m "「?? 왜 거기서 나와? 이것도 네 차였어?」"
        h2 "「더있다가 주차딱지 떼이겠어요! 빨리 타요!」"
        m "「하린이가 운전해주는 차는 오랜만인데. 고맙게 탈게」"
        h2 "「출발합니다~~!」"
        hide harin general with dissolve
        # 퇴장 : 후배(harin_sweat_general)
        m "살짝 열어둔 창문사이로 찬 바람이 새어들었다. 기어위에 올라간 하린의 손에 내 손을 포갰다."


# 모든 ui 내리고, ENDING_BG 표시

image bg ENDING_BG = "images/credit/ENDING_BG.png"
image bg CREDIT_HAKIN = "images/credit/credit_hakin.png"
image bg CREDIT_SANGHYUN = "images/credit/credit_sanghyun.png"
image bg CREDIT_CHANGEUN = "images/credit/credit_changeun.png"
image bg CREDIT_WONJIN = "images/credit/credit_wonjin.png"
image bg CREDIT_TEAM = "images/credit/credit_team.png"

window hide
$quick_menu = False;
scene bg ENDING_BG with fade
$renpy.pause(10.0)

scene bg CREDIT_HAKIN with fade
$renpy.pause(5.0)
scene bg CREDIT_SANGHYUN with fade
$renpy.pause(5.0)
scene bg CREDIT_CHANGEUN with fade
$renpy.pause(5.0)
scene bg CREDIT_WONJIN with fade
$renpy.pause(5.0)
scene bg CREDIT_TEAM with fade
$renpy.pause(10.0)

scene bg ENDING_BG with fade
$renpy.pause(10.0)

scene bg black with fade
################################ 게임 끝 #############################################
################################ 게임 끝 #############################################
################################ 게임 끝 #############################################
#---------------------------------------------------------------------------------------------------------------------
