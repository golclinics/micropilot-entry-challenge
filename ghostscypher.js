function calculateQuadratic(a, b, c){
    let shared_value = Math.sqrt((b * b) - (4 * a * c))

    return {
        x1: ((-b + shared_value) / (2 * a)),
        x2: ((-b - shared_value) / (2 * a)),
    };
}

function getX(a, b, c){
    const {x1, x2} = calculateQuadratic(a, b, c);
    
    return Math.max(x1, x2);
}

// Test
console.log(getX(2, -4, -2))