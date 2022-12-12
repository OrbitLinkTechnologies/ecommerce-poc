let alertCount = 0;

function* colorGenerator(i) {
  const colors = ['primary', 'warning', 'info', 'success', 'secondary', 'danger', 'light'];

  while (true) {
    yield colors[i];

    i++;

    if (i > colors.length - 1) {
      i = 0;
    }
  }
}

const colorIterator = colorGenerator(0);

document
  .getElementById('stacking-container-trigger-example')
  .addEventListener('click', () => {
    alertCount++;
    color = colorIterator.next().value;

    const alert = document.createElement('div');
    alert.innerHTML = `
      <div class="d-flex justify-content-between">
        <p class="mb-0"><strong>${alertCount}.</strong> Stacking alerts</p>
        <button
          type="button"
          class="btn-close"
          data-mdb-dismiss="alert"
          aria-label="Close"
        ></button>
      </div>
    `;
    alert.classList.add('alert', 'fade');

    document.getElementById('parent-stacking-container-example').appendChild(alert);

    const alertInstance = new mdb.Alert(alert, {
      color,
      stacking: true,
      container: '#parent-stacking-container-example',
      hidden: true,
      width: '250px',
      position: 'top-right',
      autohide: true,
      delay: 5000,
    });

    alertInstance.show();
  });