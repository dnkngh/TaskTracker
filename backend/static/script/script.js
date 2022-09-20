const t = [
    'Cвинья! Ковырял нос и ничего не написал. Вот 2 упрека за нынешний день.'
];

function typeText(){
  let line = 0;
  let count = 0;
  let out = '';
  let htmlOut = document.querySelector('.out');

  function  typeLine(){
    let inverval = setTimeout(function () {
      out += t[line][count];
      htmlOut.innerHTML = out;
      count++;
      if (count >= t[line].length) {
        count = 0;
        line++;
        if (line == t.length) {
          clearTimeout(inverval);
          htmlOut.innerHTML = out;
          return true;
        }
      }
      typeLine();
    }, 100)
  }
  typeLine();
}

function getRandomInt(max) {
  return Math.floor(Math.random() * Math.floor(max));
}

typeText()