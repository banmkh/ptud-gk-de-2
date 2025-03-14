document.addEventListener("DOMContentLoaded", function() {
    document.querySelectorAll(".status-select").forEach(select => {
        select.addEventListener("change", function() {
            let parent = this.closest(".task-item");
            if (this.value === "completed") {
                parent.classList.add("completed-task");
            } else {
                parent.classList.remove("completed-task");
            }
        });
    });
});