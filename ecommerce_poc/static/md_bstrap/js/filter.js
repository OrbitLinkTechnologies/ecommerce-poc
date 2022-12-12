const multiExampleFilters = document.getElementById('filter-sort-example-filters');
const multiExampleData = document.getElementById('filter-sort-example-data');
const multiReset = document.getElementById('filterSortReset');
const multiSelect = document.getElementById('filter-sort-select');

// commenting out the dataset below so we reduce clutter on the page;
// the filtering for our product page is still a work in progress
/*const dataset = [
  {
    id: 1,
    color: 'black',
    price: 100,
    sale: 'no',
    product: 'Black Jeans Jacket',
    img: 'https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Vertical/15.webp',
  },
  {
    id: 2,
    color: 'black',
    price: 100,
    sale: 'no',
    product: 'Black Jeans Jacket',
    img: 'https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Vertical/15.webp',
  },
  {
    id: 3,
    color: 'gray',
    price: 80,
    sale: 'yes',
    product: 'Gray Jumper',
    img: 'https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Vertical/14.webp',
  },
  {
    id: 4,
    color: 'gray',
    price: 80,
    sale: 'yes',
    product: 'Gray Jumper',
    img: 'https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Vertical/14.webp',
  },
  {
    id: 5,
    color: 'red',
    price: 120,
    sale: 'yes',
    product: 'Red Hoodie',
    img: 'https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Vertical/13.webp',
  },
  {
    id: 6,
    color: 'blue',
    price: 90,
    sale: 'no',
    product: 'Blue Jeans Jacket',
    img: 'https://mdbcdn.b-cdn.net/img/Photos/Horizontal/E-commerce/Vertical/12.webp',
  },
]; */

const multiInstance = new Filters(multiExampleFilters, {
  items: dataset,
});

const renderItems = (items) => {
  const elements = items.map((item) => {
    const template = `
      <div class="col-md-4 mt-3">
        <div class="card shadow-2">
          <img src="${item.img}"
            class="card-img-top" alt="..." />

          <div class="card-body">
            <h5 class="card-title">${item.product}</h5>
            <p class="card-text">
              ${item.price}$
            </p>
            <a href="#" class="btn btn-primary ripple-surface">Buy now</a>
          </div>
        </div>
      </div>
    `;
    return template;
  });

  multiExampleData.innerHTML = elements.join('\n');
};

renderItems(dataset);

multiExampleFilters.addEventListener('update.mdb.filters', (e) => {
  renderItems(e.items);
});

multiReset.addEventListener('click', () => {
  multiInstance.clear();
});

multiSelect.addEventListener('optionSelect.mdb.select', (e) => {
  const value = e.target.value;
  if (value === '1') {
    multiInstance.sort('product');
  }

  if (value === '2') {
    multiInstance.sort('product', 'desc');
  }

  if (value === '3') {
    multiInstance.sort('price', 'desc');
  }

  if (value === '4') {
    multiInstance.sort('price');
  }
});