function toggleAll() {
    const buttonsWrapper = document.querySelector('.buttons-wrapper');
    if (buttonsWrapper.classList.contains('show')) {
      buttonsWrapper.style.maxHeight = null;
      buttonsWrapper.classList.remove('show');
    } else {
      buttonsWrapper.classList.add('show');
      buttonsWrapper.style.maxHeight = buttonsWrapper.scrollHeight + "px";
    }
  }


  