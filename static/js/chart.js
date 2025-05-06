document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('moodChart').getContext('2d');
    const entries = JSON.parse(document.getElementById('entries-data').textContent);
    
    const labels = entries.map(entry => new Date(entry.date).toLocaleString());
    const moods = entries.map(entry => {
        if (entry.mood === 'Happy') return 5;
        if (entry.mood === 'Sad') return 1;
        if (entry.mood === 'Neutral') return 3;
        return 3;
    });
    const sentiments = entries.map(entry => entry.sentiment * 5);

    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Mood',
                    data: moods,
                    borderColor: 'blue',
                    fill: false
                },
                {
                    label: 'Sentiment',
                    data: sentiments,
                    borderColor: 'green',
                    fill: false
                }
            ]
        },
        options: {
            scales: {
                y: {
                    beginAtZero: true,
                    max: 5
                }
            }
        }
    });
});