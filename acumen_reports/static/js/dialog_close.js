(function() {
  var dialog = document.querySelector('dialog');
  dialogPolyfill.registerDialog(dialog);
  dialog.querySelector('.close')
    .addEventListener('click', function() {
      dialog.close();
    });
}());
