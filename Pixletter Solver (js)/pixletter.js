// Import necessary functions or libraries
const letterGrids = {}; // Define your letter_grids here
const web2lowerset = []; // Define your word list here
const alphabetList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ".split("");

// Function to scan letters based on row and pixels
function scanLetters(row, pixels) {
    const pixelList1 = pixels.map(x => (x == 2 ? 1 : x));
    const pixelList2 = pixels.map(x => (x == 2 ? 0 : x));
    const outputList = [];

    alphabetList.forEach(alphabet => {
        const scan = letterGrids[alphabet][row];
        if (arraysEqual(scan, pixelList1)) {
            outputList.push(alphabet);
        }
        if (arraysEqual(scan, pixelList2)) {
            outputList.push(alphabet);
        }
    });

    return outputList;
}

// Function to check if two arrays are equal
function arraysEqual(arr1, arr2) {
    if (arr1.length !== arr2.length) return false;
    for (let i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }
    return true;
}

// Function to scan for possible words based on character list
function scanWord(charList) {
    const outputList = [];
    const wordList = web2lowerset.filter(word => word.length === charList.length);

    wordList.forEach(word => {
        for (let i = 0; i < charList.length; i++) {
            if (!charList[i].includes(word[i].toUpperCase())) {
                return;
            }
        }
        outputList.push(word);
    });

    return outputList;
}

// Main scanning function
function mainScan() {
    try {
        const characterList = [];
        let rowNumber = 0;

        while (rowNumber < 7) { // Repeat until no more rows
            const pixelInput = prompt(`Enter pixels for row ${rowNumber + 1}:`).split(',');

            if (pixelInput.length === 1 && pixelInput[0] === '') {
                console.log('Uh oh, maybe an error occurred. Returning to menu!');
                menu();
                return;
            }

            pixelInput.forEach((input, length) => {
                const pixels = input.trim().split('').map(Number); // Convert input string to number array
                const pixelScan = scanLetters(rowNumber, pixels);

                if (rowNumber === 0) {
                    characterList.push(pixelScan);
                } else {
                    const compareList = characterList[length];
                    characterList[length] = compareList.filter(char => pixelScan.includes(char));
                }
            });

            rowNumber++;
            const possible = scanWord(characterList);
            console.log('Possible words: ', possible.join(', '));
        }
    } catch (error) {
        console.log('Uh oh, maybe an error occurred. Returning to menu!');
        menu();
    }
}

// Menu function
function menu() {
    let choice = 0;
    while (choice !== 3) {
        console.log("===============");
        console.log("1. Get Started");
        console.log("2. Help");
        console.log("3. Quit");
        choice = prompt("...");

        if (choice === "1") {
            console.log("===============");
            mainScan();
        } else if (choice === "2") {
            console.log("===============");
            console.log(`To use this program, enter the row of pixels, where Green is 1, Red is 0, and Blanks are 2.
For example, our first guess is DOG. After Pixletters has scanned the row, we enter its output,
10002, 21112, 21112. You may enter nothing if you wish to exit the program at any time.`);
        } else if (choice === "3") {
            console.log("===============");
            return; // Quit
        }
    }
}

// Example text output
const pixletterText = `
_____ _      _      _   _               _____       _                
|  __ (_)    | |    | | | |             / ____|     | |               
| |__) |__  _| | ___| |_| |_ ___ _ __  | (___   ___ | |_   _____ _ __ 
|  ___/ \\ \/ / |/ _ \\ __| __/ _ \\ '__|  \\___ \\ / _ \\ \\ \\ / / _ \\ '__|
| |   | |>  <| |  __/ |_| ||  __/ |     ____) | (_) | |\\ V /  __/ |   
|_|   |_/_/\\_\\_|\\___|\\__|\\__\\___|_|    |_____/ \\___/|_| \\_/ \\___|_|   
`;
console.log(pixletterText);
menu();
