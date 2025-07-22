/**
 * @param {number[]} arr
 * @return {boolean}
 */
var threeConsecutiveOdds = function (arr) {
    if (!Array.isArray(arr)) {
        throw new TypeError("arr must be a valid Array");
    } else if (arr.length == 0) {
        return null;
    }
    else if (arr.length < 3){
        return false;
    }

    let is_odd = true;
    let i = 0;

    while (i <= arr.length - 3) {
        if (arr[i] % 2 !== 0 && arr[i + 1] % 2 !== 0 && arr[i + 2] % 2 !== 0) {
            return is_odd;
        }
        i++;
    }

    return false;
};
