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

image senbai ="images/senbai_who.png"

image mirae general ="images/mirae_general.png"

image extra1="images/other_black_1.png"
image extra2="images/other_black_2.png"
image extras="images/others_black.png"

define callignore=False
define playername="Player"
define extraname="Player"
define m = Character("playername",dynamic=True, who_suffix = '@:~$',color="#4B89DC",who_text_align=-17.0)
define system = Character("system",color="#000000",who_suffix = '@:~$',who_text_align=-17.0)
define extra = Character("extraname",dynamic=True,color="#000000",who_suffix = '@:~$',who_text_align=-17.0)
define h1 = Character("윤미래",color="#8D43CA",who_suffix = '@:~$',who_text_align=-17.0)
define h2 = Character("유하린",color="#01003A",who_suffix = '@:~$',who_text_align=-17.0)
define pauses = Pause(.5)

label start:
    stop music
    jump chapter1
    #prologue scene start
    scene bg house_players with fade
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
            m "뭐 전역해도 연락해주는 친구하나 없는데 통화 걸어준건 고맙다."
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
            m "'언어의 사랑' 동아리."
            m "내가 이 학교에 입학하고 나서 뜻 맞는 컴퓨터 관련학과 학부생들이 만든 동아리이다."
            m "아, 고딩때는 대학교 동아리에 대한 환상이 있었는데 깨진지 오래다."
            m "보통 동아리가 그렇듯이, 가끔 술이나 한잔 하면서 지내는 동아리나 다름없었다."
            m "물론 나는 회장이기도하고 그런쪽이기 보다는 구석에서 쳐박혀서 코딩이나했지만.."
            m "그런데 전역하니까 전혀 다른 소문을 듣게 되었는데" 
            m "내가 없는 동안 수많은 프로젝트를 진행했고, 대회에 나갔다 하면 상을 휩쓸어가는 괴물같은 실력의 동아리가 되어있었다"
            m "게다가 코딩을 전혀 할 줄 모르는 사람도 가르쳐주고 있어"
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
$renpy.pause(1.0,hard=True)
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
$renpy.pause(1.0,hard=True)
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
m "윤미래 , 2학년이 전례없이 학생회장이 된 것으로 큰 주목을 받았다. 이에 더해 기존의 총학들이 해결하지 못하던 일들을 척척 해결해내며 학생들의 압도적인 지지를 받았다."
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
$renpy.pause(1.0,hard=True)


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
h1 "「바로 우리 컴공 수재 [playername]씨!」"
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