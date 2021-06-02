

count = 0


#---------------------------------------------------------------------- בדיקת משקל

Height_val = float(input('please enter height in cm: '))
Weight = float(input('please enter weight in KG: '))
Height = float(Height_val)/100
BMI = float(Weight)/float(Height)**2
print('the BMI value is: ', BMI)

if BMI < 18.5:
    print('Underweight')

elif 18.5 > BMI >= 25:
    print('Normal value')

elif 25 > BMI >= 29:
    print('over-weight')

elif 30 > BMI >= 40:
    print('obesity')

elif BMI > 40:
    print('Acute obesity')



#---------------------------------------------------------------------- סיום בדיקת משקל


#fever = int(input('Do you have a fever? '))
#if fever != 1:
 #   print("")




#------------- תאי הדם הלבנים הכללית

age = int(input('please enter the age: '))
White_Blood_Cells = int(input('enter the value: '))


if White_Blood_Cells > 17500 and 0 <= age <= 3:
    print('High value! \n Check for heat. if so there is probably an infection.')
elif White_Blood_Cells < 6500 and 0 <= age <=3:
    print('low value! \n indicate viral disease, immune system failure and in very rare cases cancer.')

else:
    print('the values is OK!')


if White_Blood_Cells > 15500 and 4 <= age <= 17:
    print('High value! \n Check for heat. if so there is probably an infection.')
            
elif White_Blood_Cells < 6500 and 4 <= age <= 17:
    print('low value! \n indicate viral disease, immune system failure and in very rare cases cancer.')
           
else:
    print('the values is OK!')
                

if White_Blood_Cells > 17500 and 18 <= age <= 99:
    print('High value! \n Check for heat. if so there is probably an infection.')

elif White_Blood_Cells < 6500 and 18 <= age <= 99:
    print('low value! \n indicate viral disease, immune system failure and in very rare cases cancer.')

else:
    print('the values is OK!')

#--------------- סיום בדיקת תאי הדם הלבנים 



"""""

#-------------כמות תאי הדם הלבנים האחראים בעיקר על חיסול החיידקים 


Neutrophil = range(0.28, 0.54)

Neutrophil = input('input value: ')

Neutrophil = Neutrophil * White_Blood_Cells

neutrophil_value = input('enter neutrophil value: ')

if neutrophil_value < Neutrophil:
    print('Values are invalid! Check if there is a problem with the formation of blood cells!')

if neutrophil_value > Neutrophil:
    print('Values are invalid! Check if it is a prolonged bacterial infection or lymphoma cancer.')

 else:
        print('the values is OK!')


#----------- סיום כמות תאי הדם הלבנים האחראים בעיקר על חיסול החיידקים

#------------------בדיקת כדוריות הדם האדומות

Red_Blood_Cells = range(4.5, 6)

Red_Blood_Cells_value = input('please enter Red Blood Cells value: ')
if Red_Blood_Cells_value < Red_Blood_Cells:
    print('Values are invalid! Check for anemia or severe bleeding.')

if Red_Blood_Cells_value > Red_Blood_Cells:
    print('Values are invalid! /n If he does not smoke or has a lung disease /n check for a disorder in the blood production system.')

 else:
        print('the values is OK!')

#------------- סיום כדוריות אדומות 



#--------- נפח כדוריות הדם האדומות 



HCT_women = range(0.33, 0.47)

HCT_women = HCT_women * Red_Blood_Cells

HCT_women_value = input('enter HCT value for a women: ')

if HCT_women_value * Red_Blood_Cells_value > HCT_women:
    print('High value, normal in a smoker')

if HCT_women_value * Red_Blood_Cells_value < HCT_women:
    print('Low value, check for bleeding or anemia')


HCT_men = range(0.37, 0.54)

HCT_men = HCT_men * Red_Blood_Cells

HCT_men_value = input('enter HCT value for a men: ')

if HCT_women_value * Red_Blood_Cells_value > HCT_men:
    print('High value, normal in a smoker')

if HCT_women_value * Red_Blood_Cells_value < HCT_men:
    print('Low value, check for bleeding or anemia')

else:
        print('the values is OK!')


#-------- סיום בדיקת נפח כדוריות הדם האדומות 


#-----רמות השתנן בדם 



urea_value: int  = int(input('please enter urea value: '))
for Urea in range(17, 44):

    if urea_value > Urea :
        print('High value!\n Check for kidney disease, dehydration or a high-protein diet.')

    if urea_value < Urea :
        print('low value! If it is not pregnancy check for malnutrition, low protein diet or liver disease.')

 else:
        print('the values is OK!')


#-------------סיום בדיקת השיינן 





#--------המוגלובין 



Hemoglobin_Women_Value = int(input('please enter value:'))

for Hemoglobin_Women in range(12, 16) :
    if Hemoglobin_Women_Value < Hemoglobin_Women :
        print('Low value!\n indicates anemia.\n  This can be due to a hematologic disorder, iron deficiency and bleeding.')

    else:
        print('the values is OK!')


Hemoglobin_men_Value = int(input('please enter value:'))

for Hemoglobin_men in range(12, 18):
    if Hemoglobin_men_Value < Hemoglobin_men:
        print('Low value!\n indicates anemia.\n  This can be due to a hematologic disorder, iron deficiency and bleeding.')

    else:
        print('the values is OK!')

Hemoglobin_children_Value = float(input('please enter value:'))

for Hemoglobin_children in range(11.5, 15.5) :
    if Hemoglobin_children_Value < Hemoglobin_children :
        print('Low value!\n indicates anemia.\n  This can be due to a hematologic disorder, iron deficiency and bleeding.')

    else:
        print('the values is OK!')



#------------ סיום בדיקת ההומולוגבין




#-------------בדיקת קריאטאינין

Creatinine_baby_Value = float(input('please enter value:'))  #תינוקות מגילאים 0-2
for Creatinine_baby in range(0.2, 0.5):
    if Creatinine_baby_Value > Creatinine_baby:
        print('High value!\n Check for diarrhea and vomiting\n if not,they may indicate a kidney problem and in severe cases kidney failure. Muscle diseases and increased consumption of meat.')

    if Creatinine_baby_Value < Creatinine_baby:
        print('low value! \n Check if the patient is malnourished and does not need enough protein.')
    else:
        print('the values is OK!')



Creatinine_Children_Value = float(input('please enter value:'))  # ילדים מגילאים 3-17
for Creatinine_Children in range(0.5, 1):
    if Creatinine_Children_Value > Creatinine_Children:
        print('High value!\n Check for diarrhea and vomiting\n if not,they may indicate a kidney problem and in severe cases kidney failure. Muscle diseases and increased consumption of meat.')

    if Creatinine_Children_Value < Creatinine_Children:
        print('low value! \n Check if the patient is malnourished and does not need enough protein.')
    else:
        print('the values is OK!')



Creatinine_Adults_Value = float(input('please enter value:')) # מבוגרים מגיל 18 - 59
for Creatinine_Adults in range(0.6, 1):
    if Creatinine_Children_Value > Creatinine_Adults:
        print('High value!\n Check for diarrhea and vomiting\n if not,they may indicate a kidney problem and in severe cases kidney failure. Muscle diseases and increased consumption of meat.')

    if Creatinine_Adults_Value < Creatinine_Adults:
        print('low value! \n Check if the patient is malnourished and does not need enough protein.')
    else:
        print('the values is OK!')



Creatinine_Elderly_Value = float(input('please enter value:')) # קשישים מגיל 60+
for Creatinine_Elderly in range(0.6, 1.2):
    if Creatinine_Elderly_Value > Creatinine_Elderly:
        print('High value!\n Check for diarrhea and vomiting\n if not,they may indicate a kidney problem and in severe cases kidney failure. Muscle diseases and increased consumption of meat.')

    if Creatinine_Elderly_Value < Creatinine_Elderly:
        print('low value! \n Check if the patient is malnourished and does not need enough protein.')
    else:
        print('the values is OK!')

#----------- סיום בדיקת קריאטנין



#-----------בדיקת ברזל


iron_value = int(input('please enter value: '))

for Iron in range(60 , 160):
    if iron_value > Iron:
        print('High value!\n Check for iron poisoning')
    if iron_value < Iron:
        print('Low value! indicates inadequate nutrition or blood loss due to bleeding')
    else:
        print('the values is OK!')


iron_Women_value = int(input('please enter value: '))

for Iron_Women in range(46 , 128):

    if iron_Women_value > Iron_Women:
        print('High value!\n Check for iron poisoning')
    if iron_Women_value < Iron_Women:
        print('Low value! Check Is pregnant \n if not, \n indicates inadequate nutrition or blood loss due to bleeding.')
    else:
        print('the values is OK!')

#--------סיום בדיקת ברזל 


#---------בדיקת כולסטרול


# להוסיף מוצא אתיופי
High_Density_Lipoprotein_Men_val = int(input('please enter value: '))

for High_Density_Lipoprotein_Men in range(29, 62):

    if High_Density_Lipoprotein_Men_val > High_Density_Lipoprotein_Men:
        print('High value!\n it is recommended to increase physical activity in order to raise the "good" cholesterol levels')

    if High_Density_Lipoprotein_Men_val < High_Density_Lipoprotein_Men:
        print('High value!\n it is recommended to increase physical activity in order to raise the "good" cholesterol levels')
    else:
        print('the values is OK!')


High_Density_Lipoprotein_Women_val = int(input('please enter value: '))

for High_Density_Lipoprotein_Women in range(34, 82):

    if High_Density_Lipoprotein_Women_val > High_Density_Lipoprotein_Women:
        print('High value!\n it is recommended to increase physical activity in order to raise the "good" cholesterol levels')

    if High_Density_Lipoprotein_Women_val < High_Density_Lipoprotein_Women:
        print('High value!\n it is recommended to increase physical activity in order to raise the "good" cholesterol levels')

    else:
        print('the values is OK!')


#-----------סיום בדיקת כולסטרול




#---------פוספטזה אלקלית

Alkaline_Phosphatase_Easterners_val = int(input('please enter value: '))

for Alkaline_Phosphatase in range(60, 120):

    if Alkaline_Phosphatase_Easterners_val > Alkaline_Phosphatase:
        print('high levels!\n May indicate liver disease, biliary tract disease, pregnancy, hypothyroidism or use of various medications.')

    if Alkaline_Phosphatase_Easterners_val < Alkaline_Phosphatase:
        print('Low levels! May indicate a poor diet that lacks protein. Deficiency in vitamins like vitamin B12, vitamin C, vitamin B6, folic acid.')

    else:
        print('the values is OK!')



Alkaline_Phosphatase_Another_population_val = int(input('please enter value: '))

for Alkaline_Phosphatase_Another_population in range(30, 90):

    if Alkaline_Phosphatase_Another_population_val > Alkaline_Phosphatase_Another_population:
        print('high levels!\n May indicate liver disease, biliary tract disease, pregnancy, hypothyroidism or use of various medications.')

    if Alkaline_Phosphatase_Another_population_val < Alkaline_Phosphatase_Another_population:
        print('Low levels! May indicate a poor diet that lacks protein. Deficiency in vitamins like vitamin B12, vitamin C, vitamin B6, folic acid.')

    else:
        print('the values is OK!')"""


#סיום בדיקה פוספטזה אלקלית-----------------------

