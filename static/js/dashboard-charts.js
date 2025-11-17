// Simple Chart.js initialization placeholder
document.addEventListener('DOMContentLoaded', function(){
    if(typeof Chart === 'undefined') return;

    // Example: sales chart (line)
    const salesCtx = document.getElementById('salesChart');
    if(salesCtx){
        new Chart(salesCtx.getContext('2d'), {
            type: 'line',
            data: {
                labels: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
                datasets: [{
                    label: 'Ventes',
                    data: [12, 19, 8, 24, 15, 30],
                    borderColor: getComputedStyle(document.documentElement).getPropertyValue('--color-accent') || '#8C6FF0',
                    backgroundColor: 'rgba(140,111,240,0.15)',
                    fill: true,
                    tension: 0.3,
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: { position: 'top' }
                }
            }
        });
    }

    // Visits chart (bar)
    const visitsCtx = document.getElementById('visitsChart');
    if(visitsCtx){
        new Chart(visitsCtx.getContext('2d'), {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Visites',
                    data: [120, 190, 150, 230, 300, 280, 320],
                    backgroundColor: getComputedStyle(document.documentElement).getPropertyValue('--color-accent') || '#8C6FF0',
                }]
            },
            options: { responsive: true }
        });
    }
});
