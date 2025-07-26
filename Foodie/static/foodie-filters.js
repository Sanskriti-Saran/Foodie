// foodie-filters.js
// Handles filter and search form submissions for Foodie app

document.addEventListener('DOMContentLoaded', function () {
  const filterForms = document.querySelectorAll('.foodie-filter-form');
  filterForms.forEach(form => {
    form.addEventListener('submit', function (e) {
      // Optionally, add custom JS validation or UX here
      // For now, let the form submit normally
    });
  });
});
