document.addEventListener('DOMContentLoaded', function() {
    // Handle upvote button
    document.getElementById('upvote-button').addEventListener('click', function(e) {
        e.preventDefault();
        const url = this.getAttribute('data-url');
        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-votes').innerText = data.total;
            document.getElementById('upvote-count').innerText = data.upvotes;
            document.getElementById('downvote-count').innerText = data.downvotes;
        });
    });

    // Handle downvote button
    document.getElementById('downvote-button').addEventListener('click', function(e) {
        e.preventDefault();
        const url = this.getAttribute('data-url');
        fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json',
            },
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('total-votes').innerText = data.total;
            document.getElementById('upvote-count').innerText = data.upvotes;
            document.getElementById('downvote-count').innerText = data.downvotes;
        });
    });
});
