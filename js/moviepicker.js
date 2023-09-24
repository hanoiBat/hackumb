console.log(document.getElementById("METROBUTTON"))
        document.getElementById("METROBUTTON").addEventListener("click", function(){
            const dataToSend = "data metro boomin want some MORE NIG**"
            console.log(dataToSend)
            fetch('/receive-data', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(dataToSend)
            })
            .then(response => response.json())
            .then(data => {
                // Handle the response from the server here
                console.log(data);
            })
            .catch(error => {
                console.error('Error:', error);
            });
})
        