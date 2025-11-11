import sys
if len(sys.argv) ==4:
    script_name=sys.argv[0]
    principle=sys.argv[1]
    rate=sys.argv[2]
    time=sys.argv[3]
    print("user provided inputs")
else:
    script_name=sys.argv[0]
    principle="1000"
    rate="5"
    time="3"
    print("default inputs")
si=(int(principle)*float(rate)*int(time))/100
print("Script Name:",script_name)   
print("Principle Amount:",principle)
print("Rate of Interest:",rate)
print("Time (years):",time)
print("Simple Interest:",si)
