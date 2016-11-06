function lakes(input) {
    var directions = input.split(''),
        water = 0,
        counter = 0;

    directions.forEach(function(direction) {

        switch(direction) {
            case 'd':
                counter++;

                if(counter > 0) {
                    water += 500;

                    if(counter > 1){
                        water += 1000 * (counter - 1);
                    };
                };

                break;

            case 'u':

                if(counter > 0) {
                    water += 500;

                    if(counter > 1){
                        water += 1000 * (counter - 1);
                    };
                };

                counter--;

                break;

            case 'h':
                if(counter > 0) {
                    water += 1000 * counter;
                };
        }
    });

    return water;
}

var input = 'ddhhuu';
var input1 = 'ddhhddhuhhuuu';
var input2 = 'dddhhhuuhhuuuhdddduu';

console.log(lakes(input));
console.log(lakes(input1));
console.log(lakes(input2));
