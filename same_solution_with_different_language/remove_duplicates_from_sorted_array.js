/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function (nums) {
    if (!Array.isArray(nums)) {
        throw new TypeError('nums must be a valid Array');
    }
    else if (nums.length == 0) {
        return null;
    }

    let left = 0;
    let right = nums.length;

    while (left < right) {
        if (nums[left] == nums[right]) {
            nums.removeDuplicates()
        }
    }
};
console.log(removeDuplicates([1, 1, 2]));
console.log(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]));