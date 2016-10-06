var input = 'H, H, H, H, T, T, T';
//var input = 'H, H, H, H, T, T, T, T';
//var input = 'H, T, H, T, T, H, T';
//var input = 'T, T, T, H, T, T, T, H, T, T, T, H, H, H, H';

function headsAndTails(input) {
    var result,
        heads = [],
        tails = [],
        input = input.split(', ').join(''),
        repeatedChars = input.match(/([T|H])\1*/g);

    repeatedChars.forEach(function(element) {

        if(element.indexOf('H') != -1) {
            heads.push(element);

        } else {
            tails.push(element);
        }

    });

    heads.sort(function(a, b) {
        return b.length - a.length;
    });

    tails.sort(function(a, b) {
        return b.length - a.length;
    });

    if(heads[0].length > tails[0].length){
        result = 'H wins!'

    } else if(heads[0].length < tails[0].length) {
        result = 'T wins!'

    } else {
        result = 'Draw!'
    }

    return result;
}

//console.log(headsAndTails(input));
