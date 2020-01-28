const navSlide = ()=>{
    const burger = document.querySelector('.burger');
    const nav = document.querySelector('.nav-links');
    const navLinks = document.querySelectorAll('.nav-links li');
    console.log(navLinks)
    navLinks.forEach((link, index)=>{
        link.addEventListener('click', ()=>{
            console.log('click')
            burger.classList.toggle('toggle');
            nav.classList.toggle('nav-active');
            navLinks.forEach((link, index)=>{
                if(link.style.animation){
                    link.style.animation = ''
                }else{
                    link.style.animation = `navLinkFade 0.5s ease forwards ${index/7+0.3}s`
                } 
            });
        });

    });
    burger.addEventListener('click', ()=>{
        //Toggle Nav
        nav.classList.toggle('nav-active');
        //Animate Links
        navLinks.forEach((link, index)=>{
            if(link.style.animation){
                link.style.animation = ''
            }else{
                link.style.animation = `navLinkFade 0.5s ease forwards ${index/7+0.3}s`
            } 
        });
        //Burger Animation
        burger.classList.toggle('toggle');
    });

}

navSlide();