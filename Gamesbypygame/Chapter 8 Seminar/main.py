import pygame
from UIclasses import TextClass, ButtonClass



WHITE = (255, 255 ,255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
FONT = "Fonts\Freedom-10eM.ttf"
POPPINS = "Fonts/Poppins-Black.ttf"


def ChangeGameState(GameStateChange):
    global GameState, buttonlist
    GameState = GameStateChange
    buttonlist = []


def NextQuestion(correct):
    global text_num, question_num, cur_team_num, question_list, question, cur_score, scores_list, questionText
    global answer, questiontuple, win_team, team_names, cur_player, cur_name, players_list, end_time_color_change, blit_black
    print(cur_score)
    if correct:
        scores_list[cur_score] += 1
        questionText = TextClass(
                f"{question_text}",
                pygame.font.Font(POPPINS, 24),
                GREEN,
                (950, 400),
                screen
            )
        blit_black = False
        questionText.blit()
    else:
        questionText = TextClass(
                f"{question_text}",
                pygame.font.Font(POPPINS, 24),
                RED,
                (950, 400),
                screen
            )
        blit_black = False
        end_time_color_change = current_time + 3000
        questionText.blit()
        scores_list[cur_score-1] += 1 
    text_num = 0

    if len(question_list) == 0:
        if scores_list[0] > scores_list[1]:
            win_team = team_names[0]
        elif scores_list[1] > scores_list[0]:
            win_team = team_names[1]
        ChangeGameState("InteractiveEnd")
        
    else:
        questiontuple = question_list.pop()
        question = questiontuple[0]
        answer = questiontuple[1]
    if cur_team_num == 0:
        cur_team_num = 1
    else: 
        cur_team_num = 0

    cur_score = (cur_score + 1) % 2
    cur_player += 1
    cur_name = players_list[cur_player]


def GuessedTrue(a):
    global answer
    print(answer)
    if answer == True:
        NextQuestion(True)
    else:
        NextQuestion(False)


def GuessedFalse(a):
    global answer
    print(answer)
    if answer == False:
        NextQuestion(True)
    else:
        NextQuestion(False)


end_time_question_increase = 10

win_team = "No One"
cur_team_num = 0
question_num = 0
text_num = 1
cur_team_text = "Team Vivaan's Turn"
scores_list = [0, 0]
cur_score = 0
cur_player = 0
players_list =[]
blit_black = True


question_list = [
    ("Copper is a mineral", True),
    ("Fossil fuels can be formed from plant waste", True),
    ("Minerals usually take less than 100 years to form", False),
    ("Running out of minerals is a big problem the world faces", False),
    ("Crude oil is the most abundant fossil fuel", False),
    ("Natural gas is a fossil fuel", True),
    ("Fracking can be used to extract coal", False),
    ("There are three types of fossil fuels", True),
    ("Burning fossil fuels can release carbon dioxide", True),
    ("Ores are a fossil fuel", False),
    ("Ore deposits only consist of one type of ore", False),
    ("Ores usually do not have to be refined and can be utilised before being refined", False),
    ("Mining companies need permission from the government to mine an area", True),
    ("Government permission to mine an area gives you complete power over the area", False),
    ("Crushing an ore can refine it", True),
    ("Fossil fuels running out is a problem in the next couple centuries", True),
    ("Minerals running out is a problem in the next couple centuries", False),
    ("Indigenous people are in trouble due to extracting of resources", True),
    ("Some profits from extracting minerals are shared with indigenous people", True),
    ("The Deepwater Horizon Oil SPill happened in 2009", False),
    ("Over 4.9 million barrels were spilt in the Deepwater Horizon Oil Spill", True),
    ("The Deepwater Horizon Oil Spill was one of the worst in history", True),
    ("The Deepwater Horizon Oil Spill happened in the Gulf of Mexico", True)
]

questiontuple = question_list.pop()
question = questiontuple[0]
answer = questiontuple[1]

team_names = ["Team Vivaan", "Team Jason"]
buttonlist = []
team1 = [
    "Krishan",
    "Alvin",
    "Dilyaa",
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
    "Cameron",
]

for x in range(len(team1)):
    try:
        team1person = team1[x]
        team2person = team2[x]
        players_list.append(team1person)
        players_list.append(team2person)
    except IndexError:
        team1person = team1[x]
        players_list.append(team1person)

cur_name = players_list[cur_player]

pygame.init()

pygame.display.set_caption("Chapter 8 Seminar")
screen = pygame.display.set_mode((1900, 900))

GameState = "TitleScreen"

runVar = True

end_time_color_change = 3000

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
                f"{team_names[0]}",
                pygame.font.Font(FONT, 60),
                BLACK,
                (400, 150),
                screen
            )

team2Text = TextClass(
                f"{team_names[1]}",
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
                    "TRUE",
                    pygame.font.Font(POPPINS, 40),
                    GREEN,
                    (400, 550),
                    screen
                ),
                pygame.Rect(400 - 125, 550 - 50, 250, 100),
                0,
                WHITE,
                screen,
                GuessedTrue,
                True
            )

wrongButton = ButtonClass(
                TextClass(
                    "FALSE",
                    pygame.font.Font(POPPINS, 40),
                    RED,
                    (1400, 550),
                    screen
                ),
                pygame.Rect(1400 - 125, 550 - 50, 250, 100),
                0,
                WHITE,
                screen,
                GuessedFalse,
                False
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

            playerText = TextClass(
                f"{cur_name}",
                pygame.font.Font(FONT, 30),
                BLACK,
                (950, 200),
                screen
            )
            playerText.blit()

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

            if blit_black:
                questionText = TextClass(
                    f"{question_text}",
                    pygame.font.Font(POPPINS, 24),
                    BLACK,
                    (950, 400),
                    screen
                )
            questionText.blit()

            score1Text = TextClass(
                f"{team_names[0]}'s Score: {scores_list[0]}",
                pygame.font.Font(POPPINS, 20),
                BLACK,
                (200, 50),
                screen
            )
            score1Text.blit()
            score2Text = TextClass(
                f"{team_names[1]}'s Score: {scores_list[1]}",
                pygame.font.Font(POPPINS, 20),
                BLACK,
                (1700, 50),
                screen
            )
            score2Text.blit()


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

            team1Text = TextClass(
                "Team Jason",
                pygame.font.Font(FONT, 60),
                BLACK,
                (400, 250),
                screen
            )

            team2Text = TextClass(
                "Team Vivaan",
                pygame.font.Font(FONT, 60),
                BLACK,
                (1400, 250),
                screen
            )
            team1Text.blit()
            team2Text.blit()

            score1Text = TextClass(
                f"{scores_list[0]}",
                pygame.font.Font(POPPINS, 50),
                BLACK,
                (400, 320),
                screen
            )
            score1Text.blit()
            score2Text = TextClass(
                f"{scores_list[1]}",
                pygame.font.Font(POPPINS, 50),
                BLACK,
                (1400, 320),
                screen
            )
            score2Text.blit()

            winText = TextClass(
                f"{win_team} Won !",
                pygame.font.Font(POPPINS, 50),
                BLACK,
                (950, 500),
                screen
            )
            winText.blit()

            
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in buttonlist:
                if button.btnRect.collidepoint(mouse_pos):
                        button.command(button.param)
                        print(button.command)
                        if button.command == GuessedFalse or button.command == GuessedTrue:
                            pygame.display.update()
                            pygame.time.wait(3000)
                            blit_black = True
                        

    
    pygame.display.update()
    
    pygame.time.Clock().tick(60)

pygame.quit()