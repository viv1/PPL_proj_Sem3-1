import re

def main():
    
    op="OPERATOR"
    dt="DATA TYPE"
    rk="RESERVED KEYWORD"
    lit="LITERAL"
    sg="STRING LITERAL"
    cmt="COMMENT"
    dl="DELIMITER"
    sep="SEPARATOR"
    iden="IDENTIFIER"
    #use above later ..//TAKEN CARE

    # == and =  //TAKEN CARE
    # 50 and 0  //TAKEN CARE

    Types={'#':op,'"':op,"true":rk,"false":rk,'Shirt':dt,"Jeans":dt,"Kurta":dt,"Frock":dt,"Button":dt,
           "Pocket":dt,"Collar":dt,"Sleeve":dt,"Zip":dt,"Frill":dt,
           "Emb":dt,"Size":dt,"Color":dt,"Univ":dt,"double":dt,
           "bool":dt,"List":dt,"Array":dt,"String":dt,"for each":rk,
           "try":rk,"catch":rk,"if":rk,"else":rk,
           "INF":rk,"begin":rk,"end":rk,"break":rk,
           "->":op,"==":op,"{":sep,"}":sep,"[":sep,"]":sep,";":dl,
           "&&":op,"!":op,"%":op,"<>":op,"^^\n":op,"|||":op,"~":op,
           "+":op,"*":op,"(":sep,")":sep,",":dl,"-":op,":":op,
           "||":op,"^^":op,"=":op,"in":rk}

    ambi_op=["-","||","^^","=","in"]
    inpfile=input("Enter file name: ")       #code1.txt or code2.txt or code3.txt or code4.txt
    with open(inpfile,encoding="utf8") as f:
        p=0
        for line in f:
            print("*****************line no."+str(p+1)+" **************")
            print(line)
            p=p+1
            com=re.findall(r'#.+',line)         # comments
            strin=re.findall(r'".*"',line)      # strings
            
            for c in com:
                comment_val=c[1:]           #extract comment
            for s in strin:
                string_val=s[1:-1]          #extract string

            if com:            
                line=line.split('#')              #to separate comments
                line="".join(line[0:-1]+list('#'))
                #print(line)
            if strin:
                line=line.split('"')              #to separate strings
                line="".join(line[0]+'"'+line[2])
                #print(line)
            #print(comment_val)
            #print(string_val)
            #print(list(line))
            
    ###########################################
            li=list(line)                   #sting="
            k=0
            hin=False
            for i in range(0,len(li)):
                while i<k :                 #to skip to i=k
                    i=i+1
                    continue
                #if(hin):
                 #  i=k
                  # hin=True            
               
                for j in range(i,len(li)):
                    
                    nl=li[i:j+1]
                    st="".join(nl)
                    if st in Types:
                        #print(st)
                        if st not in ambi_op:
                            print(st+"      "+Types[st])
                            if st=='#':
                                print(comment_val+"      "+cmt)
                            if(st=='"'):
                                print(string_val + "      "+sg)
                                print(st+"      "+Types[st])
                            k=j+1
                            #hin=True
                            break
                        else:
                            nl=li[i:j+2]
                            st1="".join(nl)
                        
                            if st1=="==" or st1=="->" or st1=="int" or st1=="in:" or st1=="|||"  or st1=="^^\n":
                                if st1=="in:":
                                    pass
                                else:
                                    print(st1+"      "+op)
                                k=j+2
                             #   hin=True
                                break
                            elif st1=="ing" or st1==":e" or st1==":\s":
                                k=j+2
                                break;
                                
                            else:
                                if st=="in":
                                    print(st+"      "+rk)
                                else:                                
                                    print(st+ "      "+op)
                                k=j+1
                              #  hin=True
                                break

                    #elif size:
                     #       si="".join(size)
                      #      si=re.sub('%',"",si)
                            
                       #     print(si)
                        #    k=j+1
                      #      print("".join(si[1:3])+"   "+rk)
                         #   break;
                    else:
                        #print(st)
                        var=re.findall(r'\$[\w]+',line)     #variable(identifiers)
                        oper=re.findall(r'@[\w]+',line)     #  @ operators
                        cons=re.findall(r'[0-9]+',line)     #constants
                        size=re.findall(r'%\s*[sSmMlL]\s*[%;]',line)    #shirt sizes
                        #print(size)
                        
                        if st in var:
                            print(st+ "      "+iden)
                            k=j+1
                            #hin=True
                            break
                        if st in oper:
                            print(st+ "      "+op)
                            k=j+1
                            #hin=True
                            break
                        if st in cons:
                            
                            print(st+ "      "+lit)
                            k=j+1
                            #maxchar=max(cons)
                            #kon=0;
                            #maxchar=int(maxchar)/10
                            #while int(maxchar) >= 1:
                            #    kon=kon+1
                            #k=j+kon
                            #hin=True
                            break
                        #print(size)
                        #print(st)
                        if size:
                            #print(st)
                            if st=='m' or st=='M' or st=='s' or st=='S' or st=='l' or st=='L':
                                print(st+ "      " +rk)
                                k=j+1
                                break;


    print()
    print()
    rop=input("Press any key to exit")

main()
