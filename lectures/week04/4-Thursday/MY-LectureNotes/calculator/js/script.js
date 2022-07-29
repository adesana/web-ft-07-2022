


let display = document.getElementById('input');
let buttons = Array.from(document.getElementsByClassName('button'));
let num1 =''
let num2 =''
let dic ={}
buttons.map( button => {
    button.addEventListener('click', (e) => {

        switch(e.target.innerText){

            default:
                num2 = display.innerText += e.target.innerText;
                const final = num2.split('+').join('$').split('-').join('$').split('/').join('$').split('*').join('$')
                num1 = final.split('$')
                console.log(num1[0])
                console.log(num1[1])

                
                

        }
    });
});

