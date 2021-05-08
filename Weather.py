weather = [['Sunday'], ['Monday'], ['Tuesday'], ['Wensday'],

            ['Thursday'], ['Friday'], ['Satturday']]

lows = []
highs = []

def weather_forcast():
    l = 0
    h = 0

    while h != 7:
        high = int(input("Enter the highest temperatures for each day: "))
        addTemp = weather[h]
        addTemp.append(high)
        h += 1
    while l < 7:
        low = int(input("Enter the lowest temperatures for each day: "))
        addTemp = weather[l]
        addTemp.append(low)
        l += 1
def find_Peak(weather):

    i = 0
    high = 0
    while i < 7:
        if high < weather[i][1]:
            high = weather[i][1]
            day = i
        i += 1
    print("The peak happend ", weather[day][0])        
def first_dip(weather):
    prehigh = 0
    prelow = 0
    i = 0
    while i < 7:
        if prehigh > weather[i][1]:
            if prelow > weather[i][2]:
                print("Dip found in", weather[i][0])
                prehigh = weather[i][1]
                prelow = weather[i][2]
                i += 1
            else:
                print("No dip")
                prehigh = weather[i][1]
                prelow = weather[i][2]
                i += 1
        else:
            print("No dip")
            prehigh = weather[i][1]
            prelow = weather[i][2]
            i += 1

def main():
    weather_forcast()
    first_dip(weather)
    find_Peak(weather)

main()

