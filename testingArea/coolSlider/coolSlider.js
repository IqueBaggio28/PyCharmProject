const track = document.getElementById("sliderDiv");

window.onmousedown = e =>{
    track.dataset.mouseDownAt = e.clientX
}

window.onmouseup = () => {
    track.dataset.mouseDownAt = "0";
    track.dataset.prevPercentage = track.dataset.percentage;
}

window.onmousemove = e => {

    if(track.dataset.mouseDownAt === "0") return;
    const mouseDelta = parseFloat(track.dataset.mouseDownAt) - e.clientX,
        maxDelta = window.innerWidth / 2;

    const percentage = (mouseDelta / maxDelta) * -100,
        nextPercentageUnconstrained = parseFloat(track.dataset.prevPercentage) + percentage,
        nextPercentage = Math.max(Math.min(nextPercentageUnconstrained, 0), -100);

    track.dataset.percentage = nextPercentage;

    track.style.transform = `translate(${nextPercentage}%, -50%)`;

    for(const image of track.getElementsByClassName("slide")){
        image.animate({
            objectPosition: `${100 + nextPercentage}% center`
    }, { duration: 1200, fill: "forwards" });
    }
}