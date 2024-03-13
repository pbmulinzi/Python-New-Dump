Weight = input('Weight:')
Unit = (input("(l)bs or (k)gs:"))
#1k = 2.20462l
#1l = 0.453592k
if Unit == 'l':
    k = float(Weight)/0.453592
    Kg = f'Weight in kgs, is {str(k)} Kgs'
    print(Kg)
elif Unit  == 'k':
    l = float(Weight)/2.20462
    lbs = f'Weight in lbs, is {str(l)} lbs'
    print(lbs)