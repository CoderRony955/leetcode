/**
 * @param {string} moves
 * @return {boolean}
 */
var judgeCircle = function(moves) {
    if (typeof moves != 'string'){
        throw new TypeError('moves must be a valid string');
    }

    let origin_point = [0, 0];
    for (let i = 0; i < moves.length; i++) {
        if (moves[i] == 'U') {
            origin_point[0] -= 1;
        }else if (moves[i] == 'L'){
            origin_point[1] -= 1;
        }else if (moves[i] == 'R'){
            origin_point[1] += 1;
        }else if (moves[i] == 'D'){
            origin_point[0] += 1;
        }
        
    }

    if (origin_point[0] === 0 && origin_point[1] === 0){
        return true;
    }
    return false;
};