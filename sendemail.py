# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from user import User

# takes in two users.buyer and seller, and the listing and sends the seller email to the seller.


def sendSellerPurchaseEmail(buyer, seller, listing):
    message = Mail(
        from_email='princetonrebook@gmail.com',
        to_emails=seller.getEmail(),
        subject='Rebook Purchase',
        html_content='<p>This email is to notify you that <strong>{buyer}</strong>  has decided to buy your book, <em>{title}</em>, for ${price}.</p>'.format(buyer=buyer.getNetID(), title=listing['title'], price=listing['price']) +
        '<p>Their contact information is <strong>{email}</strong>. They have received your contact information too. Please get in touch with the buyer to work out the logistics of the payment and delivery.</p>'.format(email=buyer.getEmail()) +
        '<p>Also, please <strong>Confirm</strong> the transaction on our website once you have received your book! This will keep the listing status up to date.</p>' +
        '<p>You can always cancel the transaction on the rebook website!</p>' +
        '<p>The <a href=https://princetonrebook.herokuapp.com>Rebook</a> Team </p>')

    try:
        sg = SendGridAPIClient(
            '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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

# takes in two users.buyer and seller, and the listing and sends the buyer email to the buyer.


def sendBuyerPurchaseEmail(buyer, seller, listing):
    message = Mail(
        from_email='princetonrebook@gmail.com',
        to_emails=buyer.getEmail(),
        subject='Rebook Purchase',
        html_content='<p>You have successfully placed your order on <em>{title}</em> for ${price}.</p>'.format(title=listing['title'], price=listing['price']) +
        '<p>The seller is <strong>{seller}.</strong> Their contact information is <strong>{email}</strong>. They have received your contact information too. Please organize payment and delivery conditions amongst yourselves. </p>'.format(seller=seller.getNetID(), email=seller.getEmail()) +
        '<p>Once you have received your book from the seller, be sure to remind the seller to click the check mark button in the "pending" tab of their Buyer Bookbag to ensure that the records are updated.</p>'
        '<p>You can always find this information in your Buyer Bookbag tab.</p>' +
        '<p>The <a href=https://princetonrebook.herokuapp.com>Rebook</a> Team </p>')
    try:
        sg = SendGridAPIClient(
            '#insertKeyHere#')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def sendBuyerCancelEmail(buyer, seller, listing):
    message = Mail(
        from_email='princetonrebook@gmail.com',
        to_emails=buyer.getEmail(),
        subject='Rebook Cancellation',
        html_content='<p>Your order on <em>{title}</em> for ${price} has been cancelled.</p>'.format(title=listing['title'], price=listing['price']) +
        '<p>The listing is now back on the search page and is up for grabs by another buyer.</p>' +
        '<p>If you did not make this cancellation, please contact the seller <strong>{seller}</strong> at <strong>{email}</strong> for more information.</p>'.format(seller=seller.getNetID(), email=seller.getEmail()) +
        '<p>The <a href=https://princetonrebook.herokuapp.com>Rebook</a> Team </p>')
    try:
        sg = SendGridAPIClient(
            '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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def sendSellerCancelEmail(buyer, seller, listing):
    message = Mail(
        from_email='princetonrebook@gmail.com',
        to_emails=seller.getEmail(),
        subject='Rebook Cancellation',
        html_content='<p>The order on your book, <em>{title}</em>, for ${price} has been cancelled.</p>'.format(title=listing['title'], price=listing['price']) +
        '<p>The listing is now back on the search page and is up for grabs by another buyer.</p>' +
        '<p>If you did not make this cancellation, please contact the buyer <strong>{buyer}</strong> at <strong>{email}</strong> for more information.</p>'.format(buyer=buyer.getNetID(), email=buyer.getEmail()) +
        '<p>The <a href=https://princetonrebook.herokuapp.com>Rebook</a> Team </p>')
    try:
        sg = SendGridAPIClient(
            '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')
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)


def main(argv):
    buyer = User('buy', 'buy', 'none')
    seller = User('bye', 'bye', 'none')
    listing = {
        'title': 'hi',
        'price': 10
    }
    sendBuyerCancelEmail(buyer, seller, listing)
