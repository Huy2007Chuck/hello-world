// File: guessing_game.cpp
// By: Huy2007Chuck
// A simple guessing game in C++

#include <iostream>
#include <ctime>

int randint(int min, int max) {
    return rand() % max + min;
}

int main() {
    int min, max, target, guess, score = 0;

    srand(time(0));

    max = randint(60, 100);
    min = randint(1, 40);
    target = randint(min, max);

    std::cout << "Max number is: " << max << "\n";
    std::cout << "Min number is: " << min << "\n";
    std::cout << "Target is: " << target << "\n";
    std::cout << "Enter your guess\n";
    std::cin >> guess;
    score++;

    while (guess != target) {
        if (guess > target)
            std::cout << "Your guess is greater than the target\n";
        else
            std::cout << "Your guess is less than the target\n";

        std::cout << "Guess again\n";
        std::cin >> guess;
        score++;
    }

    if (score == 1)
        std::cout << "You guessed the target " << target << " in " << score << " attempt.";
    else
        std::cout << "You guessed the target " << target << " in " << score << " attempts.";

    return 0;
}
