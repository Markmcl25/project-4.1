document.addEventListener("DOMContentLoaded", function () {
    const upvoteButtons = document.querySelectorAll(".btn-upvote");
    const downvoteButtons = document.querySelectorAll(".btn-downvote");

    console.log("Upvote buttons:", upvoteButtons);
    console.log("Downvote buttons:", downvoteButtons);

    // Retrieve CSRF token from meta tag or hidden input field
    const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content') || 
                      document.querySelector('[name=csrfmiddlewaretoken]')?.value;

    if (!csrfToken) {
        console.error("CSRF token not found!");
        return;
    }

    upvoteButtons.forEach(button => {
        button.addEventListener("click", function () {
            const postId = this.dataset.postId;
            console.log(`Upvote button clicked for Post ID: ${postId}`);

            fetch(`/post/${postId}/upvote/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/json",
                },
            })
                .then(response => {
                    console.log("Fetch response for upvote:", response);
                    if (!response.ok) throw new Error("Failed to upvote.");
                    return response.json();
                })
                .then(data => {
                    console.log("Upvote successful:", data);
                    const totalVotesElement = document.querySelector(`#total-votes-${postId}`);
                    if (totalVotesElement) totalVotesElement.textContent = `Total Votes: ${data.total}`;
                })
                .catch(error => console.error("Error during upvote:", error));
        });
    });

    downvoteButtons.forEach(button => {
        button.addEventListener("click", function () {
            const postId = this.dataset.postId;
            console.log(`Downvote button clicked for Post ID: ${postId}`);

            fetch(`/post/${postId}/downvote/`, {
                method: "POST",
                headers: {
                    "X-CSRFToken": csrfToken,
                    "Content-Type": "application/json",
                },
            })
                .then(response => {
                    console.log("Fetch response for downvote:", response);
                    if (!response.ok) throw new Error("Failed to downvote.");
                    return response.json();
                })
                .then(data => {
                    console.log("Downvote successful:", data);
                    const totalVotesElement = document.querySelector(`#total-votes-${postId}`);
                    if (totalVotesElement) totalVotesElement.textContent = `Total Votes: ${data.total}`;
                })
                .catch(error => console.error("Error during downvote:", error));
        });
    });
});
