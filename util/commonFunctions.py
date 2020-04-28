def setStyle(component, filename):
    file = open(filename, 'r')
    component.styleData = file.read()
    file.close()
    component.centralwidget.setStyleSheet(component.styleData)

def readPlayersBillsAddreses(filename):
    result=[]
    file=open(filename, 'r')
    playerBillsAddressesFromFile = file.readlines()
    for line in playerBillsAddressesFromFile:
        stringList = line.replace("\n","").split(" ")
        intList=[]
        for element in stringList:
            intList.append(int(element))
        result.append(intList)
    file.close()
    return result

def readCurrenLine(filename, lineNumber):
    file=open(filename, 'r', encoding='utf-8')
    allTasksList=file.readlines()
    allTasks=[]
    for line in allTasksList:
        allTasks.append(line.replace("\n", ""))
    file.close()
    return allTasks[lineNumber-1]