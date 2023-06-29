# 제작 수피아여고 10913 양유솔(@l.____.sol)
# 버그문의 DM
# 230522~230526
# 파일명 양식 : RPyG 메이저버전.마이너버전.년도.월일

atk = 0
dep = 0

def damage_exp():
    damage = int(atk - dep)
    if defend == True : damage = int(damage/2)
    if damage < 1 : damage = 1
    return damage

# 파이썬으로 전투를 만들고 싶던 아이는 기막힌 생각을 해냈지!
print("야생의 '허접해 보이는 슬라임'이 당신의 앞을 가로막았다!")
yourhpmax = 100 #최대체력
yourhp = yourhpmax
yourspmax = 70 #최대sp
yoursp = yourspmax
youratk = 40 #공격력
yourdef = 30 #방어력
slimehpmax = 100
slimehp = slimehpmax
slimespmax = 5
slimesp = slimespmax
slimeatk = 20
slimedef = 20
turn = 0 #턴수
# 여기부터 상태이상 변수
slimeacid = 0 #방깎
slimeacidcooltime = 4 #턴마다 1씩 증가/4가 되면 방깎 시전 후 리셋
slimerecovery = 0 #자힐
slimerecoverhealth = 0 #자힐량
slimerecovercooltime = 0 #0일 시 자힐 시전 후 3 부여/이후 턴마다 1씩 하락
slimerecovered = False #자힐코드 실행여부
gitti = False #기띠
gittilast = 0 #기띠 지속시간
print("#######################################################")
while 0 < slimehp and yourhp :
    defend = False #방어 커맨드 리셋
    skillexed = False #스킬 실행여부 리셋
    nosp = False #sp 부족 여부 리셋
    turn = turn + 1
    print("현재",turn,"턴째")
    print("'당신'의 hp",yourhp,"/",yourhpmax,", sp",yoursp,"/",yourspmax)
    print("'허접해 보이는 슬라임'의 hp",slimehp,"/",slimehpmax)
    # print("slimesp",slimesp,"/",slimespmax) #자힐패턴 sp 체크용
    print("------------------------------------------------------------")
    while True : #행동 선택문
     print("'당신'은 무엇을 할까?")
     print("[0. 상태를 살핀다/1. 공격/2. 스킬/3. 방어]")
     choice = input("선택: ")
     print("------------------------------------------------------------")
     if choice == '1' : #평타
         print("'당신'의 공격!")
         atk = youratk
         dep = slimedef
         damage = damage_exp()
         print("'허접해 보이는 슬라임'에게",damage,"피해!")
         slimehp = int(slimehp - damage)
         print("------------------------------------------------------------")
         break
     elif choice == '2' : #스킬
         while True : #스킬 선택문
             print("0. sp가 모자라...")
             print("1. 이악물기(sp 3 소모) / 3턴간 hp가 0이 되는 공격을 받아도 한 번 hp 1로 버틴다.")
             print("2. 응급처치(10) / 자신의 hp를 25% 회복한다.")
             print("3. 세게 베기(15) / 상대에게 공격력 150%의 피해를 준다.")
             print("4. 개쎄게 베기(30) / 상대에게 방어력의 일부를 무시하고 공격력 200%의 피해를 준다.")
             print("255. 테스트 스킬") #테스트용으로 만들어둔 스킬들
             skill = input("선택: ")
             print("------------------------------------------------------------")
             if skill == '0' : #sp 없을 때 탈출용
                 nosp = True
             elif skill == '1' : #기합의띠
                 if gitti == True : print("'당신'은 이미 이를 악물고 있다!")
                 elif yoursp < 3 : print("sp가 모자라다!")
                 else :
                     gitti = True
                     gittilast = 3
                     print("'당신'은 이를 악물었다!")
                     skillexed = True #스킬 실행여부 체크
             elif skill == '2' : #자힐
                     if yourhp == yourhpmax : print("'당신'의 hp는 이미 최대다!")
                     elif yoursp < 10 : print("sp가 모자라다!")
                     else :
                         print("'당신'의 응급처치!")
                         health = int((yourhpmax)*0.25)
                         if yourhp+health > yourhpmax : health = yourhpmax-yourhp
                         print("hp가",health,"만큼 회복되었다!")
                         skillexed = True
             elif skill == '3' : #세게베기
                 if yoursp<15 : print("sp가 모자라다!")
                 else :
                     yoursp = yoursp - 15
                     atk = youratk*1.5
                     dep = slimedef/2
                     damage = damage_exp()
                     print("'당신'의 '세게 베기'!")
                     print("'허접해 보이는 슬라임'에게",damage,"피해!")
                     slimehp = slimehp - damage
                     skillexed = True
             elif skill == '4' : #개쎄게베기
                 if yoursp < 30 : print("sp가 모자라다!")
                 else :
                     yoursp = yoursp - 30
                     atk = youratk*2
                     dep = slimedef*0.2
                     damage = damage_exp()
                     slimehp = slimehp - damage
                     print("'당신'의 '개쎄게 베기'!")
                     print("'허접해 보이는 슬라임'에게",damage,"피해!")
                     skillexed = True
             elif skill == '255' : #디버그스킬
                 while True :
                  print("1. 자살하기(0) / 자신의 hp를 1로 만든다.")
                  print("2. 죽이기(0) / 상대에게 10000의 피해를 준다.")
                  print("3. sp 내다버리기(100) / sp를 100 소모한다.")
                  print("4. 튀어오르기(0) / 아무 일도 일어나지 않는다.")
                  testskill = input("선택: ")
                  print("------------------------------------------------------------")
                  if testskill == '1' : #게임오버 테스트
                     print("'당신'은 자살을 시도했다!")
                     print("'당신'의 hp 1로 감소!")
                     yourhp = 1
                     skillexed = True
                  elif testskill == '2' : #즉사스킬
                     print("'당신'은 '허접해 보이는 슬라임'을 검지손가락으로 겨누며 그렇게 말했다.")
                     print("“반으로 갈라져서 죽어.”")
                     damage = 10000
                     slimehp = int(slimehp - damage)
                     print("'허접해 보이는 슬라임'에게 10000 의 피해!")
                     if slimehpmax <= damage : print("'허접해 보이는 슬라임'은 즉사했다!")
                     skillexed = True
                  elif testskill == '3' : #sp가부족하다 띄우기용
                      print("이게 당신의",yoursp,"sp입니다.")
                      yoursp = yoursp - 100
                      if yoursp < 0 : yoursp = 0
                      print("이제",yoursp,"sp군요.")
                      skillexed = True
                  elif testskill == '4' : #튀어오르기
                      print("'당신'의 튀어오르기!")
                      print("아무 일도 일어나지 않았다!")
                      skillexed = True
                  else :
                     print("에? 난닷떼?")
                     print("------------------------------------------------------------")
                  if skillexed == True : break
             else :
              print("오류! 루프!")
             if skillexed or nosp == True : break
         print("------------------------------------------------------------")
         if skillexed or nosp == True : break
     elif choice == '3' : #방어, 해당 턴 받는 피해/2
         print("'당신'은 몸을 지키고 있다...")
         print("------------------------------------------------------------")
         break
     elif choice == '0' :
         print("'당신'")
         print("hp -",yourhp,"/",yourhpmax)
         print("sp -",yoursp,"/",yourspmax)
         print("atk -",youratk," /  def -",yourdef)
         if slimeacid>0 : print("방어구의 몇몇 부분이 녹아 있다(def -5), 앞으로",slimeacid,"턴 남음")
         if gitti == True : print("이를 악물고 있다(hp 0 -> 1). 앞으로",gittilast,"턴 남음.")
         # 여기부터 다른 상태 넣기, 스킬 구현 이후 작업예정
         print("------------------------------------------------------------")
         print("'허접해 보이는 슬라임'")
         print("hp -",slimehp,"/",slimehpmax)
         print("sp -",slimesp,"/",slimespmax)
         print("atk -",slimeatk," /  def -",slimedef)
         if slimerecovered == True : print("파괴된 조직들을 재생하고 있다(턴 종료 시 hp",slimerecoverhealth,"회복). 앞으로",slimerecovery,"턴 남음")
         print("------------------------------------------------------------")
     else :
         print("오류! 루프!")
    if slimehp <= 0 : print("'허접해 보이는 슬라임'은 쓰러졌다!")
    else :
        if slimeacidcooltime >= 4 : #slimeacid
            print("'허접해 보이는 슬라임'이 '당신'의 몸에 달라붙어서는 달라붙은 부분이 녹아내린다!")
            atk = slimeatk*0.7
            dep = yourdef/2
            damage = damage_exp()
            print("'당신'에게",damage,"피해!")
            yourhp = yourhp - damage
            slimeacid = 3
            yourdef = yourdef-5
            print(slimeacid,"턴 동안 def 5 감소!")
            slimeacidcooltime = 0
        elif slimehp<slimehpmax/2 and slimesp>=int(slimespmax*0.6) and slimerecovercooltime == 0 :
            slimesp = slimesp - int(slimespmax*0.6)
            health = int(slimehpmax/10)
            slimerecoverhealth = int(slimehpmax*0.08)
            slimehp = slimehp + health
            print("'허접해 보이는 슬라임'이 손상된 조직들을 수복하고 있다!")
            print("hp가",health,"만큼 회복되었다!")
            print("앞으로 5턴간 지속적으로",slimerecoverhealth,"만큼의 hp가 회복된다!")
            slimerecovery = 5
            slimerecovercooltime = 3
            slimerecovered = True
        else :
         print("'허접해 보이는 슬라임'의 공격!")
         atk = slimeatk
         dep = yourdef
         damage = damage_exp()
         print("'당신'에게",damage,"피해!")
         yourhp = yourhp - damage 
        print("------------------------------------------------------------")
    yoursp = int(yoursp + yourspmax*0.05)
    if yoursp > yourspmax : yoursp = yourspmax
    slimesp = int(slimesp + slimespmax*0.05)
    if slimesp > slimespmax : slimesp = slimespmax
    slimeacidcooltime = slimeacidcooltime + 1
    if yourhp<=0 :
        if gitti == True :
            print("'당신'은 버텨냈다!")
            print("hp 1로 유지!")
            yourhp = 1
            gitti = False
        else :
            print("'당신'은 쓰러지고 말았다...")
            break # 솔직히 진심으로 이유를 모르겠는데 이악물기 쓰고 나면 변수가 False로 돌아간 이후에도 게임오버 판정이 안 나서 추가함
    else :
     if slimeacid>1 : slimeacid = slimeacid - 1
     elif slimeacid == 1 :
         slimeacid = 0
         yourdef = yourdef + 5
         print("방어구의 녹아내린 부분을 수습했다. def 복구.")
     if gittilast > 1 : gittilast = gittilast-1
     elif gittilast == 1 :
         gittilast = 0
         gitti = False
         print("이를 악물던 힘이 풀렸다.")
         print("'이 악물기' 효과 소실!")
    if (slimerecovered == True) and (slimehp>0) : #이 부분 귀찮아서 QA 안했음 버그나면 바로 알려줘
     if slimehp == slimehpmax :
         slimerecovered = False
         print("'허접해 보이는 슬라임'이 조직의 수복을 멈췄다.")
         slimerecovery = 0
     elif slimerecovery >= 1 :
         if slimehp+slimerecoverhealth > slimehpmax : slimerecoverhealth = slimehpmax-slimehp
         slimehp = slimehp + slimerecoverhealth
         print("'허접해 보이는 슬라임'이 조직들을 수복해 hp를",slimerecoverhealth,"회복했다.")
         slimerecovery = slimerecovery - 1
         if (slimehp == slimehpmax) or (slimerecovery == 1) :
             print("'허접해 보이는 슬라임'이 조직의 수복을 멈췄다.")
             slimerecovery = 0
             slimerecoverd = False
     else :
         print("아싯팔 버그다!!!!!!!")
         print("턴 끝나고 슬라임 자힐변수 체크에서 터졌어!!!!1!!!!!!")
    print("#######################################################")
if slimehp <= 0 :
    print("You Win!")
    print("제작 양유솔")
    print("Thank you for playing!")
elif yourhp <= 0 :
    print("You lose...")
    print("GAME OVER")
else :
    print("아싯팔 버그다!!!!!!!")
    print("둘 다 피 양수인데 루프문 탈출함!!!!!!!!!")