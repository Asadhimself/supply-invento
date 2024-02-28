const form = document.getElementById('form');
const item = document.getElementById('item');
const image_link = document.getElementById('image_link');
const quantity = document.getElementById('quantity');
const measurement = document.getElementById('measurement');

form.addEventListener('submit', e => {
    e.preventDefault();

    validateInputs();
});

const setError = (element, message) => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = message;
    inputControl.classList.add('error');
    inputControl.classList.remove('success')
}

const setSuccess = element => {
    const inputControl = element.parentElement;
    const errorDisplay = inputControl.querySelector('.error');

    errorDisplay.innerText = '';
    inputControl.classList.add('success');
    inputControl.classList.remove('error');
};

const validateInputs = () => {
    const itemValue = item.value.trim();
    const imageLinkValue = image_link.value.trim();
    const quantityValue = quantity.value.trim();
    const measurementValue = measurement.value.trim();

    if(itemValue === '') {
        setError(item, 'Item is required');
    } else {
        setSuccess(item);
    }

    if(imageLinkValue === '') {
        setError(image_link, 'Image link is required');
    } else {
        setSuccess(image_link);
    }

    if(quantityValue === '') {
        setError(quantity, 'Quantity is required');
    } else {
        setSuccess(quantity);
    }

    if(measurementValue === '') {
        setError(measurement, 'Measurement is required');
    } else {
        setSuccess(measurement);
    }

};
