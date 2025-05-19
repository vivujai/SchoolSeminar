import pygame
from UIclasses import TextClass, ButtonClass

def ChangeGameState(GameStateChange):
    global GameState, buttonlist
    GameState = GameStateChange
    buttonlist = []

def NextQuestion(a):
    global text_num, question_num, cur_team_num, question_list, question
    a = a
    text_num = 0

    if len(question_list) == 0:
        ChangeGameState("InteractiveEnd")
        
    else:
        question = question_list.pop()
    if cur_team_num == 0:
        cur_team_num = 1
    else: 
        cur_team_num = 0
    



WHITE = (255, 255 ,255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = "Fontsforpygame\Freedom-10eM.ttf"
POPPINS = "Fontsforpygame/poppins.regular.ttf"


end_time_question_increase = 10

cur_team_num = 0
question_num = 0
text_num = 1
cur_team_text = "Team Jason's Turn"

question_list = [
    "Question question question question question question questoin eusiotnsetoi sentosein",
    "Question question question questiQuestion question question questiQuestion question question questi"
]

question = question_list.pop()
team_names = ["Team Jason", "Team Vivaan"]
buttonlist = []
team1 = [
    "Krishan",
    "Alvin",
    "Cameron",
    "Josh",
    "Ethan",
    "Max",
    "Kyle",
    "Joey",
    "Rex",
    "Dulaine",
    "Aarib",
    "Nathalie"
]

team2 = [
    "MJ",
    "Oliver",
    "AJ",
    "Grace",
    "Dilan",
    "Justin",
    "Jerin",
    "Ella",
    "Jake",
    "Kate",
    "Dilyaa",
    "AJ"
]

pygame.init()

pygame.display.set_caption("Animal Journey")
screen = pygame.display.set_mode((1900, 900))

GameState = "TitleScreen"

runVar = True

#------------------------WIDGETS---------------------

titleText = TextClass(
                "Interactive Activity",
                pygame.font.Font(FONT, 100),
                BLACK,
                (950, 100),
                screen
            )

startButton = ButtonClass(
                TextClass(
                    "Start",
                    pygame.font.Font(FONT, 40),
                    BLACK,
                    (950, 250),
                    screen
                ),
                pygame.Rect(950 - 100, 250 - 50, 200, 100),
                0,
                GREEN,
                screen,
                ChangeGameState,
                "TeamDescribe"
            )

creditsText = TextClass(
                "Credit to Dilan for idea",
                pygame.font.Font(FONT, 40),
                BLACK,
                (950, 550),
                screen
            )

matchText = TextClass(
                "Teams",
                pygame.font.Font(FONT, 100),
                BLACK,
                (950, 100),
                screen
            )

team1Text = TextClass(
                "Team Jason",
                pygame.font.Font(FONT, 60),
                BLACK,
                (400, 150),
                screen
            )

team2Text = TextClass(
                "Team Vivaan",
                pygame.font.Font(FONT, 60),
                BLACK,
                (1400, 150),
                screen
            )

continueButton = ButtonClass(
                TextClass(
                    "Continue",
                    pygame.font.Font(FONT, 40),
                    BLACK,
                    (950, 550),
                    screen
                ),
                pygame.Rect(950 - 125, 550 - 50, 250, 100),
                0,
                GREEN,
                screen,
                ChangeGameState,
                "Levels"
            )

correctButton = ButtonClass(
                TextClass(
                    "CORRECT",
                    pygame.font.Font(POPPINS, 40),
                    GREEN,
                    (400, 550),
                    screen
                ),
                pygame.Rect(400 - 125, 550 - 50, 250, 100),
                0,
                WHITE,
                screen,
                NextQuestion,
                None
            )

wrongButton = ButtonClass(
                TextClass(
                    "INCORRECT",
                    pygame.font.Font(POPPINS, 40),
                    RED,
                    (1400, 550),
                    screen
                ),
                pygame.Rect(1400 - 125, 550 - 50, 250, 100),
                0,
                WHITE,
                screen,
                NextQuestion,
                None
            )

thanksText = TextClass(
                "End Of Our Interactive",
                pygame.font.Font(FONT, 100),
                BLACK,
                (950, 100),
                screen
            )

while runVar:
    current_time = pygame.time.get_ticks()


    match GameState:
        case "TitleScreen":
            screen.fill(WHITE)

            buttonlist = []
            
            
            titleText.blit()
            
            buttonlist.append(startButton)
            startButton.draw()

            creditsText.blit()

        case "TeamDescribe":
            buttonlist = []
            screen.fill(WHITE)

            
            matchText.blit()
            
            team1Text.blit()

            team2Text.blit()

            for x in range(len(team1)):
                member1 = team1[x]

                memberText = TextClass(
                    f"{member1}",
                    pygame.font.Font(FONT, 40),
                    BLACK,
                    (400, 200 + x * 50),
                    screen
                )
                memberText.blit()

            for y in range(len(team2)):
                member2 = team2[y]

                memberText = TextClass(
                    f"{member2}",
                    pygame.font.Font(FONT, 40),
                    BLACK,
                    (1400, 200 + y * 50),
                    screen
                )
                memberText.blit()

            
            buttonlist.append(continueButton)
            continueButton.draw()

        case "Levels":
            screen.fill(WHITE)
            buttonlist = []

            cur_team_text = team_names[cur_team_num]

            curteamText = TextClass(
                f"{cur_team_text}'s turn",
                pygame.font.Font(FONT, 60),
                BLACK,
                (950, 150),
                screen
            )
            curteamText.blit()


            question_text = question

            questionText = TextClass(
                f"{question_text}",
                pygame.font.Font(POPPINS, 24),
                BLACK,
                (950, 400),
                screen
            )
            questionText.blit()


            if current_time > end_time_question_increase:
                if text_num != len(list(question)):
                    text_num += 1

            
            buttonlist.append(correctButton)
            correctButton.draw()

            
            buttonlist.append(wrongButton)
            wrongButton.draw()

        case "InteractiveEnd":
            screen.fill(WHITE)

            buttonlist = []

            thanksText.blit()

            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttonlist:
                if button.btnRect.collidepoint(mouse_pos):
                        button.command(button.param)
                        

    
    pygame.display.update()
    
    pygame.time.Clock().tick(60)

pygame.quit()