# 배열로 letter/digit/0/기타 등등 선언
Letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
          'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
Digit = ['1','2','3','4','5','6','7','8','9']
Zero = '0'
Others = ['+', '*', '/', '-', ';','_',' ','\t','\n','(',')','{','}','[',']','>','<','=','!','\'','\"',',']


#state 에 따라 token 을 결정
def checkToken(state):
    if state in [1]:
        return "Vtype"
    elif state in [2] or (state in [i for i in range(100,141)] and state not in [102,109,115,119,125,129,134,135,140]): 
        return "ID"
    elif state in [3,4]:
        return "Operator"
    elif state in [5]:
        return "Semicolon"
    elif state in [6]:
        return "Underbar"
    elif state in [7,22,23]: #discard
        return "WhiteSpace"
    elif state in [8]:
        return "Lparen"
    elif state in [9]:
        return "Rparen"
    elif state in [10]:
        return "Lbrace"
    elif state in [11]:
        return "Rbrace"
    elif state in [12]:
        return "Lbraket"
    elif state in [13]:
        return "Rbraket"
    elif state in [14,19,26,27]:
        return "Compare"
    elif state in [15]:
        return "Assign"
    elif state in [20]:
        return "String"
    elif state in [24]:
        return "Char"
    elif state in [25,29]:     
        return "Integer"
    elif state in [28]:
        return "KW"
    elif state in [30]:
        return "Comma"

    else: 
        return "Error" 



def next_token_letter(lex, k, nowstate): 
    # kw/vtype를 구별하기 위한 과정
    # 맨 처음으로 letter가 입력되면 Vtype 과 KW 가 될 수 있으므로
    if nowstate == 0:
        if k =='i': nowstate = 100
        elif k =='c': nowstate = 116
        elif k =='r': nowstate = 120
        elif k =='S': nowstate = 110
        elif k =='b': nowstate = 103
        elif k =='e': nowstate = 138
        elif k =='w': nowstate = 130
        else: nowstate = 2
    return nowstate

def state_change(lex, nowstate, k, beforetoken): # nowstate와 k 입력이 주어졌을 때 state 변화
    # d 2 #

    end = False #false인 상태가 기본
    if k not in Others and k not in Digit and k not in Letter and k not in Zero:
        #when undefined symbol given for next input
        nowstate = 31
        return lex, nowstate, end # 3개 값 리턴


    
    if nowstate in [17] and k is None: # \"
        end = True # 끝내야한다 -> 더이상 읽지 않는다
        lex = "Error"
        return lex, nowstate, end


    if k is None: #맨 마지막일때 k는 아무런 값도 없음
        end = True
        if nowstate == 31: #when undefined input is given
            end = True #do not read more
            lex = "Error"
            return lex, nowstate, end 
        
        if (state in [i for i in range(100,141)] and state not in [102,109,115,119,125,129,134,135,140]):
            nowstate = 2
        return lex, nowstate, end


    if nowstate == 0: #맨 처음일 때
        if k in Letter: 
            nowstate = next_token_letter(lex,k,nowstate) # Kw, Vtype 확인하러
            lex+=k
            return lex, nowstate, end 
            
        else:
            lex += k 
            if k == Zero: nowstate = 29
            elif k in Digit: nowstate = 25
            elif k in ['+', '*', '/']: nowstate = 3
            elif k == '-': nowstate = 4
            elif k == ';': nowstate = 5
            elif k == '_': nowstate = 6

            elif k == ' ': nowstate = 22
            elif k == '\t': nowstate = 23
            elif k == '\n': nowstate = 7

            elif k == '(': nowstate = 8
            elif k == ')': nowstate = 9
            elif k == '{': nowstate = 10
            elif k == '}': nowstate = 11
            elif k == '[': nowstate = 12
            elif k == ']': nowstate = 13

            elif k in ['>', '<']: nowstate = 14
            elif k == '=': nowstate = 15
            elif k == '!': nowstate = 16

                
            elif k == '\"': nowstate = 17
            elif k == '\'': nowstate = 18  
            elif k == ',': nowstate=30
            else: nowstate = 31

             

        return lex, nowstate, end 



    elif nowstate == 31: #when undefined input is given
        end = True #do not read more
        lex = "Error"
        return lex, nowstate, end 

    elif nowstate == 4: #op(-)
        if beforetoken in ["ID", "Integer", "Rparen"]: # 앞 토큰을 보고 연산자인 경우
            nowstate=4
            end=True
            return lex, nowstate, end
        
        elif beforetoken in [ "", "WhiteSpace","Operator", "Lparen", "Compare", "Assign", "Underbar","String","Char" ,"Comma", "Lbrace"]:
            if k in Digit: #이때만 음수
                nowstate = 25
                lex+=k
                return lex, nowstate, end
            else: # 음수에 해당하지 않는 부분은 연산자로
                nowstate=4
                end=True
                return lex, nowstate, end
        else: # 나머지의 경우는 연산자로
            nowstate=4
            end=True
            return lex, nowstate, end

            
            
        
        return "Error", nowstate, end

    #===============================================================
    #ID, KW, Vtype 구별
    elif nowstate in [i for i in range(100,141)]:
        #print("!1")
        if k not in Letter: # i 뒤에 다른 것이 나올 때 op, compate 등
            end = True #ex) lkadf;
            #print("!2")
            return lex, nowstate, end 

        if (nowstate,k) == (100,'n'): # i -> in
            nowstate = 101 
        elif (nowstate,k) == (100,'f'): #i -> if
            nowstate = 28 
        elif (nowstate,k) == (101,'t'): # in->int
            nowstate = 1 
        elif (nowstate,k) == (103,'o'): #b->bo
            nowstate = 104 
        elif (nowstate,k) == (104,'o'): # bo->boo
            nowstate = 105 
        elif (nowstate,k) == (105,'l'): # boo->bool
            nowstate = 106 
        elif (nowstate,k) == (106,'e'): #bool->boole
            nowstate = 107 
        elif (nowstate,k) == (107,'a'): #boole -> boolea
            nowstate = 108 
        elif (nowstate,k) == (108,'n'): #boolea->boolean
            nowstate = 1 
        elif (nowstate,k) == (110,'t'): #S->st
            nowstate = 111
        elif (nowstate,k) == (111,'r'): #St->Str
            nowstate = 112
        elif (nowstate,k) == (112,'i'):#Str->Stri
            nowstate = 113
        elif (nowstate,k) == (113,'n'): #Stri->Strin
            nowstate = 114
        elif (nowstate,k) == (114,'g'): #Strin->String
            nowstate = 1
        elif (nowstate,k) == (116,'h'): #c->ch
            nowstate = 117
        elif (nowstate,k) == (116,'l'): #c->cl
            nowstate = 126
        elif (nowstate,k) == (117,'a'):#ch->cha
            nowstate = 118
        elif (nowstate,k) == (118,'r'):#cha->char
            nowstate = 1
        elif (nowstate,k) == (120,'e'): #r->re
            nowstate = 121
        elif (nowstate,k) == (121,'t'):  #re->ret
            nowstate = 122
        elif (nowstate,k) == (122,'u'): #ret->retu
            nowstate = 123
        elif (nowstate,k) == (123,'r'): #retu->retur
            nowstate = 124
        elif (nowstate,k) == (124,'n'): #retur->return
            nowstate = 28
        elif (nowstate,k) == (126,'a'): #cl->cla
            nowstate = 127
        elif (nowstate,k) == (127,'s'): #cla->clas
            nowstate = 128
        elif (nowstate,k) == (128,'s'):  #clas->class
            nowstate = 28
        elif (nowstate,k) == (130,'h'): # w->wh
            nowstate = 131
        elif (nowstate,k) == (131,'i'): # wh->whi
            nowstate = 132
        elif (nowstate,k) == (132,'l'): # whi->whil
            nowstate = 133
        elif (nowstate,k) == (133,'e'): # whil->while
            nowstate = 28
        elif (nowstate,k) == (138,'l'): #e->el
            nowstate = 139
        elif (nowstate,k) == (139,'s'): #el->els
            nowstate = 140
        elif (nowstate,k) == (140,'e'): #els->else
            nowstate = 28
        elif k in ["\n", "\t"," "]:
            end = True
            return lex, nowstate, end

        else: #중간에 다른 letter이 들어오면 무조건ID가 된다
            nowstate = 2
            
        lex += k
        return lex, nowstate, end
        
    #end state
    elif nowstate in [3,5,7,8,9,10,11,12,13,19,20,22,23,24,26,27,29,30]: # 더이상 읽지 않고 끝내야할 것
        end = True
        return lex, nowstate, end

    elif nowstate in [1,6,2]: # _
        if k in Letter or k in Zero or k in Digit or k == '_' : 
            nowstate = 2
            lex += k
            return lex, nowstate, end 
        else: 
            end = True
            return lex, nowstate, end
        
    elif nowstate == 14: # <,>
        if k == '=':
            nowstate = 26
            lex+=k
            return lex, nowstate, end
        else:
            end = True
            return lex, nowstate, end

    elif nowstate == 15: # =
        if k == '=':
            nowstate = 27
            lex+=k
            return lex, nowstate, end
        else:
            end = True
            return lex, nowstate, end
        
    elif nowstate == 28: #KW
        if k in Letter or k in Zero or k in Digit or k == '_' : 
            nowstate = 2
            lex += k
            return lex, nowstate, end 
        else: 
            end = True
            return lex, nowstate, end

    elif nowstate == 25: #integer
        if k in Zero or k in Digit:
            nowstate = 25
            lex+=k
            return lex, nowstate, end 
        else:
            end = True
            return lex, nowstate, end

    elif nowstate == 16: #!
        if k=='=':
            lex += k
            nowstate = 19
            return lex, nowstate, end
        else: 
            end = True
            lex = "Error"
            return lex, nowstate, end


    elif nowstate == 17:
        if k=='\"':
            nowstate = 20
            lex += k
            return lex, nowstate, end
        else: 
            nowstate = 17
            lex += k
            return lex, nowstate, end

    elif nowstate == 18:
        if k in Letter or k in Zero or k in Digit or k ==" ":
            nowstate = 21
            lex += k
            return lex, nowstate, end
        else: 
            end = True
            lex = "Error"
            return lex, nowstate, end

    elif nowstate == 21:
        if k=='\'':
            nowstate = 24
            lex += k
            return lex, nowstate, end
        else: 
            end = True
            lex = "Error"
            return lex, nowstate, end


def Lex(line):
    fin = [] # return value
    end = False # check whether reading input is done or not
    beforetoken = "" # need this to figure out role of -; operator or negative integer
    lex = "" # parsing
    nowstate=0 # start state

    i = 0 # for while loop, initialize
    while True:
        #print("\n")
        if(i==len(line)): break
        
        #print(line[i], lex, nowstate, end)
        #print(lex, nowstate, line[i])

        lex, nowstate, end = state_change(lex, nowstate, line[i], beforetoken)

        #print(line[i], lex, nowstate, end)
        #print(lex, nowstate, line[i],i)

        if(i==len(line)-1):
            if nowstate in [16,17,18,21,31]:
                #읽기가 모두 끝났는데 unvaild end state에 있으면 error
                lex = "Error"
                end = True

        
 
        if(lex == "Error"): #when error occurs
            fin.append([lex, "Error"])
            break # stop while loop

        if(end == False): #if reading lex is not done, keep reading
            i+=1
        
        if(end == True or i == len(line)): # stop reading
            token = checkToken(nowstate)

            if nowstate == 7: #when nowstate is 7 which is newline:
                beforetoken = "" #reinitialize beforetoken (for '-') 

            if(token != "WhiteSpace"): #discard Whitespace
                fin.append([lex,token]) # append lex and token
                #print(lex, nowstate, beforetoken, token)
                beforetoken = token 
                #문제: 줄바꿈 -1 을 int로 인식 못함, 근데 여기서 미리 처리하고 후 과정을 보는 게 더 나을 듯
                #해결방안: \n 받을 때 (줄바꿈, 새로운 줄) 아예 beforetoken 을 초기화
                

            #initialize for next parsing
            nowstate = 0
            lex = ""
            end = False
    return fin

#main
if __name__ == "__main__":
    
    #f = open('D:\git\Compiler\compiler\input.txt', 'r',encoding='UTF-8')
    f = open('input1.txt', 'r',encoding='UTF-8')
    #f = open('input2.txt', 'r',encoding='UTF-8')

    myline = f.read() #파일 내용 한번에 읽기
    fin=[]
    fin = Lex(myline)
    f.close()

    #out = open('D:\git\Compiler\compiler\output.txt', 'w')
    out = open('output1.txt', 'w')
    #out = open('output2.txt', 'w')

    for i in range(len(fin)): 
        line = ""
        line= line +fin[i][1]  + ' , ' + fin[i][0] 
        out.write(line)
        out.write("\n")
    out.close()
