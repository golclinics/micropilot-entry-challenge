const challenge = require('./count_zeros.js');
const { count_zeros } = challenge;

if (count_zeros && typeof count_zeros == 'function') {
    console.log(count_zeros([1, 0, 5, 6, 0, 2]));
    console.log('ran for my life')
}