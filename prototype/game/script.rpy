image bg prologue_1 = "images/prologue_bedroom.png"
image bg black = "#000"
image phoneclock = "images/prologue_phone.jpg"
image bg chap1_bench = "images/chap1_bench.jpg"
image bg chap1_road = "images/chap1_road.jpg"
image senbai who ="images/senbai_who.png"
define playername="Player"
define m = Character("playername",dynamic=True, who_suffix = '@:~$',color="#4B89DC",who_text_align=-19.0)
define system = Character("root",color="#000000",who_suffix = '@:~$')
define pauses = Pause(.5)

label start:
    #jump chapter1
    #prologue scene start
    scene bg prologue_1 with fade
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
    scene bg prologue_1 with dissolve
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
    scene bg chap1_bench with dissolve
    play music "audio/chap1_walking.mp3"
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
            jump chapter1_1_2
            
    label chapter1_1_1:
            stop sound
            stop music fadeout 1.0
            play music "audio/chap1_WhoAreYou.mp3" 
            play sound "audio/chap1_phone_answer.mp3"
            m "「여보세요...?{w} 누구신가요?」" 
            m "나름대로 정중한 말투로 물었다." 
            m "내 전화번호를 아는 사람이라니, 누구지?"
            show senbai who at truecenter with fade
            "???@:~$" "「와~ 네가 받을까 긴가민가 하며 걸었는데{w}\n아직 핸드폰 번호가 그대로구나!」"
            m "수화기 너머 예상치 못한 활기찬 목소리에 내 머리속의 생각회로가 빠르게 굴러가기 시작했다."
            m "그리고 내린 결론은...."
            m "「….? 누구세요?」"
            m "순간적인 고민끝에 내놓은 대답에 잠깐 목소리가 끊겼다"
            m "장난스럽게 흐느끼는 목소리가 들려왔다."
            "???@:~$" "「힝~~ 이 누님의 목소리를 잊다니 좀 섭섭한걸?」"
            "???@:~$" "「설마 잠깐 못본 사이에 나를 기억 못하는 거니?!」"
            m "「저기, 죄송하지만 전화 잘못거신것 같아요..」"
            "???@:~$" "「[playername]."
            m "...내 이름을 아네..!?"
            "???" "「[playername]씨 휴대폰 아닌가요?」"
            m "「아, 네 제가 [playername]맞습니다만.」"
            "???@:~$" "「뭐야 그럼, 제대로 걸은거 맞네~!」"
            "???@:~$" "「너 진짜로 내목소리 기억안나는구나??」"
            m "「네 그렇습니다만..」"
            "???@:~$" "「풉ㅋ」"
            "???@:~$" "「언어 마술사 동아리 방알지?」"
            "???@:~$" "「내가 누군지 궁금하면 언어 마술사 동아리 방으로 와줄래?」"
            "???@:~$" "「기다리고 있을테니까, 도망가면 안된다??~」"
            m "「예? 그게 무슨 말...」"
            hide senbai with fade
            play sound "audio/chap1_phone_answer.mp3"
            system "뚝-"
            m "물어보기가 무섭게 그녀의 전화는 의문만을 남기며 끊어졌다..."
            m "돌이켜보면 1학년때 나는 거의 아싸의 정석같은 존재였다."
            m "고삼때는 나름 대학교에 대한 환상이 있었다.{w}\n cc, mt등등"
            m "그런건 나에게 존재하지 않았다.."
            m "입학 초기에는 나름 대로 내 모습을 바꿔보려고 시도는 해봤다."
            m "하지만 학창시절때 부터 글러먹은 사교성은 대학교 온다고 별반 달라지지 않았다."
            m "뭐, 유일하게 애들이 나한테 말걸때는 수업때 코딩 조금 물어보는정도 밖에 없다."
            m "혼밥은 기본이고, 내 유일한 친구는 노트북이랑 스마트폰밖에 없었는데"
            m "그런데.."
            m "그럼, 이 여잔.. 대체 누구지?"
            m "내 이름이랑 동아리를 아는거보면 나를 아는건 맞는거같은데.."
            m "일단 동아리실로 가볼까?"
            m "나는 동아실로 향했다."
            jump chapter1_1

    label chapter1_1_2:
            stop sound
            m "뭐 전역해도 연락해주는 친구하나 없는데 통화걸어준건 고맙다 임마."
            m "맞다, 입대하기 전까지 활동하던 ‘언어 마술사 동아리'는 어떻게 되었을까?"
            m "동아리실 건물이 어디였더라..?"
            m "나는 동아실로 향했다."
            jump chapter1_1

    label chapter1_1:
            stop music fadeout 1.0 
            $renpy.pause(2.0,hard=True)
            scene bg chap1_road with fade
            play music "audio/chap1_walking.mp3" 
            m "언어 마술사 동아리."
            m "내가 이 학교에 입학하고 나서 뜻 맞는 컴퓨터 관련학과 학부생들이 만든 동아리이다."
            m "아, 동아리에 대한 환상도 있었는데 이것도 깨진지 오래다."
            m "보통 동아리가 그렇듯이, 가끔 술이나 한잔 하면서 지내는 동아리나 다름없었다."
            m "물론 나는 그런쪽이기 보다는 구석에서 쳐박혀서 코딩이나했지만.."
            m "그런데 전역하니까 전혀 다른 소문을 듣게 되었는데" 
            m "내가 없는 동안 수많은 프로젝트를 진행했고, 대회에 나갔다 하면 상을 휩쓸어가는 괴물같은 실력의 동아리가 되어있었다"
            m "게다가 코딩을 전혀 할 줄 모르는 사람도 가르쳐주고 있어"
            m "학점 잘따려는 애들이나 코딩에 관심있는 사람들이 줄을 서고 있다고 한다."
            m "대체 술이나 마시던 동아리가 어떻게 제대로 돌아가게 된건지 궁금하구만."
            m "나는 가벼운 발걸음으로 동아실로 향했다."