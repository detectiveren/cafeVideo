// If the notification button is clicked
document.addEventListener("DOMContentLoaded", function() {
    const notificationButton = document.getElementById("notificationButton");
    const cafeNotificationsPanel = document.getElementById("cafeNotificationsPanel");

    notificationButton.addEventListener("click", () => {
        event.stopPropagation();
        cafeNotificationsPanel.classList.toggle("hidden");
    });

    // If the cursor clicks anywhere outside the notification area
    document.addEventListener("click", (event) => {
        if (!cafeNotificationsPanel.contains(event.target) && !notificationButton.contains(event.target)) {
            cafeNotificationsPanel.classList.add("hidden");
        }
    });
});