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

document.addEventListener("DOMContentLoaded", function() {
  // Function to show confirmation box
  function showConfirmationBox(box) {
      box.style.display = 'block';
  }

  // Function to hide confirmation boxes
  function hideConfirmationBoxes() {
      document.querySelectorAll('.confirmation-box').forEach(function(box) {
          box.style.display = 'none';
      });
  }

  // Add click event listener to each delete button
  document.querySelectorAll('.delete-item').forEach(function(button) {
      button.addEventListener('click', function(event) {
          event.preventDefault();
          var row = button.closest('tr');
          var confirmationBoxId = button.getAttribute('data-confirm-id');
          var confirmationBox = row.querySelector('#' + confirmationBoxId);
          hideConfirmationBoxes();
          showConfirmationBox(confirmationBox);
          event.stopPropagation();
      });
  });

  // Add click event listener to each archive button
  document.querySelectorAll('.archive-item').forEach(function(button) {
      button.addEventListener('click', function(event) {
          event.preventDefault();
          var row = button.closest('tr');
          var confirmationBoxId = button.getAttribute('data-confirm-id');
          var confirmationBox = row.querySelector('#' + confirmationBoxId);
          hideConfirmationBoxes();
          showConfirmationBox(confirmationBox);
          event.stopPropagation();
      });
  });

  // Add click event listener to delete and archive confirm buttons
  document.querySelectorAll('.confirm-btn').forEach(function(button) {
      button.addEventListener('click', function() {
          var row = button.closest('tr');
          if (button.classList.contains('delete-confirm')) {
              console.log('Item deleted');
          } else if (button.classList.contains('archive-confirm')) {
              console.log('Item archived');
          }
          hideConfirmationBoxes();
      });
  });

  // Add click event listener to cancel buttons
  document.querySelectorAll('.cancel-btn').forEach(function(button) {
      button.addEventListener('click', function() {
          hideConfirmationBoxes();
      });
  });

  // Add click event listener to document body to close confirmation boxes when clicked outside of them
  document.body.addEventListener('click', function(event) {
      document.querySelectorAll('.confirmation-box').forEach(function(box) {
          if (!box.contains(event.target)) {
              hideConfirmationBoxes();
          }
      });
  });
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
