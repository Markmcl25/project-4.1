document.addEventListener("DOMContentLoaded", function () {
    const upvoteButtons = document.querySelectorAll(".btn-upvote");
    const downvoteButtons = document.querySelectorAll(".btn-downvote");

    console.log("Upvote buttons:", upvoteButtons);
    console.log("Downvote buttons:", downvoteButtons);

    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;

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
