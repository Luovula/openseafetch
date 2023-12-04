function updateCounters() {
    fetch('https://dry-plains-13766-d22087ffb2f5.herokuapp.com/get_nft_data')
        .then(response => response.json())
        .then(data => {
            // Assuming 'data' is an array of owner counts
            for (let i = 0; i < data.length; i++) {
                document.getElementById(`counter${i+1}`).innerText = `${data[i]}`;
            }
        })
        .catch(error => console.error('Error:', error));
}

// Call this function periodically
// setInterval(updateCounters, 30000);  // Update every 30 seconds
// Call the function when the page loads
document.addEventListener('DOMContentLoaded', updateCounters);
