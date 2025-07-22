/**
 * @param {number} n
 * @return {number}
 */
var sumOfMultiples = function (n) {
    if (!Number.isInteger(n)) {
        throw new TypeError("n must be a valid Number");
    } else if (n <= 0) {
        return null;
    }

    let nums = [];

    for (let i = 0; i <= n; i++) {
        if (i % 3 == 0 || i % 5 == 0 || i % 7 == 0) {
            nums.push(i);
        }
    }

    let sum = 0;

    for (let j = 0; j < nums.length; j++) {
        sum += nums[j];
    }
    return sum;
};

console.log(sumOfMultiples(7));
console.log(sumOfMultiples(10));
console.log(sumOfMultiples(9));
