let animatable = 'Cвинья! Ковырял нос и ничего не написал. Вот 2 упрека за нынешний день'

const letters = split(animatable)
setTimeout(() => letters.forEach(span => span.style.opacity = 1), 0)

function split(element) {
  element.style.wordBreak = 'break-word'

  const letters = element.innerText.split('').map((letter, i) => {
    const span = document.createElement('span')
    span.innerHTML = letter !== ' ' ? letter : '&nbsp;'
    span.style.opacity = 0
    span.style.transitionDelay = 0.1 * i + 's'
    return span
  })

  element.innerHTML = ''
  element.append(...letters)
  return letters
}