const getX = require('./getX')
const cli = require('./cli')
const jest = require('jest')

let start = async () => {
    let choice = await cli.getUserChoice()
    if (choice === "Run Tests") {
        jest.run([])
        return
    }
    let num = await cli.getNums()
    console.log(`Larger value of X is -> ${getX(...num)}`);
}

start()