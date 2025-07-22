/**
 * @param {number[]} nums
 * @return {number[]}
 */
var leftRightDifference = function (nums) {
    if (!Array.isArray(nums)) {
        throw new TypeError("nums must be a valid array");
    }
    else if (nums.length == 0) {
        return 0;
    }

    let left_sum = [];
    let right_sum = [];

    let left_total = 0;

    for (let i = 0; i < nums.length; i++) {
        left_sum.push(left_total);
        left_total += nums[i];
    }

    let right_total = 0;

    for (let j = nums.length - 1; j >= 0; j--) {
        right_sum.push(right_total);
        right_total += nums[j];
    }
    right_sum.reverse()

    let answer = [];
    let k = 0;

    while (k < nums.length) {
        answer.push(Math.abs(left_sum[k] - right_sum[k]));
        k++;
    }

    return answer;


};


console.log(leftRightDifference([10, 4, 8, 3]));