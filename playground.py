#!/usr/bin/python3
#------------------------------------------------------------------------------
# Python 3.4.3
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# includes
#------------------------------------------------------------------------------
import os
import sys 
#------------------------------------------------------------------------------
# definitions
#------------------------------------------------------------------------------
lineLength       = 11
lineCnt          = 11
sign_non         = '.'
sign_space       = 'o'
sign_rampL       = 'L'
sign_rampR       = 'R'
sign_crossover   = 'X'
sign_bitL        = '<'
sign_bitR        = '>'
sign_interceptor = '-'
sign_gear        = '*'
sign_gearBitL    = '('
sign_gearBitR    = ')'
#------------------------------------------------------------------------------
# classes
#------------------------------------------------------------------------------
class Ball :
  ballOldPosX = 0
  ballOldPosY = 0
  ballActPosX = 0
  ballActPosY = 0
  ballColor = 'b'
  def __init__(self,x,y,comesFrom = 'r',ballColor = 'b') :
    self.setNewPos(x,y)
    self.ballColor = ballColor
    if comesFrom == 'r' :
      self.ballOldPosX = lineLength
  def setNewPos(self,x,y) :
    self.ballOldPosX = self.ballActPosX
    self.ballOldPosY = self.ballActPosY
    self.ballActPosX = x
    self.ballActPosY = y
  def nextD(self) :
    self.setNewPos(self.ballActPosX,self.ballActPosY+1)
  def nextLD(self) :
    self.setNewPos(self.ballActPosX-1,self.ballActPosY+1)
  def nextRD(self) :
    self.setNewPos(self.ballActPosX+1,self.ballActPosY+1)
  def wasL(self) :
    if self.ballOldPosX < self.ballActPosX :
      return True
    else :
      return False
  def isSame(self,ballPos) :
    if self.ballActPosX == ballPos.ballActPosX : 
      if self.ballActPosY == ballPos.ballActPosY :
        return True
    return False
  def printIt(self) :
    print("X:",self.ballActPosX," Y:",self.ballActPosY)
  def printItAll(self) :
    print("Xa:",self.ballActPosX," Ya:",self.ballActPosY)
    print("Xo:",self.ballOldPosX," Yo:",self.ballOldPosY)
    if True == self.wasL() :
      print("from left")
    else :
      print("from right")
    print("color ",self.ballColor)
  def getX(self) :
    return self.ballActPosX
  def getY(self) :
    return self.ballActPosY
  def getColor(self) :
    return self.ballColor
#------------------------------------------------------------------------------
class ConnectedGears :
  gearList = []
  def __init__(self,gearList) :
    self.gearList = gearList
  def getGearList(self) :
    return self.gearList
#------------------------------------------------------------------------------
# functions
#------------------------------------------------------------------------------
def getBallList(text, right) :
  liste = []
  siteSign = 'l'
  if ( True == right ) :
    siteSign = 'r'  
  for sign in text :
    if ( sign == 'b' ) :
      liste.append( Ball(3,0,siteSign,'b') )
    else :
      liste.append( Ball(3,0,siteSign,'r') )    
  return liste
#------------------------------------------------------------------------------
def genBallList(red,right,num) :
  liste = []
  ballColor = 'b'
  if ( True == red ) :
    ballColor = 'r'  
  siteSign = 'l'
  if ( True == right ) :
    siteSign = 'r'  
  for x in range(num) :
    liste.append( Ball(3,0,siteSign,ballColor) )
  return liste  
#------------------------------------------------------------------------------
def getFilenameParameter() :
  datName = ""
  site = True
  numBalls = 1
  leftBalls = []
  rightBalls = []
  lastNr = 3;
  if len(sys.argv) > 1 :
    datName = sys.argv[1]
  if len(sys.argv) > 2 :
    if ( True == sys.argv[2].isnumeric() ) :
      numBalls = int(sys.argv[2])
      leftBalls = genBallList(False,False,numBalls)
      rightBalls = genBallList(True,True,numBalls)
    else :
      lastNr = lastNr + 1
      if len(sys.argv) > 3 :
        leftBalls  = getBallList(sys.argv[2],False)
        rightBalls = getBallList(sys.argv[3],True)    
      else :
        print ("need left and right definition" )
  if len(sys.argv) > lastNr :
    site = False
    print("begin right")
  if len(sys.argv) == 1 :
    print("# Usage:", sys.argv[0], " <PlayGround Filename> [<number Balls>] [Right]");
    printPlayground()
    print("#")
    print("# Non            ",sign_non)
    print("# Space          ",sign_space)
    print("# Ramp Left      ",sign_rampL)
    print("# Ramp Right     ",sign_rampR)
    print("# Crossover      ",sign_crossover)
    print("# Bit Left       ",sign_bitL)
    print("# Bit Right      ",sign_bitR)
    print("# Interceptor    ",sign_interceptor)
    print("# Gear           ",sign_gear)
    print("# Gear Bit Left  ",sign_gearBitL)
    print("# Gear Bit Right ",sign_gearBitR)
    exit()
  return (datName,leftBalls,rightBalls,site)
#------------------------------------------------------------------------------
def loadPlayGround(playgroundName) :
  if os.path.isfile(playgroundName) == False :
    print("File:", playgroundName, " doesnt exist");
    exit() 
  fnDatei = open(playgroundName,"r")
  playliste = []
  for line in fnDatei :
    line = line.strip()
    if 0 < len( line ) :
      if line[0] != '#' :
        playliste.append(line)
  fnDatei.close()
  return playliste
#------------------------------------------------------------------------------
def checkSignPosition(actSign,posX,posY) :
  countPos = posY * lineLength + posX
  # gears could have all positions
  if actSign != sign_gear :
    if actSign == sign_non :
      if countPos % 2 == 1 :
        return False   
  return True
#------------------------------------------------------------------------------
def printPlayground() :
  for y in range(lineCnt) :
    for x in range(lineLength) :
      countPos = y * lineLength + x
      if countPos % 2 == 0 :
        print(sign_non, end = '')
      else :
        print(sign_space, end = '')
    print()
#------------------------------------------------------------------------------
def checkPlayGround(playliste) :
  signs = [ sign_non, 
            sign_space, 
            sign_rampL, 
            sign_rampR, 
            sign_crossover,
            sign_bitL,
            sign_bitR,
            sign_interceptor,
            sign_gear,
            sign_gearBitL,
            sign_gearBitR]
  for y in range(len(playliste)) :
    actLine = playliste[y]
    if lineLength != len(actLine) :
      print(y," len", len(actLine), "doesnt equal ",lineLength)
      exit()
    for x in range(len(actLine)) :
      actSign = actLine[x]
      if actSign not in signs :
        print("sign",actSign,"not in signs")
        exit()
      if checkSignPosition(actSign,x,y) == False:
        print("Wrong Sign Position x",x," y",y)
        exit()
#------------------------------------------------------------------------------
def printPlayGround(playliste) :
  for x in range(len(playliste)) :
    print(x,":\t", end = '')
    for sign in playliste[x] :
      print(sign, end = '')
    print()
#------------------------------------------------------------------------------
def printPlayGroundWithBall(playliste,playball) :
  for x in range(len(playliste)) :
    if x == playball.ballActPosY :
      print(x,":\t", end = '')
      for y in range(len(playliste[x])) :
        if y == playball.ballActPosX :
          if playball.getColor() == 'b' :
            print("b", end = '')
          else :
            print("r", end = '')
        else :
          print(" ", end = '')
      print()
    print(x,":\t", end = '')
    for sign in playliste[x] :
      print(sign, end = '')
    print()
#------------------------------------------------------------------------------
def printPlayGroundWithBallInside(playliste,playball, lineNr = False) :
  for y in range(len(playliste)) :
    if lineNr :
      print(y,":\t", end = '')
    line = playliste[y]
    for x in range(len(line)) :
      if y == playball.ballActPosY and \
         x == playball.ballActPosX :
        if playball.getColor() == 'b' :
          print("b", end = '')
        else :
          print("r", end = '')
      else :  
        print(line[x], end = '')
    print()
#------------------------------------------------------------------------------
def getSign(playliste,playball) :
  actSign = ""
  if playball.ballActPosY < len(playliste)  and 0 <= playball.ballActPosY :
    line = playliste[playball.ballActPosY]
    if playball.ballActPosX < len(line) and 0 <= playball.ballActPosX :
      actSign = line[playball.ballActPosX]
  return actSign
#------------------------------------------------------------------------------
def setSign(playliste,playball, sign) :
  if playball.ballActPosY < len(playliste) and 0 <= playball.ballActPosY :
    line = playliste[playball.ballActPosY]
    if playball.ballActPosX < len(line) and 0 <= playball.ballActPosX :
      posX = 0
      newLine = []
      for i in line :
        if posX == playball.ballActPosX :
          newLine.append(sign)
        else :
          newLine.append(line[posX])
        posX = posX + 1
    playliste[playball.ballActPosY] = newLine
#------------------------------------------------------------------------------
def singleStep(playliste,playball,ConnectedGearsList) :
  actSign = getSign(playliste,playball)
  if   actSign == sign_non :
    playball.nextD()
  elif actSign == sign_space :
    playball.nextD()
  elif actSign == sign_rampL :
    playball.nextLD()
  elif actSign == sign_rampR :
    playball.nextRD()
  elif actSign == sign_crossover :
    if playball.wasL() :
      playball.nextRD()
    else :
      playball.nextLD()
  elif actSign == sign_bitL :
    setSign(playliste,playball,sign_bitR)
    playball.nextRD()
  elif actSign == sign_bitR :
    setSign(playliste,playball,sign_bitL)
    playball.nextLD()
  elif actSign == sign_interceptor :
    return False
  elif actSign == sign_gear :
    playball.nextD()
  elif actSign == sign_gearBitL :
    gearList = getConnectedGearListInBall(ConnectedGearsList,playball)
    changePlaylistGears(playliste,gearList)
    playball.nextRD()
  elif actSign == sign_gearBitR :
    gearList = getConnectedGearListInBall(ConnectedGearsList,playball)
    changePlaylistGears(playliste,gearList)
    playball.nextLD()
  else :
    playball.nextD()
  return True
#------------------------------------------------------------------------------
# gears and gearBits
#------------------------------------------------------------------------------
def printBallList(ballList) :
  for x in range(len(ballList)) :
    ballList[x].printIt()
#------------------------------------------------------------------------------
def isBallInTheList(ballList,ball) :
  for elemBall in ballList :
    if elemBall.isSame(ball) : 
      return True
  return False
#------------------------------------------------------------------------------
def connectLists(listeA,ListeB) :
  nextList = listeA
  for elemBall in ListeB :    
    nextList.append(elemBall)
  return nextList
#------------------------------------------------------------------------------
def getConnectedGears(playliste,actBallPos,connectedList) :
  actConnection = []
  actSign = getSign(playliste,actBallPos)

  if False == isBallInTheList(connectedList,actBallPos) :
    actConnection.append(actBallPos)

  if sign_gearBitL == actSign or \
     sign_gearBitR == actSign or \
     sign_gear == actSign :
    upPos = Ball(actBallPos.getX(),actBallPos.getY()-1)
    upSign = getSign(playliste,upPos)
    if sign_gearBitL == upSign or \
       sign_gearBitR == upSign or \
       sign_gear == upSign :
      if False == isBallInTheList(connectedList,upPos) :
        actConnection.append(upPos)

    downPos = Ball(actBallPos.getX(),actBallPos.getY()+1)
    downSign = getSign(playliste,downPos)
    if sign_gearBitL == downSign or \
       sign_gearBitR == downSign or \
       sign_gear == downSign :
      if False == isBallInTheList(connectedList,downPos) :
        actConnection.append(downPos)

    leftPos = Ball(actBallPos.getX()-1,actBallPos.getY())
    leftSign = getSign(playliste,leftPos)
    if sign_gearBitL == leftSign or \
       sign_gearBitR == leftSign or \
       sign_gear == leftSign :
      if False == isBallInTheList(connectedList,leftPos) :
        actConnection.append(leftPos)

    rightPos = Ball(actBallPos.getX()+1,actBallPos.getY())
    rightSign = getSign(playliste,rightPos)
    if sign_gearBitL == rightSign or \
       sign_gearBitR == rightSign or \
       sign_gear == rightSign :
      if False == isBallInTheList(connectedList,rightPos) :
        actConnection.append(rightPos)

  return actConnection
#------------------------------------------------------------------------------
def getConnectedGearList(playliste,actBallPos,connectedList) :
  actConnected = getConnectedGears(playliste,actBallPos,connectedList)
  connectedList = connectLists(connectedList,actConnected)
  for elemBall in actConnected :
    getConnectedGearList(playliste,elemBall,connectedList)
  return connectedList
#------------------------------------------------------------------------------
def isInConnectedGearsList(ConnectedGearsList,playball) :
  for connGears in ConnectedGearsList :
    actGearList = connGears.getGearList()
    if True == isBallInTheList(actGearList,playball) :
      return True    
  return False
#------------------------------------------------------------------------------
def getConnectedGearsList(playliste) :
  ConnectedGearsList = []
  for y in range(len(playliste)) :
    actLine = playliste[y]
    for x in range(len(actLine)) :
      actSign = actLine[x]
      if sign_gearBitL == actSign or \
         sign_gearBitR == actSign or \
         sign_gear == actSign :
        playball = Ball(x,y)
        if False == isInConnectedGearsList(ConnectedGearsList,playball) :
          connectedList = getConnectedGearList(playliste,playball,[])
          ConnectedGearsList.append(ConnectedGears(connectedList))
  return ConnectedGearsList
#------------------------------------------------------------------------------
def getConnectedGearListInBall(ConnectedGearsList,playball) :
  actGearList = []
  for connGears in ConnectedGearsList :
    actGearList = connGears.getGearList()
    if True == isBallInTheList(actGearList,playball) :
      return actGearList
  return actGearList
#------------------------------------------------------------------------------
def printGearLists(ConnectedGearsList) :
  for connGears in ConnectedGearsList :
    printBallList(connGears.getGearList())
    print()
#------------------------------------------------------------------------------
def changePlaylistGears(playliste,gearList) :
  for actBall in gearList :
    actSign = getSign(playliste,actBall)
    if actSign == sign_gearBitL :
      setSign(playliste,actBall,sign_gearBitR)
    elif actSign == sign_gearBitR :
      setSign(playliste,actBall,sign_gearBitL)
#------------------------------------------------------------------------------
def printBallResultList(playBallResults) :
  revList = playBallResults[::-1]
  for playBall in revList :
    print(playBall.getColor(),end = '')
  print()
#------------------------------------------------------------------------------
# main
#------------------------------------------------------------------------------
def main() :
  (datName,leftBalls,righBalls,site) = getFilenameParameter()
  playliste = loadPlayGround(datName)
  checkPlayGround(playliste)

  ConnectedGearsList = getConnectedGearsList(playliste)
  playBallResults = []

  if True == site :
    playBall = leftBalls.pop(0)
  else :
    playBall = righBalls.pop(0)

  while playBall != None   :
    storeBall = False
    while playBall.getY() < lineCnt :
      printPlayGroundWithBallInside(playliste,playBall)
      if False == singleStep(playliste,playBall,ConnectedGearsList) :
        print("Stopp",playBall.getColor())
        printBallResultList(playBallResults)
        exit() 
      else :
        storeBall = True
      print()
    if storeBall :
      playBallResults.append(playBall)
      if playBall.getX() < lineLength/2 :
        playBall = None
        if 0 < len (leftBalls) :
          playBall = leftBalls.pop(0)
        else :
          playBall = None
      else :
        if 0 < len (righBalls) :
          playBall = righBalls.pop(0)
        else :
          playBall = None
      printBallResultList(playBallResults)
      print()
#------------------------------------------------------------------------------
# start
#------------------------------------------------------------------------------
main()
#------------------------------------------------------------------------------


