"""
Viết 1 game cho phép người dùng đoán số từ 1 đến 100.
Game có 3 cấp độ chơi:
    - dễ - đoán tối đa 9 lần
    - vừa - đoán tối đa 6 lần
    - khó - đoán tối đa 4 lần
Sau khi người dùng hoàn tất 1 lần chơi,
    chương trình sẽ hỏi người dùng có chơi nữa không.
    - Nếu người chơi đồng ý thì tiếp tục 1 lần chơi mới.
    - Nếu không thì kết thúc trò chơi, thống kê số lần chơi thắng/thua
"""
import random
def game_play():
    wins = 0
    losses = 0
    while True:
        print("Choose the level of the game.")
        print("1. Easy: You have 9 times to guess.")
        print("2. Medium: You have 6 times to guess.")
        print("3. Hard: You have 4 times to guess.")
        level = int(input("Choose the level of the game: "))

        if level == 1:
            max_attempts = 9
        elif level == 2:
            max_attempts = 6
        elif level == 3:
            max_attempts = 4
        else:
            print("The level is invalid. It is set to medium in default.")
            max_attempts = 6


        random_num = random.randint(1, 100)
        #print(random_num)
        print(f"\nYou have {max_attempts} times to guess the number from 1 to 100.")
        for i in range(1, max_attempts + 1):
            guess_num = int(input("Enter a number: "))
            if random_num == guess_num:
                print(f"Correct! You guessed the number in {i} times.")
                wins += 1
                break
            else:
                if random_num > guess_num:
                    print(f"Sorry, the number you guessed is lower than the random number.")
                    losses += 1
                else:
                    print(f"Sorry, the number you guessed is higher than the random number.")
                    losses += 1
        print("Win times: ", wins)
        print("Lose times: ", losses)
        print("Game Over! The random number is: ", random_num)
        again = input("\nDo you wanna continue? (yes/no): ").lower()
        if again != "yes":
            break

if __name__ == '__main__':
    game_play()

