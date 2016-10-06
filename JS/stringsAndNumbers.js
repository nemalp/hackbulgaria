function stringsAndNumbers(input) {

    var matchOnlyDigits = /(\d+)/g,
        sortedArray = [],
        inputCopy = input,
        decodedString,
        numericArray,
        obj = {},
        output = 0,
        i, j;

    createSortedArray(input);

    // Take only the first ten elements (0 - 9)
    sortedArray.splice(10, sortedArray.length - 10);

    // Replace numeric values with the corresponding numbers from 0 - 9
    for(i = 0, j = 9; i < sortedArray.length; i++, j--) {
        sortedArray[i][1] = j;
    }

    decodeChars(sortedArray);

    // Extract only digits from the decoded string
    numericArray = decodedString.match(matchOnlyDigits);

    // Sum all numbers
    if(numericArray.length == 1) {
        output = parseInt(numericArray[0], 10);

    } else {
        numericArray.forEach(function(number){
            // remove leading zeroes
            var parsedNum = parseInt(number, 10);
            output += parsedNum;
        });
    }

    // Create sorted array of arrays in descending order. Each sub-array contains a single char from the input string and how many times it is repeated.
    function createSortedArray(inputString) {
        for(i = 0; i < input.length; i++) {
            var val = input.split(input[i]).length - 1;
            var ch = input[i];

            obj[ch] = val

        }

        for(var key in obj) {
            sortedArray.push([key, obj[key]]);
        }

        sortedArray.sort(function(a, b){
            return b[1] - a[1];
        });
    }

    function decodeChars(arr) {
        arr.forEach(function(element) {

            for(i = 0; i < inputCopy.length; i++) {
                var s = input[i];

                if(s.match(/[a-z]/i)){
                    var re = new RegExp(s, "g");
                } else {
                    var re = new RegExp('\\' + s, "g");
                };

                if(s == element[0]) {
                    decodedString = inputCopy.replace(re, element[1]);
                    inputCopy = decodedString;
                };

            };
        });

    }

    return output;

    //console.log(output);
    //console.log(decodedString);
}


var s = "bbcccddddeeeeeffffffggggggghhhhhhhhiiiiiiiiijjjjjjjjjja";

var s1 = '}w#\\a:\\?uxv?xvxx@axx?\\u\\^:a~wx?x-:u\\v\\a:???^xv?x??cwwx_?uhvc:w<v,:ucwzuaw::uaucwaa^ra:;?:\\?xbw[^^:w::ca\\wcvl\\:%';

var s2 = 'pr$pprtppp{%r%%#(;%rn$;~*s%r%r%;(#(x$p([~(~(r}%=([$[#[~[;~+rr~[r#(n([r%(n%b~;p#rp($;$[,l?(n~p#%$prn~%$r#(~$';

var s3 = '|?=xi^.k%x||^cs^s^=||x=x|.&=..|=x=|&kv^^jkt&jzx.xx=|&&!jkjs&kj|x>j.!..^&k..&k||o&s|s=j.xx!x)j=!&s&]n|^j.!jx';

console.log(stringsAndNumbers(s));
console.log(stringsAndNumbers(s1));
console.log(stringsAndNumbers(s2));
console.log(stringsAndNumbers(s3));
