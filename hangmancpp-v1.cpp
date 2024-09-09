#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <ctime>
#include <cctype>
#include <algorithm>

using namespace std;

const vector<string> optionsList = {
    "wordlist.txt", "movielist.txt", "videogameslist.txt", "countrieslist.txt",
    "americanstateslist.txt", "tvshowlist.txt", "carslist.txt"
};

void clearScreen() {
    // Clear screen cross-platform
    #ifdef _WIN32
        system("cls");
    #else
        system("clear");
    #endif
}

string getRandomWord(const string& filePath) {
    ifstream file(filePath);
    vector<string> wordList;
    string line;
    
    if (!file) {
        cerr << "Error: Cannot open file " << filePath << endl;
        exit(EXIT_FAILURE);
    }

    while (getline(file, line)) {
        if (!line.empty()) {
            wordList.push_back(line);
        }
    }

    if (wordList.empty()) {
        cerr << "Error: No words found in file " << filePath << endl;
        exit(EXIT_FAILURE);
    }

    srand(static_cast<unsigned>(time(0)));
    return wordList[rand() % wordList.size()];
}

void displayHangman(int chances) {
    const string hangmanStates[] = {
        R"(
            ______
           |      |
           O      |
          /|\     |
          / \     |
          ---------
        )",
        R"(
            ______
           |      |
           O      |
          /|\     |
          /       |
          ---------
        )",
        R"(
            ______
           |      |
           O      |
          /|\     |
                  |
          ---------
        )",
        R"(
            ______
           |      |
           O      |
          /|      |
                  |
          ---------
        )",
        R"(
            ______
           |      |
           O      |
           |      |
                  |
          ---------
        )",
        R"(
            ______
           |      |
           O      |
                  |
                  |
          ---------
        )",
        R"(
            ______
           |      |
                  |
                  |
                  |
          ---------
        )"
    };

    cout << hangmanStates[chances] << endl;
}



void playGame() {
    clearScreen();
    cout << "_______________________________________" << endl;
    cout << "1: Common English Words" << endl;
    cout << "2: Movies" << endl;
    cout << "3: Video Games" << endl;
    cout << "4: Countries" << endl;
    cout << "5: American States" << endl;
    cout << "6: TV Shows" << endl;
    cout << "7: Cars" << endl;
    cout << "_______________________________________" << endl;

    int choice;
    cout << "> ";
    cin >> choice;

    if (choice < 1 || choice > static_cast<int>(optionsList.size())) {
        cerr << "Invalid category number." << endl;
        return;
    }

    string filePath = "database/" + optionsList[choice - 1];
    string word = getRandomWord(filePath);
    transform(word.begin(), word.end(), word.begin(), ::tolower);

    vector<char> blankArr(word.length(), '-');
    vector<char> wordArr(word.begin(), word.end());
    vector<char> attemptedLetters;

    int chances = 6;
    bool completion = false;

    while (chances > 0 && !completion) {
        clearScreen();
        cout << "Word: ";
        for (char ch : blankArr) {
            cout << ch;
        }
        cout << endl;

        cout << "Attempted letters: ";
        for (char ch : attemptedLetters) {
            cout << ch << " ";
        }
        cout << endl;

        displayHangman(chances);

        char guess;
        cout << "Guess a letter: ";
        cin >> guess;
        guess = tolower(guess);

        // Check for invalid input or repeated letters
        if (!isalpha(guess) || std::find(attemptedLetters.begin(), attemptedLetters.end(), guess) != attemptedLetters.end()) {
            cout << "Invalid input or letter already attempted." << endl;
            continue;
        }

        attemptedLetters.push_back(guess);
        bool correctGuess = false;

        for (size_t i = 0; i < word.length(); ++i) {
            if (word[i] == guess) {
                blankArr[i] = guess;
                correctGuess = true;
            }
        }

        if (correctGuess) {
            if (string(blankArr.begin(), blankArr.end()) == word) {
                completion = true;
            } else {
                cout << "CORRECT" << endl;
            }
        } else {
            --chances;
            cout << "INCORRECT" << endl;
        }
    }

    clearScreen();
    if (chances == 0) {
        cout << "YOU COULDNT GUESS THE WORD" << endl;
    } else {
        cout << "CONGRATULATIONS ON GUESSING THE WORD!!!!" << endl;
    }
    cout << "THE WORD WAS: [" << word << "]" << endl;
}

int main(){
    playGame();
}


