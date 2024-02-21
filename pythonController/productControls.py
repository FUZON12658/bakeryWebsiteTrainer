from js import alert           
from js import document, console

def checkoutPopup(event):
    # Get the product details from the clicked button's parent container

    productContainer = event.target.closest('.imgContainer')
    
    # Extract relevant information
    productName = productContainer.querySelector('.displayProductName').textContent
    productPrice = float(productContainer.querySelector('.displayProductPrice').textContent.replace('Rs ', ''))
    productQuantity = int(productContainer.querySelector('.addToCartQuantity').value)

    # Calculate total price
    totalPrice = productPrice * productQuantity

    popupContent = f"""
        <div class="aboveButtons">
            <div class="popupImageContainer">
                <img class="popupProductImage" src="{productContainer.querySelector('.displayImages').src}" alt="{productName}">
            </div>
            <div class="popupDetailsContainer">
                <div class="popupRow">
                    <span class="popupLabel">Product:</span>
                    <span class="popupValue">{productName}</span>
                </div>
                <div class="popupRow">
                    <span class="popupLabel">Price:</span>
                    <span class="popupValue">Rs {productPrice:.2f}</span>
                </div>
                <div class="popupRow">
                    <span class="popupLabel">Quantity:</span>
                    <span class="popupValue">{productQuantity}</span>
                </div>
                <div class="popupRow">
                    <span class="popupLabel">Delivery Charge:</span>
                    <span class="popupValue">Rs 50</span> <!-- You can modify this based on your actual delivery charge logic -->
                </div>
                <div class="popupRow">
                    <span class="popupLabel">Grand Total:</span>
                    <span class="popupValue">Rs {(totalPrice + 50):.2f}</span> <!-- Total price + delivery charge -->
                </div>
            </div>
        </div>
        <div class="popupButtons">
            <button class="proceedButton" py-click="closePopup()">Proceed</button>
            <button class="closeButton" py-click="closePopup()">Close</button>
        </div>
    """

    # Get the checkoutPopup div and populate it with the content
    checkoutPopupDiv = document.querySelector('.checkoutPopup')
    checkoutPopupDiv.innerHTML = popupContent

    # Display the popup
    checkoutPopupDiv.style.display = 'block'

    blurredBackground = document.querySelector('.toBeBlurred')
    blurredBackground.classList.add('active')


def closePopup(): 
    # Get the checkoutPopup div and hide it
    checkoutPopupDiv = document.querySelector('.checkoutPopup')
    checkoutPopupDiv.style.display = 'none'
    blurredBackground= document.querySelector('.toBeBlurred')
    blurredBackground.classList.remove('active')


