$(function() {
    $('.selectpicker').selectpicker();
 });
 
function toggleTab(e){
    var hrefVal = $(e).attr('href');
    $('.nav-tabs li').removeClass('active');
    $('.nav-tabs li[data-active="'+hrefVal+'"]').addClass('active');
}
function getJsonData(inputString){
    let startIndex = inputString.indexOf('{');
    let endIndex = inputString.lastIndexOf('}');
    if (startIndex !== -1 && endIndex !== -1 && endIndex > startIndex) {
        // Extract the JSON string
        let jsonString = inputString.substring(startIndex, endIndex + 1);
        try {
            // Parsing JSON string to JavaScript object
            let parsedObject = JSON.parse(jsonString);
            return parsedObject;
            // Now you can use parsedObject[key] to access values
        } catch (e) {
            console.error('Error parsing JSON:', e);
        }
    } else {
        console.error('No valid JSON object found in the input string.');
    }
}
function toggleTabTinder(element) {
    try {
        
        // Get the current counter from the data attribute and increment it
        const currentCounter = parseInt(element.getAttribute('data-counter'), 10);
        const nextCounter = currentCounter + 1;
        
        // Get the current taste category and meaning
        const type = element.getAttribute('data-type');
        const currElement = document.getElementById(`gift_idx_${currentCounter}`);
        const cat = currElement.getAttribute('category');

        var inputPoints = document.getElementById('points_counter');

        var points = getJsonData(inputPoints.value);

        if (type === 'love')
        {
            points[cat] = points[cat] + 2
            const giftId = currElement.getAttribute('data-id');
            console.log(giftId)
            points['liked_gifts'].push(giftId)
        }
        else if (type=='like')
        {
            points[cat] = points[cat] + 1
        }
        else if (type=='hate')
        {
            points[cat] = points[cat] - 1
        }


        console.log(points)

        inputPoints.value = JSON.stringify(points);

        // Get all elements with class 'tindercard' and remove 'in active' from them
        const cards = document.querySelectorAll('.tindercard');
        cards.forEach(card => card.classList.remove('in', 'active'));

        // Add 'in active' to the clicked element's corresponding div
        const nextElementId = `gift_idx_${nextCounter}`;
        const nextElement = document.getElementById(nextElementId);
        if (nextElement) {
            nextElement.classList.add('in', 'active');
        } else {
            const nextElement = document.getElementById('no_products');
            nextElement.classList.add('in', 'active');
        }
    } catch (error) {
        console.error('An error occurred in toggleTabTinder:', error);
    }
}