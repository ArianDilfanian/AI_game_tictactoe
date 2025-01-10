import pygame
import sys
import time
import tictactoe as ttt

pygame.init()
size = width, height = 800,600

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 128, 0)
blue = (124, 178, 232)
redo = (255, 102, 102)

screen = pygame.display.set_mode(size)

mediumFont = pygame.font.Font("OpenSans-Regular.ttf", 28)
largeFont = pygame.font.Font("OpenSans-Regular.ttf", 40)
moveFont = pygame.font.Font("OpenSans-Regular.ttf", 60)

user = None
board = ttt.initial_state()
ai_turn = False
difficulty_selected = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    # Let user choose difficulty
    if not difficulty_selected:
        title = largeFont.render("Select Difficulty", True, white)
        titleRect = title.get_rect()
        titleRect.center = ((width / 2), 50)
        screen.blit(title, titleRect)

    # Define the buttons with a gap
        easyButton = pygame.Rect((width / 4) - 50, (height / 2), width / 4, 50)  # Shift left
        hardButton = pygame.Rect((2 * (width / 4)) + 50, (height / 2), width / 4, 50)  # Shift right

        easyText = mediumFont.render("Easy", True, green)
        hardText = mediumFont.render("Hard", True, red)

        easyTextRect = easyText.get_rect(center=easyButton.center)
        hardTextRect = hardText.get_rect(center=hardButton.center)

        pygame.draw.rect(screen, white, easyButton)
        pygame.draw.rect(screen, white, hardButton)
        screen.blit(easyText, easyTextRect)
        screen.blit(hardText, hardTextRect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if easyButton.collidepoint(mouse):
                ttt.set_difficulty("easy")
                difficulty_selected = True
                time.sleep(0.2)
            elif hardButton.collidepoint(mouse):
                ttt.set_difficulty("hard")
                difficulty_selected = True
                time.sleep(0.2)

    elif user is None:
        title = largeFont.render("Play Tic-Tac-Toe", True, white)
        titleRect = title.get_rect(center=(width / 2, 50))
        screen.blit(title, titleRect)

        playXButton = pygame.Rect((width / 8), (height / 2), width / 4, 50)
        playOButton = pygame.Rect(5 * (width / 8), (height / 2), width / 4, 50)
        playX = mediumFont.render("Play as X", True, blue)
        playO = mediumFont.render("Play as O", True, redo)

        playXRect = playX.get_rect(center=playXButton.center)
        playORect = playO.get_rect(center=playOButton.center)

        pygame.draw.rect(screen, white, playXButton)
        pygame.draw.rect(screen, white, playOButton)
        screen.blit(playX, playXRect)
        screen.blit(playO, playORect)

        click, _, _ = pygame.mouse.get_pressed()
        if click == 1:
            mouse = pygame.mouse.get_pos()
            if playXButton.collidepoint(mouse):
                user = ttt.X
                time.sleep(0.2)
            elif playOButton.collidepoint(mouse):
                user = ttt.O
                time.sleep(0.2)

    else:
        # Draw game board
        tile_size = 80
        tile_origin = (width / 2 - (1.5 * tile_size),
                       height / 2 - (1.5 * tile_size))
        tiles = []
        for i in range(3):
            row = []
            for j in range(3):
                rect = pygame.Rect(
                    tile_origin[0] + j * tile_size,
                    tile_origin[1] + i * tile_size,
                    tile_size, tile_size
                )
                pygame.draw.rect(screen, white, rect, 3)

                if board[i][j] != ttt.EMPTY:
                    
                    color = blue if board[i][j] == ttt.X else redo
                    move = moveFont.render(board[i][j], True, color)
                    moveRect = move.get_rect()
                    moveRect.center = rect.center
                    screen.blit(move, moveRect)

                row.append(rect)
            tiles.append(row)

        game_over = ttt.terminal(board)
        player_turn = ttt.player(board)

        # Show title
        if game_over:
            winner = ttt.winner(board)
            if winner is None:
                title = "Game Over: Tie."
            else:
                title = f"Game Over: {winner} wins."
        elif user == player_turn:
            title = f"Your Turn ({user})"
        else:
            title = "Computer thinking..."
        title = largeFont.render(title, True, white)
        titleRect = title.get_rect(center=(width / 2, 30))
        screen.blit(title, titleRect)

        # AI move
        if user != player_turn and not game_over:
            if ai_turn:
                time.sleep(0.5)
                move = ttt.minimax(board)
                board = ttt.result(board, move)
                ai_turn = False
            else:
                ai_turn = True

        # User move
        click, _, _ = pygame.mouse.get_pressed()
        if click == 1 and user == player_turn and not game_over:
            mouse = pygame.mouse.get_pos()
            for i in range(3):
                for j in range(3):
                    if board[i][j] == ttt.EMPTY and tiles[i][j].collidepoint(mouse):
                        board = ttt.result(board, (i, j))

        if game_over:
            againButton = pygame.Rect(width / 3, height - 65, width / 3, 50)
            again = mediumFont.render("Play Again", True, black)
            againRect = again.get_rect(center=againButton.center)
            pygame.draw.rect(screen, white, againButton)
            screen.blit(again, againRect)
            click, _, _ = pygame.mouse.get_pressed()
            if click == 1:
                mouse = pygame.mouse.get_pos()
                if againButton.collidepoint(mouse):
                    time.sleep(0.2)
                    user = None
                    board = ttt.initial_state()
                    ai_turn = False

    pygame.display.flip()

