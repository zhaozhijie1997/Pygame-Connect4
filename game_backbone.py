


import numpy as np
import pygame
import sys
import math

ROW_COUNT = 6
COL_COUNT = 7
SQUARESIZE = 100
class Connect4:
    def __init__(self):
        self.ROW_COUNT = 6
        self.COL_COUNT = 7
        self.turn = 0
        self.game_over = False
        self.board = None
        self.SQUARESIZE = 100
        self.width = self.COL_COUNT * self.SQUARESIZE
        self.height = (self.ROW_COUNT + 1) * self.SQUARESIZE
        self.BLUE = (0,0,255)
        self.BLACK = (0,0,0)
        self.size = (self.width,self.height)
        self.radius = int(self.SQUARESIZE/2-5)
        self.player1_color = (255,0,0)
        self.player2_color = (0,255,0)
        self.font = pygame.font.SysFont('monospace',75)
        
        
    def create_board(self):
        self.board = np.zeros((6,7),dtype = int)
        return self.board

    def check_columns(self,col):
        return self.board[0][col] == 0
    
    def open_row(self,col):
        for r in range(self.ROW_COUNT):
            if self.board[self.ROW_COUNT-1-r][col] == 0:
                return (self.ROW_COUNT-1-r)         
        
    def drop_piece(self,row,col,piece):
        self.board[row][col] = piece
    
    def win(self,piece):
        ### Check horizontal
        for c in range(self.COL_COUNT-3):
            for r in range(self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r][c+1] == piece and self.board[r][c+2] == piece and self.board[r][c+3] == piece:
                    return True
        
        
        ### Check vertical
        for c in range(self.COL_COUNT):
            for r in range(self.ROW_COUNT-3):
                if self.board[r][c] == piece and self.board[r+1][c] == piece and self.board[r+2][c] == piece and self.board[r+3][c] == piece:
                    return True
                
                
        ### Check -VE ly sloped Diagonal
        for c in range(self.COL_COUNT-3):
            for r in range(3,self.ROW_COUNT):
                if self.board[r][c] == piece and self.board[r-1][c+1] == piece and self.board[r-2][c+2] == piece and self.board[r-3][c+3] == piece:
                    return True 
    
    
    
        for c in range(self.COL_COUNT-3):
                for r in range(self.ROW_COUNT-3):
                    if self.board[r][c] == piece and self.board[r+1][c+1] == piece and self.board[r+2][c+2] == piece and self.board[r+3][c+3] == piece:
                        return True 

    def draw_board(self):
        for c in range(self.COL_COUNT):
            for r in range(self.ROW_COUNT):
                pygame.draw.rect(screen,self.BLUE,(c*self.SQUARESIZE,r*self.SQUARESIZE+self.SQUARESIZE,self.SQUARESIZE,self.SQUARESIZE))
                
                if self.board[r][c] == 0:
                    pygame.draw.circle(screen,self.BLACK,(int(c*self.SQUARESIZE+self.SQUARESIZE/2),int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)),self.radius)
                elif self.board[r][c] == 1:
                    pygame.draw.circle(screen,self.player1_color,(int(c*self.SQUARESIZE+self.SQUARESIZE/2),int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)),self.radius)
                elif self.board[r][c] == 2:
                    pygame.draw.circle(screen,self.player2_color,(int(c*self.SQUARESIZE+self.SQUARESIZE/2),int(r*self.SQUARESIZE+self.SQUARESIZE+self.SQUARESIZE/2)),self.radius)
        pygame.display.update()

    def game(self):
        self.board = self.create_board()
        self.draw_board()
        while not self.game_over:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                
                if event.type == pygame.MOUSEMOTION:
                    pygame.draw.rect(screen,self.BLACK,(0,0,self.width,SQUARESIZE))
                    posx = event.pos[0]
                    if self.turn == 0:
                        pygame.draw.circle(screen,self.player1_color,(posx,int(self.SQUARESIZE/2)),self.radius)
                    else:
                        pygame.draw.circle(screen,self.player2_color,(posx,int(self.SQUARESIZE/2)),self.radius)
                pygame.display.update()
                
                if event.type == pygame.MOUSEBUTTONDOWN:
                    

                    if self.turn == 0:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.SQUARESIZE))
              
                        #col = int(input('Player 1 Make Your Selection (0-6):'))
                        if self.check_columns(col):
                            row = self.open_row(col)
                            self.drop_piece(row,col,1)
                            
                            if self.win(1):
                                print('PLAYER 1 WINS !!!!! CONGRATS')
                                pygame.draw.rect(screen,self.BLACK,(0,0,self.width,SQUARESIZE))
                                label = self.font.render('PLAYER 1 WINS !!!!! CONGRATS',1,self.player1_color)
                                screen.blit(label,(40,10))
                                self.game_over = True
                                
                                
                        print(self.board)
                        print('\n')
                       
                    ## Ask player 2 for input
                    
                    else:
                        posx = event.pos[0]
                        col = int(math.floor(posx / self.SQUARESIZE))
                        #col = int(input('Player 2 Make Your Selection (0-6):'))
                        if self.check_columns(col):
                            row = self.open_row(col)
                            self.drop_piece(row,col,2)
                            
                            if self.win(2):
                                print('PLAYER 2 WINS !!!!! CONGRATS')
                                pygame.draw.rect(screen,self.BLACK,(0,0,self.width,SQUARESIZE))
                                label = self.font.render('PLAYER 2 WINS !!!!! CONGRATS',1,self.player2_color)
                                screen.blit(label,(40,10))
                                self.game_over = True
                        print(self.board)
                        print('\n')
                    self.draw_board()    
                    self.turn = self.turn + 1
                    self.turn = self.turn % 2
                    
                if self.game_over:
                    pygame.time.wait(3000)
        pygame.quit()
        sys.exit()
                
                
        ## Ask player1 for input

    
   

pygame.init()  
size = (COL_COUNT * SQUARESIZE,(ROW_COUNT + 1) * SQUARESIZE)


screen = pygame.display.set_mode(size)
game = Connect4()
game.game()    
      
    
    
    
    







        ### PLayer 2
    
    
    
    




























