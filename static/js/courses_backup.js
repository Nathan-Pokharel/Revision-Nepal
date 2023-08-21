let tags;
let currentIndex = 0;
const chunkSize = 3;

function navigateTo(folder, subfolder) {
    const currentUrl = window.location.href;
    let newurl;

    if (subfolder === "nil") {
        newurl = currentUrl + folder + "/";
    } else {
        newurl = currentUrl + folder + "/" + subfolder + "/";
    }

    window.location.href = newurl;
}

function updateTags() {
    tags = document.querySelectorAll('.tag');
    const arrowButtons = document.querySelectorAll('.arrow-button');
    alert(arrowButtons)
    if (tags.length > 50) {
        arrowButtons.forEach(button => {
            button.style.display = 'inline-block';
        });
    } else {
        arrowButtons.forEach(button => {
            button.style.display = 'none';
        });
    }

    tags.forEach((tag, index) => {
        if (index >= currentIndex && index < currentIndex + chunkSize) {
            tag.style.display = 'inline-block';
        } else {
            tag.style.display = 'none';
        }
    });
}

function showNext() {
    if (currentIndex + chunkSize < tags.length) {
        currentIndex += chunkSize;
        updateTags();
    }
}

function showPrevious() {
    if (currentIndex - chunkSize >= 0) {
        currentIndex -= chunkSize;
        updateTags();
    }
}

document.addEventListener('DOMContentLoaded', function() {
    const prevButton = document.getElementById("prevButton");
    const nextButton = document.getElementById("nextButton");
    prevButton.addEventListener('click', showPrevious);
    nextButton.addEventListener('click', showNext);

    updateTags();
});
