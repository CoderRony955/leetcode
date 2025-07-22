/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function (nums) {
    if (!Array.isArray(nums)) {
        throw new TypeError('nums must be a valid Array');
    }
    else if (nums.length === 0) {
        return null;
    }

    let ans = [];

    for (let i = 0; i < nums.length; i++) {
        ans.push(nums[i] ** 2);

    }

    return ans.sort((a, b) => a - b);

};

console.log(sortedSquares([-4, -1, 0, 3, 10]))
console.log(sortedSquares([-7, -3, 2, 3, 11]))