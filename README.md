<h1 align="center">Beyound</h1>
<h4 align="center">Bring back your lost ones❤️</h4>

Demo: https://www.youtube.com/watch?v=q56b7C88TcA&feature=youtu.be

### Inspiration
For most parents, their world revolves around their child. Their whole life is turned upside down when their dear one is gone missing. It is shocking to know that every year more than a million children go missing. In India alone, 174 children go missing every day. Only about 40% of them are ever found again.

Children aged between 3-10 can go missing in a highly crowded area. When authorities find these children, because of their young age, these children can't recall the name, contact info, and address of their parents. This makes it difficult for the authorities

### What it does
Beyound is an eCommerce platform that sells QR code jewelry that helps to get your child back when they are lost. A QR code is added to jewelry like a necklace/bracelet so that when the code is scanned, it shows the name, phone number, and address of the parent.

If a child wearing the Beyound QR code jewelry goes missing in a crowd, the authorities just need to scan the QR code get the contact info of their guardian. The owner also gets notified (through a phone call and a whatsapp text) of the exact location of the scan

In order to improve user engagement, for every successful order that is placed, the user is given a chance to enter a raffle. If their scancount matches the lucky number in the backend, then they would be given a special gift card

### Target audience
Children between the age of 3-10 and older parents over the age of 70. Because of their age, both these age groups have trouble recalling the name, contact info, and address of their caretaker

### Openscreen Interactions
#### QR Code generation
When the user clicks on a 'Generate QR' button, it created an asset and a corresponding QR code. A unique link having the details of the child is added as an intent
A verification is then done to check if the qr code is properly generated
From that the qr code id and the asset id is extracted for further use
A contact object based on the guardian's contact info is then created

#### Workflow when a QR Code is scanned
The scanid is fetched from the query parameter
Based on the scanid, the entire details of the qrcode is extracted. This includes the time of scan, location, region, latitude and longitude etc
Whenever a scan is made, the owner of the QRCode is notified through a automated call and a whatsapp notification

#### Raffle system
In order to improve user engagement, everytime a customer places an order, then would be added to a raffle system
The user would be redirected a site and the scanid is fetched from the query parameter
Based on the scanid, the entire details of the qrcode is extracted.If the scancount matches with the randomly generated lucky number in the backend, that customer would win the lucky draw

#### Twilio Interactions
When a child is missing, a parent will have to contact the local authorities, neighbours, friends and family. But finding each number and manually calling each person is time consuming and difficult in the state of panic. They may also forget to mention critical information. In order to solve this, automated the entire process
It also sends an automated call and message to the owner, whenever the qr code of a missing child is scanned

### How we built it

- Django - Backend framework 
- Twilio - For sending message and call notifications 
- Stripe - Payment Gateway system 
- sqlite3 - Database used 
- Openscreen -Dynamic qr code 
- Bootstrap and css- For styling Javascript
