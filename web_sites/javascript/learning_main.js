// single element selector
console.log(document.getElementById('my-form'));
console.log(document.querySelector('h1'));

// multiple element selector
console.log(document.querySelectorAll('.item'));

// loop through items
// const items = document.querySelectorAll('.item');
// items.forEach((item)) => console.log((item));

// changing the DOM
// const ul = document.querySelector('.items');
// ul.firstElementChild.textContent = 'Hello';
// ul.children[1].innerText = 'Brad';
// ul.children[2].innerHTML = '<h1>Smile</h1>';
// ul.lastElementChild.remove();

// const btn = document.querySelector('.btn');
// btn.addEventListener('click', (e) => {
//     e.preventDefault();
//     console.log('click');
// });


const myForm = document.querySelector('#my-form');
const nameInput = document.querySelector('#name');
const emailInput = document.querySelector('#email');
const msg = document.querySelector('.msg');
const userList = document.querySelector('#users');

myForm.addEventListener('submit', onSubmit);

function onSubmit(e) {
    e.preventDefault();

    if(nameInput.value == '' || emailInput.value == '') {
        msg.classList.add('error');
        msg.innerHTML = 'Please enter all fields';

        setTimeout(() => msg.remove(), 3000);
    } else {
        const li = document.createElement('li');
        li.appendChild(document.createTextNode(`${nameInput.value}: ${emailInput.value}`));
        userList.appendChild(li);

        // clear fields
        nameInput.value = '';
        emailInput.value = '';
    }
}