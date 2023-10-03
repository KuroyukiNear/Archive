function click(){
event = document.createEvent("HTMLEvents");
    event.initEvent("mousedown", true, true);
    event.eventName = "mousedown";
document.querySelector(".tfny-circleGreen").dispatchEvent(event)
}
async function does(){
while(document.querySelector(".tfny-circleGreen") == null){
    await new Promise(r => setTimeout(r, 10));
    console.warn('gg')
}
    console.warn('ff')
    click()
}
let n = 5; //amount of tests
while(n-->0){
does()
}

// https://www.arealme.com/reaction-test/
