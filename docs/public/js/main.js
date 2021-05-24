
window.addEventListener('load', init);

let page = 0;
let maxpage = 0;
let x = 0;
let enabled = true;
i = 0;
function init() {
    maxpage = Math.floor((document.querySelectorAll('.endmenu-element').length + 3) / 4);
}

function endmenuleft() {
    if (enabled) {
        page = (page + maxpage - 1) % maxpage;
        enabled = false;
        tick()
    }
}

function endmenuright() {
    if (enabled) {
        page = (page + 1) % maxpage;
        enabled = false;
        tick()
    }
}

function tick() {
    i += 0.02
    document.getElementById("endmenu").style.transform = "translate(" + (((3 * x) + (page * -100)) / 4) + "vw, 0)";
    x = (((3 * x) + (page * -100)) / 4);
    if (i > 1) {
        x = page * -100;
        document.getElementById("endmenu").style.transform = "translate(" + (page * -100) + "vw, 0)";
        enabled = true;
        i = 0;
    }
    else setTimeout(tick, 10);
}

function print(it) {
    it.select();
    document.execCommand("copy");
}

window.onload = function() {
    var clipboard = new ClipboardJS(".rdzip");
    console.log("onLoad Called")

    clipboard.on('success', function (e) {
        console.info('Action:', e.action);
        console.info('Text:', e.text);
        console.info('Trigger:', e.trigger);

        e.clearSelection();
    });
    clipboard.on('error', function (e) {
        console.error('Action:', e.action);
        console.error('Trigger:', e.trigger);
    });
};