const getX = require('./getX')
const cli = require('./cli')
const jest = require('jest')

let start = async () => {
    // Start cli interation
    // Promp user to choose either get x of run tests
    let choice = await cli.getUserChoice()
    
    if (choice === "Run Tests") {
        // Run tests
        jest.run([])
        return
    }

    // Prompt user to input nums a, b and c
    let num = await cli.getNums()

    // Output the answer
    console.log(`Larger value of X is -> ${getX(...num)}`);
}

start()