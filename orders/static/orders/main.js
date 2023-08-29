document.addEventListener('DOMContentLoaded', () => {
    
    function disableToppings(isDisabled){
        document.querySelectorAll('.toppingOption').forEach(option => { 
            option.disabled = isDisabled;
        });
    }

    // By default disable all check boxes for toppings
    disableToppings(true);

    // When a pizza order is clicked
    document.querySelectorAll('.toppings').forEach(topping => {
        topping.onclick = function(){
            const nameOfTopping = this.name;
            const numberofTopping = this.id;
            price = this.innerHTML;
            price = price.replace(/[$]/g, "");
            checkTopping(nameOfTopping, numberofTopping, price);
        }
    });
});

function checkTopping(nameOfTopping, numberOfTopping, price){
    // Helper function to disable checkboxes
    function disableToppings(isDisabled){
        document.querySelectorAll('.toppingOption').forEach(option => { 
            option.disabled = isDisabled;
        });
    }

    // Helper function to count checked checkboxes
    async function countChecked() {
        var n = $( "input:checked" ).length;
        return n;
    }

    // Pass the checkbox name to the function
    async function getCheckedBoxes(chkboxName) {
        var checkboxes = document.getElementsByName(chkboxName);
        var checkboxesChecked = [];
        // loop over them all
        for (var i=0; i<checkboxes.length; i++) {
        // And stick the checked ones onto an array...
        if (checkboxes[i].checked) {
            checkboxesChecked.push(checkboxes[i].value);
        }
        }

        // Return the array if it is non-empty, or null
        return checkboxesChecked.length > 0 ? checkboxesChecked : null;
    }


    // Helper function to control the checkbox diabled option
    async function checkChecked(checkLimit) {
        disableToppings(false);
        document.querySelectorAll('.toppingOption').forEach(topping => {
            topping.addEventListener('change',async function() {
                if (this.checked){
                    var count = await countChecked();
                    if (count >= checkLimit){
                        disableToppings(true);
                        var checkedBoxes = await getCheckedBoxes("toppingCheck");
                        makeUrlRequest(nameOfTopping, price, checkedBoxes)
                    }
                }
            });
        })
    }

    // Main function for checking number of toppings
    if (numberOfTopping === 'Cheese'){
        // submit the url or form
        makeUrlRequest(nameOfTopping, price, "No topping");
    } else if (numberOfTopping == '1'){
        checkChecked(1);   
    } else if (numberOfTopping == '2'){
        checkChecked(2);
    } else if (numberOfTopping == '3'){
        checkChecked(3)
    } else {
        checkChecked(5);
    }
}


function makeUrlRequest(nameOfTopping, price, toppingsList){
    document.location.href = "order" + "/" + nameOfTopping + "/" + price + "/" + toppingsList;
}