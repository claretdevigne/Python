from app import *

# Punto de acceso de la aplicación.
def main():
    while(True):
        title()
        mainAmount = amount()
        percentageVar = 0
        totalVar = 0
        tipVar = 0

        if mainAmount == "restart":
            continue
        elif mainAmount[0] == "ok": 
            while(True):
                title()
                percentages = definePercertages(mainAmount[1])
                if percentages[0] == "ok":
                    mainTotal = total(mainAmount[1], percentages)
                    while(True):
                        title()
                        showInfo(mainTotal)
                        totalTmp = totalPerDiner(mainTotal[0])
                        if totalTmp[0] == "ok":
                            title()
                            showInfo(mainTotal)
                            message(totalTmp)
                            restart()
                        elif totalTmp[0] == "error":
                            continue
                elif percentages[0] == "error":
                    continue
            
if __name__ == "__main__":
    main()