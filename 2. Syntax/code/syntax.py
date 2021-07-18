import sys


before_reduce={
    "r0"  : ["CODE"],
    "r1"  : ["CDECL", "CODE"],
    "r2"  : ["VDECL", "CODE"],
    "r3"  : ["FDECL", "CODE"],
    "r4"  : [""],
    "r5"  : ["vtype", "id", "semi"],
    "r6"  : ["vtype", "ASSIGN", "semi"],
    "r7"  : ["id", "assign", "RHS"],
    "r8"  : ["EXPR"],
    "r9"  : ["literal"],
    "r10" : ["character"],
    "r11" : ["boolstr"],
    "r12" : ["FACTOR", "addsub", "EXPR"], 
    "r13" : ["FACTOR"],
    "r14" : ["TERM", "multdiv", "FACTOR"],
    "r15" : ["TERM"],
    "r16" : ["lparen", "EXPR", "rparen"],
    "r17" : ["id"],
    "r18" : ["num"],
    "r19" : ["vtype", "id", "lparen", "ARG", "rparen", "lbrace", "BLOCK", "RETURN", "rbrace"],
    "r20" : ["vtype", "id", "MOREARGS"],
    "r21" : [""],
    "r22" : ["comma", "vtype", "id", "MOREARGS"],
    "r23" : [""],
    "r24" : ["STMT", "BLOCK"],
    "r25" : [""],
    "r26" : ["VDECL"],
    "r27" : ["ASSIGN", "semi"],
    "r28" : ["if", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace", "ELSE"],
    "r29" : ["while", "lparen", "COND", "rparen", "lbrace", "BLOCK", "rbrace"],
    "r30" : ["TERM", "comp", "TERM"],
    "r31" : ["BOOL"],
    "r32" : ["boolstr"],
    "r33" : ["else", "lbrace", "BLOCK", "rbrace"],
    "r34" : [""],
    "r35" : ["return", "RHS", "semi"],
    "r36" : ["class","id", "lbrace", "ODECL", "rbrace"],
    "r37" : ["VDECL","ODECL"],
    "r38" : ["FDECL","ODECL"],
    "r39" : [""], 
}

after_reduce={
    "r0":"FINAL", 
    "r1" : "CODE",
    "r2" : "CODE",
    "r3" : "CODE",
    "r4" : "CODE",
    "r5" : "VDECL",
    "r6" : "VDECL",
    "r7" : "ASSIGN",
    "r8" : "RHS",
    "r9" : "RHS",
    "r10" : "RHS",
    "r11" : "RHS",
    "r12" : "EXPR",
    "r13" : "EXPR",
    "r14" : "FACTOR",
    "r15" : "FACTOR",
    "r16" : "TERM",
    "r17" : "TERM",
    "r18" : "TERM",
    "r19" : "FDECL",
    "r20" : "ARG",
    "r21" : "ARG",
    "r22" : "MOREARGS",
    "r23" : "MOREARGS",
    "r24" : "BLOCK",
    "r25" : "BLOCK",
    "r26" : "STMT",
    "r27" : "STMT",
    "r28" : "STMT",
    "r29" : "STMT",
    "r30" : "COND",
    "r31" : "COND",
    "r32" : "BOOL",

    "r33" : "ELSE",
    "r34" : "ELSE",
    "r35" : "RETURN",
    "r36" : "CDECL",
    "r37" : "ODECL",
    "r38" : "ODECL",
    "r39" : "ODECL",
}

goto_table = {
    # 0
    (0,"CODE") : 1,
    (0,"VDECL") : 2,
    (0,"FDECL") : 3,
    (0,"CDECL") : 4,

    #2
    (2,"CODE") : 7,
    (2,"VDECL") : 2,
    (2,"FDECL") : 3,
    (2,"CDECL") : 4,

    #3
    (3,"CODE") : 8,
    (3,"VDECL") : 2,
    (3,"FDECL") : 3,
    (3,"CDECL") : 4,

    #4
    (4,"CODE") : 9,
    (4,"VDECL") : 2,
    (4,"FDECL") : 3,
    (4,"CDECL") : 4,

    #5
    (5,"ASSIGN") : 11,

    # 14
    (14,"ARG"):18,

    #15
    (15,"RHS") : 20,
    (15,"EXPR") : 21,
    (15,"FACTOR") : 25,
    (15,"TERM") : 26,

    #17
    (17,"VDECL") : 31,
    (17,"FDECL") : 32,
    (17,"ODECL") : 30,

    #27
    (27,"EXPR") : 37,
    (27,"FACTOR") : 25,
    (27,"TERM") : 26,




    #31
    (31,"VDECL") : 31,
    (31,"FDECL") : 32,
    (31,"ODECL") : 39,

    #32
    (32,"VDECL") : 31,
    (32,"FDECL") : 32,
    (32,"ODECL") : 40,


    #34
    (34,"MOREARGS") : 42,

    #35
    (35,"EXPR") : 44,
    (35,"FACTOR") : 25,
    (35,"TERM") : 26,


    #36
    (36,"FACTOR") : 45,
    (36,"TERM") : 26,



    #41
    (41,"VDECL") : 49,
    (41,"ASSIGN") : 50,
    (41,"BLOCK") : 47,
    (41,"STMT") : 48,

    #47
    (47,"RETURN") : 56,

    #48
    (48,"VDECL") : 49,
    (48,"ASSIGN") : 50,
    (48,"BLOCK") : 58,
    (48,"STMT") : 48,

    #53
    (53,"ASSIGN") : 11,

    #57
    (57,"RHS") : 65,
    (57,"EXPR") : 21,
    (57,"FACTOR") : 25,
    (57,"TERM") : 26,

    #60
    (60,"COND") : 66,
    (60,"BOOL") : 67,

    #61
    (61,"COND") : 69,
    (61,"BOOL") : 67,


    # 63
    (63,"MOREARGS") : 70,




    #73
    (73,"BOOL") : 76,

    #75
    (75,"VDECL") : 49,
    (75,"ASSIGN") : 50,
    (75,"BLOCK") : 78,
    (75,"STMT") : 48,

    #77
    (77,"VDECL") : 49,
    (77,"ASSIGN") : 50,
    (77,"BLOCK") : 79,
    (77,"STMT") : 48,

    #80
    (80,"ELSE") : 82,

    #84
    (84,"VDECL") : 49,
    (84,"ASSIGN") : 50,
    (84,"BLOCK") : 85,
    (84,"STMT") : 48,

}

action_table = {

    # 86 6
    (86 ,"vtype" ):"r33",
    (86 ,"id" ):"r33",
    (86 ,"rbrace" ):"r33",
    (86 ,"if" ):"r33",
    (86 ,"while" ):"r33",
    (86 ,"return" ):"r33",

    #85 1
    (85 ,"rbrace" ):"s86",

    #84 6
    (84 ,"vtype" ):"s53",
    (84 ,"id" ):"s54",
    (84 ,"rbrace" ):"r25",
    (84 ,"if" ):"s51",
    (84 ,"while" ):"s52",
    (84 ,"return" ):"r25",

    #83 1
    (83 ,"lbrace" ):"s84",


    #82 6
    (82 ,"vtype" ):"r28",
    (82 ,"id" ):"r28",
    (82 ,"rbrace" ):"r28",
    (82 ,"if" ):"r28",
    (82 ,"while" ):"r28",
    (82 ,"return" ):"r28",

    #81 6
    (81 ,"vtype" ):"r29",
    (81 ,"id" ):"r29",
    (81 ,"rbrace" ):"r29",
    (81 ,"if" ):"r29",
    (81 ,"while" ):"r29",
    (81 ,"return" ):"r29",

    #80 7
    (80 ,"vtype" ):"r34",
    (80 ,"id" ):"r34",
    (80 ,"rbrace" ):"r34",
    (80 ,"if" ):"r34",
    (80 ,"while" ):"r34",
    (80 ,"else" ):"s83",
    (80 ,"return" ):"r34",

    #79 1
    (79 ,"rbrace" ):"s81",

    #78 1
    (78 ,"rbrace" ):"s80",

    #77 6
    (77 ,"vtype" ):"s53",
    (77 ,"id" ):"s54",
    (77 ,"rbrace" ):"r25",
    (77 ,"if" ):"s51",
    (77 ,"while" ):"s52",
    (77 ,"return" ):"r25",

    #76 1 
    (76 ,"rparen" ):"r30",
    # ================
    #75 6
    (75 ,"vtype" ):"s53",
    (75 ,"id" ):"s54",
    (75 ,"rbrace" ):"r25",
    (75 ,"if" ):"s51",
    (75 ,"while" ):"s52",
    (75 ,"return" ):"r25",

    #74 1
    (74 ,"lbrace" ):"s77",

    #73 
    (73 ,"boolstr" ):"s68",

    #72 1
    (72 ,"lbrace" ):"s75",

    #71 1
    (71 ,"rbrace" ):"r35",

    #70 1
    (70 ,"rparen" ):"r22",

    #69 1
    (69 ,"rparen" ):"s74",
    
    # 68 2
    (68 ,"rparen" ):"r32",
    (68 ,"comp" ):"r32",

    # 67 1
    (67 ,"rparen" ):"r31",
    (67 ,"comp" ):"s73",
    
    # 66 1
    (66 ,"rparen" ):"s72",
    
    # 65 1
    (65 ,"semi" ):"s71",

    #-=-==--=
    #64 4
    (64 ,"vtype" ):"r19",
    (64 ,"rbrace" ):"r19",
    (64 ,"class" ):"r19",
    (64 ,"$" ):"r19",

    # 63
    (63 ,"rparen" ):"r23",
    (63 ,"comma" ):"s43",

    #62
    (62 ,"semi" ):"s13",
    (62 ,"assign" ):"s15",

    #61
    (61 ,"boolstr" ):"s68",
    
    #60
    (60 ,"boolstr" ):"s68",

    #59
    (59 ,"vtype" ):"r27",
    (59 ,"id" ):"r27",
    (59 ,"rbrace" ):"r27",
    (59 ,"if" ):"r27",
    (59 ,"while" ):"r27",
    (59 ,"return" ):"r27",

    #58
    (58 ,"rbrace" ):"r24",
    (58 ,"return" ):"r24",

    #57
    (57 ,"id" ):"s28",
    (57 ,"literal" ):"s22",
    (57 ,"character" ):"s23",
    (57 ,"boolstr" ):"s24",
    (57 ,"lparen" ):"s27",
    (57 ,"num" ):"s29",

    #56
    (56 ,"rbrace" ):"s64",

    #55
    (55 ,"id" ):"s63",

    #54
    (54 ,"assign" ):"s15",




    # ====
    #53
    (53 ,"id" ):"s62",

    #52
    (52 ,"lparen" ):"s61",

    #51
    (51 ,"lparen" ):"s60",

    #50
    (50 ,"semi" ):"s59",
    # -=================   
    # 
    # 
    # 
    # 

    # 40 ~ 49
     
    (40,"rbrace") : "r38",


    (41,"vtype") : "s53",
    (41,"id") : "s54", 
    (41,"rbrace") : "r25", 
    (41,"if") : "s51", 
    (41,"while") : "s52", 
    (41,"return") : "r25",


    (42,"rparen") : "r20",


    (43,"vtype") : "s55",


    (44,"semi") : "r12", 
    (44,"rparen") : "r12",

    (45,"semi") : "r14", 
    (45,"addsub") : "r14", 
    (45,"rparen") : "r14",
    
    
    (46,"semi") : "r16", 
    (46,"addsub") : "r16", 
    (46,"multdiv") : "r16", 
    (46,"rparen") : "r16", 

    (47,"return") : "s57",

    (48,"vtype") : "s53", 
    (48,"id") : "s54", 
    (48,"rbrace") : "r25", 
    (48,"if") : "s51", 
    (48,"while") : "s52", 
    (48,"return") : "r25",

    (49,"vtype") : "r26", 
    (49,"id") : "r26", 
    (49,"rbrace") : "r26", 
    (49,"if") : "r26", 
    (49,"while") : "r26", 
    (49,"return") : "r26",


    #= ====

    (30,"rbrace") : "s38", 

    (31,"vtype") : "s5", 
    (31,"rbrace") : "r39", 

    (32,"vtype") : "s5", 
    (32,"rbrace") : "r39",

    (33,"lbrace") : "s41", 

    (34,"rparen") : "r23",
    (34,"comma") : "s43",

    (35,"id") : "s28",
    (35,"lparen") : "s27",
    (35,"num") : "s29",

    (36,"id") : "s28",
    (36,"lparen") : "s27",
    (36,"num") : "s29",

    (37,"rparen") : "s46", 

    (38,"vtype") : "r36", 
    (38,"class") : "r36", 
    (38,"$") : "r36",

    (39,"rbrace") : "r37",

    # ===========




    (0,"vtype") : "s5", (0,"class") : "s6", (0,"$") : "r4",
    (1,"$") : "acc",
    (2,"vtype") : "s5", (2,"class") : "s6", (2,"$") : "r4",
    (3,"vtype") : "s5", (3,"class") : "s6", (3,"$") : "r4",
    (4,"vtype") : "s5", (4,"class") : "s6", (4,"$") : "r4",
    (5,"id") : "s10",
    (6,"id") : "s12",
    (7,"$") : "r1",
    (8,"$") : "r2",
    (9,"$") : "r3",
    (10,"semi") : "s13", (10,"assign") : "s15", (10,"lparen") : "s14",


    (11,"semi") : "s16",
    (12,"lbrace") : "s17",
    (13,"vtype") : "r5", (13,"id") : "r5", (13,"rbrace") : "r5", (13,"if") : "r5", (13,"while") : "r5", (13,"return") : "r5", (13,"class") : "r5", (13,"$") : "r5",
    (14,"vtype") : "s19", (14,"rparen") : "r21",
    (15,"id") : "s28", (15,"literal") : "s22", (15,"character") : "s23", (15,"boolstr") : "s24", (15,"lparen") : "s27", (15,"num") : "s29",
    (16,"vtype") : "r6", (16,"id") : "r6", (16,"rbrace") : "r6", (16,"if") : "r6", (16,"while") : "r6", (16,"return") : "r6", (16,"class") : "r6", (16,"$") : "r6",
    (17,"vtype") : "s5", (17,"rbrace") : "r39", 
    (18,"rparen") : "s33", 
    (19,"id") : "s34", 
    (20,"semi") : "r7",


    (21,"semi") : "r8",
    (22,"semi") : "r9",
    (23,"semi") : "r10",
    (24,"semi") : "r11",
    (25,"semi") : "r13", (25,"addsub") : "s35", (25,"rparen") : "r13",
    (26,"semi") : "r15", (26,"addsub") : "r15", (26,"multdiv") : "s36", (26,"rparen") : "r15",
    (27,"id") : "s28", (27,"lparen") : "s27", (27,"num") : "s29",
    (28,"semi") : "r17", (28,"addsub") : "r17", (28,"multdiv") : "r17", (28,"rparen") : "r17",
    (29,"semi") : "r18", (29,"addsub") : "r18", (29,"multdiv") : "r18", (29,"rparen") : "r18"



}

def syntax(token):
    state = 0
    stack = [0] # with start state
    i = 0 #token 몇번째인지
    n = 2 # 몇번쨰 step
    while True:
        
        try:
            action = action_table.get((stack[-1], token[i])) # shift or reduce
            #print("action",action,stack[-1],token[i])
            
            if action[0] == 's': #shift
                stack.append(token[i])
                stack.append(int(action[1:]))
                #print(type(action[1:]))
                #print(stack)
                i+=1
                #print(n,stack)
                n+=1

            elif action[0] == 'r': #reduce
                after = after_reduce.get(action)
                #print("after",after)
                before = before_reduce.get(action) # 5
                #print("before",before)

                if before != ['']:
                    stack = stack[0: len(stack) - 2*len(before)] 
                
                stack.append(after) 
                #print(n,stack)
                n+=1
                goto = goto_table.get((stack[-2],stack[-1])) 
                stack.append(goto) 
                #print(n,stack)
                n+=1

            #print(stack)
            #print(i," : ",stack)    
            if action == 'acc':
                return True


        except:
            print("ERROR! error at {}th token; \"{}\"".format(i,token[i]))
            #print("ERROR! error at {}th token; \"{}\" can't be after \"{}\"".format(i,token[i],token[i-1]))
            return False


#main
if __name__ == "__main__":


    inputName = sys.argv[1] #print(inputName)
    f = open(inputName, 'r',encoding='UTF-8')

    mytoken = f.readline() # tokens 한줄로 읽고
    token = mytoken.split()
    token.append("$") # 코드의 끝
    #print(token)


    if token[0] not in ['vtype','class']:
        print("ERROR; need to be started with vtype or class")
       
    else:
        isAccessed = syntax(token)

        if isAccessed == True :
            print("access")
     



