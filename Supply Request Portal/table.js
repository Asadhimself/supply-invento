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

// Get confirmation box and buttons
var confirmationBox = document.querySelector('.confirmation-box');
var confirmButton = document.querySelector('.confirm-btn');
var cancelButton = document.querySelector('.cancel-btn');

// Add click event listener to each delete button
deleteButtons.forEach(function(button) {
    button.addEventListener('click', function(event) {
        event.preventDefault(); // Prevent default link behavior
        confirmationBox.style.display = 'block'; // Show confirmation box
        event.stopPropagation(); // Prevent click event from propagating to document body
    });
});

// Add click event listener to confirm button
confirmButton.addEventListener('click', function() {
    // Perform delete operation here
    // For demonstration, I'm just logging a message
    console.log('Item deleted');
    confirmationBox.style.display = 'none'; // Hide confirmation box
});

// Add click event listener to cancel button
cancelButton.addEventListener('click', function() {
    console.log('Deletion cancelled');
    confirmationBox.style.display = 'none'; // Hide confirmation box
});

// Add click event listener to document body to close confirmation box when clicked outside of it
document.body.addEventListener('click', function(event) {
    if (!confirmationBox.contains(event.target)) {
        confirmationBox.style.display = 'none'; // Hide confirmation box
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
