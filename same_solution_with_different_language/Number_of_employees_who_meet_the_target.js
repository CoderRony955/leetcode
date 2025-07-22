/**
 * @param {number[]} hours
 * @param {number} target
 * @return {number}
 */
var numberOfEmployeesWhoMetTarget = function(hours, target) {
    if (!Array.isArray(hours) && !Number.isInteger(target)){
        throw new TypeError('hours must be valid Array and target must be valid Number');
    }
    for (let i = 0; i < hours.length; i++) {
        if (!Number.isInteger(hours[i])){
            throw new TypeError('Array elements must be valid Number');
        }
    }

    if (!hours) {
        return null;
    }

    let count  = 0;
    for (let j = 0; j < hours.length; j++) {
        if (hours[j] >= target){
            count += 1;
        }
    }

    return count;


};

console.log(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2));
console.log(numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6));