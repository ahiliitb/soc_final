// to get current year
function getYear() {
    var currentDate = new Date();
    var currentYear = currentDate.getFullYear();
    document.querySelector("#displayYear").innerHTML = currentYear;
}

getYear();


/** google_map js **/

function myMap() {
    var mapProp = {
        center: new google.maps.LatLng(40.712775, -74.005973),
        zoom: 18,
    };
    var map = new google.maps.Map(document.getElementById("googleMap"), mapProp);
}

function messagefunc() {
    alert("We will contact you in few days.\nThank you")
}

function add_to_cart(pid, pname, price) {
    let cart = localStorage.getItem("cart");
    if (cart == null) {
        let products = [];
        let product = { productid: pid, productname: pname, productquantity: 1, productprice: price };
        products.push(product);
        localStorage.setItem("cart", JSON.stringify(products));
    }
    else {
        let pcart = JSON.parse(cart);

        let oldproduct = pcart.find((item) => item.productid == pid)
        if (oldproduct) {
            oldproduct.productquantity = oldproduct.productquantity + 1;
            pcart.map((item) => {
                if (item.productid == oldproduct.productid) {
                    item.productquantity = oldproduct.productquantity;
                }
            })
            localStorage.setItem("cart", JSON.stringify(pcart));
        }
        else {
            let product = { productid: pid, productname: pname, productquantity: 1, productprice: price };
            pcart.push(product)
            localStorage.setItem("cart", JSON.stringify(pcart));
        }
    }
    updatecart()
}

function updatecart() {
    let cartstring = localStorage.getItem("cart");
    let cart = JSON.parse(cartstring);
    if (cart == null || cart.length == 0) {
        $(".cart_number").html("0");
        $(".cart-body").html("<h3>Cart does not have any items </h3>");
        $(".checkout-btn").attr('disabled', true)
    }
    else {
        let ans = 0;
        for (let i = 0; i < cart.length; i++) {
            ans = ans + cart[i].productquantity
        }
        $(".cart_number").html(`${ans}`);
        let table = `
            <table class='table'>
            <thead class='thread-light'>
                <tr>
                <th>Item Name </th>
                <th>Price </th>
                <th>Quantity </th>
                <th>Total Price </th>
                <th>Action</th>
                
        
                </tr>
        
            </thead>

        


            `;

        let totalprice = 0;
        cart.map((item) => {


            table += `
                    <tr>
                        <td> ${item.productname} </td>
                        <td> ${item.productprice} </td>
                        <td> ${item.productquantity} </td>
                        <td> ${item.productquantity * item.productprice} </td>
                        <td> <button onclick='deleteItemFromCart(${item.productid})' class='btn btn-danger btn-sm'>Remove</button> </td>    
                     </tr>
                 `

            totalprice += item.productprice * item.productquantity;

        })
        table = table + `
        <tr><td colspan='5' class='text-right font-weight-bold m-5'> Total Price : ${totalprice} </td></tr>
     </table>`
        $(".cart-body").html(table);
        $(".checkout-btn").attr('disabled', false)
        console.log("removed")
    }

}

function deleteItemFromCart(pid) {
    let cart = JSON.parse(localStorage.getItem('cart'));

    let newcart = cart.filter((item) => item.productid != pid)

    localStorage.setItem('cart', JSON.stringify(newcart))

    updatecart();

    showToast("Item is removed from cart ")

}

$(document).ready(function () {
    updatecart()
})