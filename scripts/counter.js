async function getResponse(url) {
    const response = await fetch(url, {
        method: "POST"
    });

    if (!response.ok) {
        throw new Error(`HTTP Error, Response status: ${response.status}`);
    }

    return await response.json();
}

async function updateVisitCount() {
    const count_response = await getResponse("https://crc-website-visit-counter-ayavekgjaggfcvha.australiaeast-01.azurewebsites.net/api/visits");
    document.getElementById("visit-count").innerHTML = count_response.count;
}

updateVisitCount();