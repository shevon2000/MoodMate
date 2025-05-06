document.addEventListener('DOMContentLoaded', function() {
    const dateFilter = document.getElementById('taskDateFilter');
    if (dateFilter) {
        dateFilter.addEventListener('change', function() {
            const date = this.value;
            window.location.href = `/tasks/tasks?date=${date}`;
        });
    }
});