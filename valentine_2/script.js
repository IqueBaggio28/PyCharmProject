const noButton = document.querySelector('.no_button');
const catImages = document.querySelectorAll('.cat_main');

noButton.addEventListener('mouseover', () => {
    const bodyWidth = document.body.clientWidth;
    const bodyHeight = document.body.clientHeight;
    const buttonWidth = noButton.clientWidth;
    const buttonHeight = noButton.clientHeight;

    const randomX = Math.floor(Math.random() * (bodyWidth - buttonWidth));
    const randomY = Math.floor(Math.random() * (bodyHeight - buttonHeight));

    noButton.style.position = 'absolute';
    noButton.style.zIndex = '100'
    noButton.style.left = randomX + 'px';
    noButton.style.top = randomY + 'px';
    catImages.forEach(catImage => {
        catImage.classList.remove('hidden');
    });
});


const yesButton = document.querySelector('.yes_button');
const mainContainer = document.querySelector('.ask_container');

yesButton.addEventListener('click', () => {
    mainContainer.remove();

    const message = document.createElement('div');
    message.textContent = "Yiiiipyyyy";
    message.style.textAlign = 'center';
    message.style.fontFamily = "Arial";
    message.style.fontSize = '5rem';
    message.style.color = '#fff';




    catImages.forEach(catImage => {
        catImage.classList.add('hidden');
    });
    // const images = document.createElement('img');
    // images.style.position = 'relative';
    // images.style.top ='5rem';
    // images.style.top = '3rem';
    const gif2 = document.createElement('img');
    gif2.src = 'https://gifdb.com/images/high/happy-cat-glad-to-see-you-jump-66iz8j0kv557z85l.gif'; // Replace 'image1.jpg' with your image URL
    gif2.style.width = '17rem';
    gif2.style.height= 'auto';
    gif2.style.position = 'absolute';
    gif2.style.top = '3rem';
    gif2.style.left = '28rem';
    document.body.appendChild(gif2);




    const gif3 = document.createElement('img');
    gif3.src = 'https://gifdb.com/images/high/happy-cat-hands-in-the-air-slow-dancing-gbah5wpamm28t2ul.gif'; // Replace 'image1.jpg' with your image URL
    gif3.style.width = '17rem';
    gif3.style.height= 'auto';
    gif3.style.position = 'absolute';
    gif3.style.bottom = '2rem';
    gif3.style.right = '17rem';
    document.body.appendChild(gif3);

    const gif4 = document.createElement('img');
    gif4.src = 'https://gifdb.com/images/high/happy-cat-you-re-here-excited-jump-414bnrj063t5wry2.gif'; // Replace 'image2.jpg' with your image URL
    gif4.style.width = '15rem';
    gif4.style.height= 'auto';
    gif4.style.position = 'absolute';
    gif4.style.bottom = '4rem';
    gif4.style.left = '7rem';
    document.body.appendChild(gif4);


    // Adding GIF
    const gif = document.createElement('img');
    gif.src = 'happy-cat-smiling-kitty.gif'; // Replace 'animation.gif' with your GIF URL
    gif.style.width = '15rem';
    gif.style.height= 'auto';
    gif.style.position = 'absolute';
    gif.style.top = '4rem';
    gif.style.right = '7rem';
    document.body.appendChild(gif);




    document.body.appendChild(message);
});