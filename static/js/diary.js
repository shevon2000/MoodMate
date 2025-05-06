document.addEventListener('DOMContentLoaded', function() {
    const dateFilter = document.getElementById('dateFilter');
    if (dateFilter) {
        dateFilter.addEventListener('change', function() {
            const date = this.value;
            window.location.href = `/diary/entries?date=${date}`;
        });
    }
});