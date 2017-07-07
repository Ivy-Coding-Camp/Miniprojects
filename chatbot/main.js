//Shows algorithims, control, and API
function has(string) {
    var args = Array.prototype.slice.call(arguments, 0);
    for (var i = args.length - 1; i >= 1; i--) {
        var regex = new RegExp('\\b' + args[i] + '\\b');
        if ((string.search(regex) !== -1)) {
            return true;
        }
    }
    return false;
}
function oneOf(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}
var greetings = ["Hello!", "Hi!", "Hey there", "yo", "wassup!", "What up!"]
var emotions = ["Pretty angry", "Sad", "Great!", "Amazing!", "Not bad"]
var shouldLoop = true;

function startBot() {
    reallySimpleWeather.weather({
        location: 'Okemos, MI', //your location 
        wunderkey: '',
        woeid: '',
        unit: 'f', // 'c' also works
        success: function(w) {
            while (shouldLoop) {
                q = prompt("What would you like to say?")
                if (shouldLoop == null) { shouldLoop = false }
                if (has(q, "name", "Who are you")) { alert("I am Simon.") }
                if (has(q, "hello", "hey", "hi", "sup", "yo", "salutations")) { alert(oneOf(greetings)) }
                if (has(q, "weather", "temperature", "umbrella", "outside")) { alert("The temperature is " + w.temp + '°' + w.units.temp + ", in " + w.city) }
                if (has(q, "how are")) { alert(oneOf(emotions)) }
                if (has(q, "was bad", "poor day", "was okay", "was better")) { alert("I'm sorry to hear that. Hope you feel better!"); }
                if (has(q, "great", "good", "fine")) { alert("Good to hear that you are doing well!"); }
            }
        }
    })
}