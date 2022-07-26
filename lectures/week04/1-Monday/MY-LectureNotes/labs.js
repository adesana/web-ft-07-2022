

let firstName = 'Austin'
let lastName = 'Desana'

console.log(firstName+' '+lastName)

let a = 4
let b = 6

let sum = a+b

console.log(sum)


let name = firstName + ' ' + lastName

console.log(name)

let num1 = 5
let num2 = 3

if (num1 > num2){
    console.log(`${num1} is greater than ${num2}`)
}
else if(num1 < num2){
    console.log(`${num1} is less than ${num2}`)
}
else {
    console.log(`${num1} is equal to ${num2}`)
}


let month = 2
// if (
//     month === 1 ||
//     month === 3 ||
//     month === 5 ||
//     month === 7 ||
//     month === 8 ||
//     month === 10 ||
//     month === 12
//   ) {
//     alert("This month has 31 days");
//   } else if (month === 4 || month === 6 || month === 9 || month === 11) {
//     alert("This month has 30 days");
//   } else if (month === 2) {
//     alert("This month has 28 days");
//   } else {
//     alert("Unknown month!");
//   }

switch(month){

    case 4, 6, 9, 11:
        console.log('This month has 30 days.')
        break;
    case 1, 3, 5, 7, 8, 10, 12:
        console.log('This month has 31 days.')
        break;
    case 2:
        console.log('This month has 28 days.')
        break;
    
    default:
        console.log('Unknown Month')
}


for (i=0; i<=20; i++){
    if (i % 2 == 0){
        console.log(i);
    }
}


var x = 0;
while (x <= 20) {
  if (x % 2 == 0)
    console.log(x);
  x++;
}



for (var i = 0; i <= 30; i++) {
    if (i % 15 == 0) console.log("FizzBuzz");
    else if (i % 3 == 0) console.log("Fizz");
    else if (i % 5 == 0) console.log("Buzz");
    else console.log(i);
}



let str1 = 'javascript'
let str_arr = str1.split('')
for (i=0; i<str1.length; i++){
    if ((i+1) % 2 ==0){
        str_arr[i] = 'Z'
        
    }
    str2 = str_arr.join('')

}

console.log(str2)