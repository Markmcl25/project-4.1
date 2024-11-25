document.addEventListener("DOMContentLoaded", function () {
    const upvoteButtons = document.querySelectorAll(".btn-upvote");
    const downvoteButtons = document.querySelectorAll(".btn-downvote");

    console.log("Upvote buttons found:", upvoteButtons);
    console.log("Downvote buttons found:", downvoteButtons);

    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || 
                      document.querySelector('[name=csrfmiddlewaretoken]')?.value;

    if (!csrfToken) {
        console.error("CSRF token not found! Voting functionality will not work.");
        return;
    }

    function handleVote(button, action) {
        const postId = button.dataset.postId;
        const fetchUrl = `/post/${postId}/${action}/`;

        console.log(`Button clicked for ${action}, Post ID: ${postId}`);
        console.log(`${action} Fetch URL: ${fetchUrl}`);

        fetch(fetchUrl, {
            method: "POST",
            headers: {
                "X-CSRFToken": csrfToken,
                "Content-Type": "application/json",
            },
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Failed to ${action}. HTTP status: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                console.log(`${action} successful, response data:`, data);

                const totalVotesElement = document.querySelector(`#total-votes-${postId}`);
                if (totalVotesElement) {
                    totalVotesElement.textContent = `Total Votes: ${data.total}`;
                }
            })
            .catch(error => console.error(`Error during ${action} process:`, error));
    }

    upvoteButtons.forEach(button => {
        button.addEventListener("click", () => handleVote(button, "upvote"));
    });

    downvoteButtons.forEach(button => {
        button.addEventListener("click", () => handleVote(button, "downvote"));
    });
});
