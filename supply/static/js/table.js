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
