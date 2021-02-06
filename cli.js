const inquirer = require('inquirer')

let choices = [
    {
        type: "list",
        name: "choice",
        message: "What would you like to do?",
        choices: [
            "Get X ",
            "Run Tests"
        ]
    }
]

let nums = [
    {
        type: 'input',
        name: 'a',
        message: "To find largest X, input a, b, and c below \n \n Input a",
        validate: (value) => isValid(value)
    },
    {
        type: 'input',
        name: 'b',
        message: "then b",
        validate: (value) => isValid(value)
    },
    {
        type: 'input',
        name: 'c',
        message: "and finaly c",
        validate: (value) => isValid(value)
    }
]

let getUserChoice = async () => {
    let choice = await inquirer.prompt(choices)
    return choice.choice
}

let getNums = async () => {
    let num = await inquirer.prompt(nums)
    return [num.a, num.b, num.c]
}

let isValid = (answer) => {
    if (isNaN(answer)) {
        return "Please add a valid number";
    }
    return true;
}

module.exports = {
    getUserChoice,
    getNums
}