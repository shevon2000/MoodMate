document.addEventListener('DOMContentLoaded', function() {
    const ctx = document.getElementById('moodChart').getContext('2d');
    const entries = JSON.parse(document.getElementById('entries-data').textContent);
    
    const labels = entries.map(entry => new Date(entry.date).toLocaleString());
    const moods = entries.map(entry => {
        if (entry.mood === 'Cheerful') return 10;       
        if (entry.mood === 'Happy') return 8;        
        if (entry.mood === 'Normal') return 5;    
        if (entry.mood === 'Sad') return 2;    
        if (entry.mood === 'Anxious') return 1;     
    
        return 3;  // Default for any unknown mood
    });
    
    const sentiments = entries.map(entry => entry.sentiment );

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
                    max: 11
                }
            }
        }
    });
});