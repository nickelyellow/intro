input=-5
result=0

if input==0:
    result=input
elif 0<input<10:
    result= input**2
elif input==10:
    result=input%3
elif 10<input<20:
    result=input/5
elif input==20:
    result=input*4
elif 20<input<=30:
    result=input+5
elif 30<input<40:
    result=input-8
elif 40<=input<50:
    result = (input%2)==0
# elif 50<=input and input!=100:
#     result=input
elif 50<=input<=150:
    result = input==100
elif input>150:
    result=(input+5)*8
else:
    print("LOL")

print(input)
print(result)