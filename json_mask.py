import random 
input_file_path='/Users/sanjay.bedwal/Desktop/work/mask/json_in.json'
  
# Using readlines()
file1 = open(input_file_path, 'r')
lines = file1.readlines()
data=lines[0]
# data=data.replace('": true', '": "true"') # need to print it as it is 
# data=data.replace('": false', '": "false"') # need to print it as it is 
# data=data.replace('null', '"null"') # need to print it as it is 
data=data.replace('\\"','') # removing reverse slash with qoutes ( it uses as a escape char)
data=data.replace('\\','')  # removing any extra reverse slash 


lochar=[*data]
final_str=''
value_started=False
i=-1
counter=0

for c in lochar:
    i=i+1
    # print(i)
    if i<=4:                       # need to generalise this
        final_str=final_str+c
        continue
    # if i==224:
    #     break
    if (lochar[i]=='t' and lochar[i+1]=='r' and lochar[i+2]=='u' and lochar[i+3]=='e') \
    or (lochar[i]=='n' and lochar[i+1]=='u' and lochar[i+2]=='l' and lochar[i+3]=='l'):
        counter=counter+1
        final_str=final_str+c
        if counter==4:
            counter=0
        continue
        
    if lochar[i]=='f' and lochar[i+1]=='a' and lochar[i+2]=='l' and lochar[i+3]=='s' and lochar[i+4]=='e':
        counter=counter+1
        final_str=final_str+c
        if counter==5:
            counter=0
        continue

    if i >4:
        if lochar[i-4]=='"' and lochar[i-3]==':' and lochar[i-2]==' ' and lochar[i-1]=='"'  \
        or lochar[i-4]==':' and lochar[i-3]==' ' and lochar[i-2]=='[' and lochar[i-1]=='"'  \
        or lochar[i-3]=='"' and lochar[i-2]==':' and lochar[i-1]==' ' and  (c.isalpha() or c.isdigit() or c=='-' )  :
            value_started=True
#{"director_number": ["D09590522"]}}]
#"ind_historical_average_delphi_score": ["043", "043", "043", "
        if i<len(lochar)-4 and  lochar[i]=='"' and lochar[i+1]==',' and lochar[i+2]==' ' and lochar[i+3]=='"'\
        or i<len(lochar)-4 and  lochar[i]=='}' and lochar[i+1]==',' and lochar[i+2]==' ' and lochar[i+3]=='"'\
        or i<len(lochar)-4 and  lochar[i]=='}' and lochar[i+1]==',' and lochar[i+2]==' ' and lochar[i+3]=='{'\
        or i<len(lochar)-4 and  lochar[i]==',' and lochar[i+1]==' ' and lochar[i+2]=='"' :
            value_started=False
        if value_started is True:
            if c.isalpha() :
                c=random.randint(97,122)
                encrypted_char=chr(c)
                final_str=final_str+encrypted_char
                continue
            if c.isdigit() :
                c=random.randint(49,57)
                encrypted_char=chr(c)
                final_str=final_str+encrypted_char
                continue
            final_str=final_str+c
            continue
        final_str=final_str+c

# print(final_str)
with open('output.json', 'w') as f:
    f.write(final_str)






    