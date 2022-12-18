import random 
input_file_path='/Users/sanjay.bedwal/Desktop/work/mask/xml_in.xml'
  
# Using readlines()
file1 = open(input_file_path, 'r')
lines = file1.readlines()
data=lines[0]
print(len(data))

lochar=[*data]
l=len(lochar)
final_str=''
value_started=False
i=-1
counter=0

for c in lochar:
    i=i+1
    if lochar[i-1]=='>' and lochar[i]!='<':
        value_started=True
    # </
    if i<l-2 and  lochar[i+1]=='<' and lochar[i+2]=='/':
        print('')
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

# print(final_str)
with open('xml_output.xml', 'w') as f:
    f.write(final_str)
    