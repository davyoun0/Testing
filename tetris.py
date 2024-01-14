import eventBasedAnimation
import random
def playTetris():
    #15x10
    rows = 15
    cols = 10

    margin = 20
    cellSize = 10

    height = 15 * cellSize + 2 * margin
    width = 10 * cellSize + 2 * margin
    eventBasedAnimation.run(initFn = tetrisInit, drawFn = tetrisDrawFn, width = width,
                            height = height, rows=rows, cols=cols, margin=margin, keyFn = keyPressed, stepFn=stepFunction)

def tetrisInit(data):
    data.emptyColor = "Blue" # the cells without pieces are blue
    data.board = [([data.emptyColor] * data.cols) for row in range(data.rows)]
    data.tetrisPieces = tetrisPieces() #Get tetris pieces from the below function
    tetrisPieceColors = ["red", "yellow", "magenta", "pink","cyan","green","orange"]
    data.tetrisPieceColors = tetrisPieceColors
    newFallingPiece(data)
    data.isGameOver = False #Game is ended if this variable is True
    data.score = 0 #Iniial score is 0

# Choose a random piece from tetrisPieces
def newFallingPiece(data):
    data.newFallingPiece = random.choice(data.tetrisPieces) # pick one random piece from the list
    fallingPieceCols = len(data.newFallingPiece[0])
    data.newFallingColor = random.choice(data.tetrisPieceColors) #pick random Color
    data.fallingPieceRow = 0
    data.fallingPieceCol = (data.cols/2) - fallingPieceCols/2
    if islegal(data) == False:
        data.isGameOver = True
    else:
        data.isGameOver = False

# This function returns one of pieces
def tetrisPieces ():
    iPiece = [[True, True, True, True]]
    jPiece = [[True,False,False], [True,True,True]]
    lPiece = [[False,False,True], [True,True,True]]

    oPiece = [[True,True], [True,True]]

    sPiece = [[False,True,True],[True,True,False]]

    tPiece = [[False,True,False],[True,True,True]]

    zPiece = [[True,True,False], [False,True,True]]
    tetrisPieces = [iPiece,jPiece,lPiece,oPiece,sPiece,tPiece,zPiece]
    return tetrisPieces

def tetrisDrawFn(canvas, data):
    # we can draw something using canvas
    # canvas.create_rectangle(x-coordinate of left-corner, y-coordinate of left-corner)
    canvas.create_rectangle(0,0,data.width,data.height, fill ="#03FCFC")
    drawFallingPiece(canvas, data)
    tetrisDrawGrid(canvas,data)
    drawFallingPiece(canvas, data)
    drawScore(canvas,data)
    if data.isGameOver == True:
        canvas.create_text(data.width/2, data.height/2, text = "Game Over")

def tetrisDrawGrid(canvas,data):
    for rows in range(data.rows):
        for cols in range(data.cols):

            tetrisDrawCell(canvas,data,rows,cols,data.board[rows][cols])

def tetrisDrawCell(canvas, data, row, col, color):
    gridWidth = data.width - data.margin*2
    gridHeight = data.height - data.margin*2
    x0 = gridWidth * col / data.cols + data.margin
    y0 = gridHeight * row / data.rows + data.margin
    x1 = gridWidth * (col+1) / data.cols + data.margin
    y1 = gridHeight * (row+1) / data.rows + data.margin
    border = 1
    canvas.create_rectangle(x0,y0,x1,y1,fill = "black")
    canvas.create_rectangle(x0+border, y0+border, x1-border, y1-border,fill=color)

def drawFallingPiece(canvas, data):
    for row in range(len(data.newFallingPiece)):
        for col in range(len(data.newFallingPiece[0])):
            #checking the piece
            if data.newFallingPiece[row][col] == True:
                #if there is a piece on the box
                newrow = row + data.fallingPieceRow
                newcol = col + data.fallingPieceCol
                #take care of offset by adding row and col
                tetrisDrawCell(canvas, data, newrow, newcol , data.newFallingColor)
                # tetrisDrawCell(cavnas, data, newrow, newcol , "Yellow")
def drawScore(canvas,data):
    canvas.create_text(data.width/2, 10, text = "Socre:" +str(data.score))
    #displays the score on the top, center of the board

#Moving Part

def moveFallingPiece(data, drow, dcol):
    data.fallingPieceRow += drow
    data.fallingPieceCol += dcol
    #Step #2: make a function that will make blocks to stay within the grid
    if islegal(data) == False:
        data.fallingPieceRow -= drow
        data.fallingPieceCol -= dcol
        return False
    else:
        return True

def islegal(data):
    pieceRow = int(data.fallingPieceRow)
    pieceCol = int(data.fallingPieceCol)

    for row in range(len(data.newFallingPiece)):
        for col in range(len(data.newFallingPiece[0])):
            if ((pieceRow < 0 or pieceRow > data.rows - len(data.newFallingPiece)) or
                (pieceCol < 0 or pieceCol > data.cols - len(data.newFallingPiece[0]))):
                return False
            #anoter condition that checks if there is another block right below
            elif (data.board[pieceRow + row][pieceCol + col] != data.emptyColor):
                return False
    return True

def placeFallingPiece(data):
    for i in range(len(data.newFallingPiece)):
        for k in range(len(data.newFallingPiece[0])):
            if data.newFallingPiece[i][k] == True:
                newPieceRow = int(data.fallingPieceRow + i)
                newPieceCol = int(data.fallingPieceCol + k)
                data.board[newPieceRow][newPieceCol] = data.newFallingColor

def removeFullRows(data):
    newRow = data.rows - 1
    fullRows = 0 #counts the number of lines we are clearing
    for oldRow in range(data.rows-1, 0, -1): #Scanning from bottom to top
        if data.emptyColor in data.board[oldRow]: #If there is a row that have empty blocks
            for item in range(data.cols):
                data.board[newRow][item] = data.board[oldRow][item]
            newRow -= 1 #clears the line
        else:
            fullRows += 1

    for row in range(fullRows): #line clearing
        for col in range(len(data.board[0])):
            data.booard[row][col] = data.emptyColor #block

    data.score += fullRows ** 2
def stepFunction(data):
    #Step #1: make the blocks to fall down
    moveFallingPiece(data,1,0)
    if data.isGameOver == False: #while game is still running
        if moveFallingPiece(data,1,0) == False: #Block is on the ground
            #Step #3: make a function that will fix the location and fix colors for the previous block
            placeFallingPiece(data)
            newFallingPiece(data)
    removeFullRows(data)

#Rotating Blocks Part

def rotateFallingPiece(data):

    #We first need to store the old row and old col in case we need to undo the rotate
    #We then need to store the new row and new col wehre we want to rotate the new falling piece

    piecelist = data.newFallingPiece
    #piecelist is old piece

    locationRow = data.fallingPieceRow
    locationCol = data.fallingPieceCol

    #locationRow/Col is row/col of old piece

    dimensRow = len(data.newFallingPiece)
    dimensCol = len(data.newFallingPiece[0])

    #dimensrow/Col is amount of Row/Col in piece

    newDRow = len(data.newFallingPiece[0])
    newDCol = len(data.newFallingPiece)
    #newDrow / Col will be used for the rotating piece

    #Formulas for rotating blocks

    oldCRow, oldCCol = locationRow + dimensRow/2, locationCol + dimensCol/2
    #OldCROw, OldCCOl are old piece Row and Col

    newRow, newCol = oldCRow-newDRow/2, oldCCol - newDCol/2
    #newRow, newCol are new piece Row and Col

    sublist = []
    finalpiecelist = []

    for i in range(newDRow):
        for k in range(newDCol):
            item = piecelist[k][dimensCol -i -1] #rotate block 90 degrees
            sublist.append(item)
        finalpiecelist.append(sublist)
        sublist = []

    data.newFallingPiece = finalpiecelist
    data.fallingPieceRow = newRow
    data.fallingPieceCol = newCol

    #We need to check if rotating is valid

    if islegal(data) == False: #if rotating is not legal, undo the rotate
        data.newFallingPiece = piecelist #old piece
        data.fallingPieceRow, data.fallingPieceCol = locationRow, locationCol




def keyPressed(event, data):
    if event.keysym == "Left":
        moveFallingPiece(data,0,-1)
    if event.keysym == "Right":
        moveFallingPiece(data,0,1)
    if event.keysym == "Down":
        moveFallingPiece(data,1,0)
    if event.keysym == "Up":
        rotateFallingPiece(data)
    if event.keysym == "r":
        tetrisInit(data)
playTetris()

#next week
#create a function that tells user the game is over
#create a function that will move block left and right (key event)
#create a functiion that will remove the entire row and increase the score