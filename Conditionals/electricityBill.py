electricity_unit=int(input("Enter the units consumed :"))
#units
if electricity_unit<=50:
    charge=electricity_unit*0.50
elif electricity_unit>50 and electricity_unit<=150:
    charge=25+(electricity_unit-50)*0.75
elif electricity_unit>150 and electricity_unit<=250:
    charge=75+(electricity_unit-150)*1.20
elif electricity_unit>250:
    charge=200+(electricity_unit-250)*1.5
#sub charge
subcharge=(0.2)*charge
#total charge
print(charge+subcharge)
