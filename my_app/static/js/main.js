console.log("Hello from main.js")

// event listener for js-add-address-line
document.getElementById("js-add-address-line").addEventListener("click", () => {

	console.log(document.getElementById("subforms-container").childElementCount);

	const index = document.getElementById("subforms-container").childElementCount;
	const prevIndex = (index == 0) ? 0 : index - 1;

	document.getElementById(`address-${prevIndex}-form`).insertAdjacentHTML("afterend",
		`<div id='address-${index}-form' data-index='${index}'><label for='address-${index}-address_line' class='active'>Address</label><input id='address-${index}-address_line' name='address-${index}-address_line' type='text' value='123 Main St, Smallville, Kansas 50050'><a class='js-remove-address-line' href='#'>Remove</a></div>`)
});