test1 = int(input('enter the score for Test1 : '))
gpa1 = int(input('enter cradit hour for this subject:'))
test2 = int(input('enter the score for test2 : '))
gpa2 = int(input('enter cradit hour for this subject:'))
test3 = int(input('enter the score for test3 : '))
gpa3 = int(input('enter cradit hour for this subject:'))
test4 = int(input('enter the score for test4: '))
gpa4 = int(input('enter cradit hour for this subject:'))
test5 = int(input('enter the score for test5: '))
gpa5 = int(input('enter cradit hour for this subject:'))
test6 = int(input('enter the score for test6: '))
gpa6 = int(input('enter cradit hour for this subject:'))
CH=int(input('enter total credit hour: '))
gpa=(test1*gpa1+test2*gpa2+test3*gpa3+test4*gpa4+test5*gpa5+test6*gpa6) /CH
print ('your GPA is in this semester is ', gpa)
if gpa >= 91:
    print('4.0 GPA and A+ grade')
    print('Outstsnding!')
elif gpa>=87:
    print('4.0 GPA and A grade')
elif gpa>=80:
    print('3.5 GPA and B+ garde')
elif gpa>=72:
    print('3.0 GPA and B garde')
elif gpa>=66:
    print('2.5 GPA and C+ garde') 
elif gpa>=60:
    print('2.0 GPA and C garde')
else:
    print('you are have GPA Below than 60')
    print('you are failed in this semester')

