
//var input = 'H, H, H, H, T, T, T';
//var input = 'H, H, H, H, T, T, T, T';
//var input = 'H, T, H, T, T, H, T';
var input = 'T, T, T, H, T, T, T, H, T, T, T, H, H, H, H';
var arr = input.split(', ');

function streak(arr) {
    var i,
        temp,
        streak,
        result,
        length = arr.length,
        highestStreak = 0,
        highestStreakValue, 
        obj = {};

    for(i = 0; i < length; i++) {

        if(temp == arr[i]) {
            streak++;
        } else {
            streak = 1;
        }

        temp = arr[i];

        if(streak >= highestStreak) {
            highestStreakValue = temp;
            highestStreak = streak;

            obj[highestStreakValue] = streak;
        }
    }

    if(!obj['H']) {
        result = 'T wins!';

    } else if(!obj['T']) {
        result = 'H wins!';

    } else if(obj['T'] > obj['H']) {
        result = 'T wins!';

    } else if(obj['H'] > obj['T']) {
        result = 'H wins!';

    } else {

        result = 'Draw!';
    }

    return result;
}

console.log(streak(arr));
