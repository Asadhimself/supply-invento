// Pagination logic

// Get all page buttons
const pageButtons = document.querySelectorAll('.page');

// Add click event listeners to each button
pageButtons.forEach(button => {
  button.addEventListener('click', () => {
    // Remove 'active' class from all buttons
    pageButtons.forEach(btn => btn.classList.remove('active'));

    // Add 'active' class to the clicked button
    button.classList.add('active');
  });
});

// Function to change the active page
function changePage(offset) {
  const activeButton = document.querySelector('.page.active');
  if (activeButton) {
    const currentIndex = Array.from(pageButtons).indexOf(activeButton);
    const newIndex = currentIndex + offset;

    // Check if the new index is within bounds
    if (newIndex >= 0 && newIndex < pageButtons.length) {
      // Remove 'active' class from the current active button
      activeButton.classList.remove('active');

      // Add 'active' class to the new active button
      pageButtons[newIndex].classList.add('active');
    }
  }
}

// Zoom logic

document.addEventListener('DOMContentLoaded', function() {
  const zoomableImages = document.querySelectorAll('.zoomable-image');
  const zoomedPhoto = document.querySelector('.zoomed-photo');
  const zoomedImage = document.querySelector('.zoomed-image');
  const closeBtn = document.querySelector('.close-btn');

  zoomableImages.forEach(image => {
    image.addEventListener('click', () => {
      zoomedImage.src = image.src;
      zoomedPhoto.style.display = 'block';
    });
  });

  closeBtn.addEventListener('click', () => {
    zoomedPhoto.style.display = 'none';
  });

  // Close the zoomed photo when clicking anywhere outside of it
  document.addEventListener('click', function(event) {
    if (event.target === zoomedPhoto || event.target === zoomedImage) {
      zoomedPhoto.style.display = 'none';
    }
  });
});

// Delete confirm logic

var deleteButtons = document.querySelectorAll('.delete-item');
var archiveButtons = document.querySelectorAll('.archive-item');

// Get confirmation box and buttons
var confirmationBox = document.querySelector('.confirmation-box');
var confirmButton = document.querySelector('.confirm-btn');
var cancelButton = document.querySelector('.cancel-btn');

// Function to show confirmation box
function showConfirmationBox(action) {
    var confirmationMessage = confirmationBox.querySelector('p');
    confirmationMessage.textContent = 'Are you sure you want to ' + action + ' this item?';
    confirmationBox.style.display = 'block';
}

// Function to hide confirmation box
function hideConfirmationBox() {
    confirmationBox.style.display = 'none';
}

// Add click event listener to each delete button
deleteButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        showConfirmationBox('delete');
        event.stopPropagation(); // Prevent click event from propagating to document body
    });
});

// Add click event listener to each archive button
archiveButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        showConfirmationBox('archive');
        event.stopPropagation(); // Prevent click event from propagating to document body
    });
});

// Add click event listener to confirm button
confirmButton.addEventListener('click', function() {
    // Perform delete or archive operation here based on a flag or any other logic
    // For demonstration, I'm just logging a message
    console.log('Item action confirmed');
    hideConfirmationBox();
});

// Add click event listener to cancel button
cancelButton.addEventListener('click', function() {
    console.log('Action cancelled');
    hideConfirmationBox();
});

// Add click event listener to document body to close confirmation box when clicked outside of it
document.body.addEventListener('click', function(event) {
    if (!confirmationBox.contains(event.target)) {
        hideConfirmationBox();
    }
});




// Sorting logic

var sortDirection = "asc";

function sortTable(columnIndex) {
    var table, rows, switching, i, shouldSwitch;
    table = document.getElementById("original-table");
    switching = true;

    while (switching) {
        switching = false;
        rows = table.rows;

        for (i = 1; i < rows.length - 1; i++) {
            shouldSwitch = false;
            var x = rows[i].getElementsByTagName("td")[columnIndex].textContent.toLowerCase();
            var y = rows[i + 1].getElementsByTagName("td")[columnIndex].textContent.toLowerCase();

            if ((sortDirection === "asc" && x > y) || (sortDirection === "desc" && x < y)) {
                shouldSwitch = true;
                break;
            }
        }

        if (shouldSwitch) {
            rows[i].parentNode.insertBefore(rows[i + 1], rows[i]);
            switching = true;
        }
    }

    // Toggle sorting direction after sorting is complete
    sortDirection = (sortDirection === "asc") ? "desc" : "asc";
}



// Status logic

var elements = document.querySelectorAll('.status');
    
// Loop through each element
elements.forEach(function(element) {
    // Check content and apply class accordingly
    if (element.textContent.includes('Pending')) {
        element.classList.add('status-pending');
        element.classList.remove('status-partial');
        element.classList.remove('status-full');
    } else if (element.textContent.includes('Partial')) {
        element.classList.add('status-partial');
        element.classList.remove('status-pending');
        element.classList.remove('status-full');
    } else if (element.textContent.includes('Full')) {
      element.classList.add('status-full');
      element.classList.remove('status-pending');
      element.classList.remove('status-partial');
  }
});

function filterTable(status) {

  var tabButtons = document.querySelectorAll('.tablinks');

  // Add the active-tab class to the clicked tab button
  event.currentTarget.classList.add('active-tab');

  tabButtons.forEach(function(button) {
    button.classList.remove('active-tab');
  });

  event.currentTarget.classList.add('active-tab');

  var rows = document.querySelectorAll('tbody tr');
  rows.forEach(function(row) {
    var statusCell = row.querySelector('.status-cell .status');
    if (status === 'all' || statusCell.classList.contains('status-' + status)) {
      row.style.display = '';
    } else {
      row.style.display = 'none';
    }
  });
}

// By default, show all rows
filterTable('all');
