#import firebase_admin
#from firebase_admin import credentials, messaging

#path_secret = 'C:/Repos/cenit/cenit-hub/firebase_key.json'
#cred = credentials.Certificate(path_secret)
#firebase_admin.initialize_app(cred)

#def send_notification(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
#    message = messaging.MulticastMessage(
#        notification=messaging.Notification(
#            title=title,
#            body=msg
#        ),
#        data=dataObject,
#        tokens=registration_token,
#    )

    # Send a message to the device corresponding to the provided
    # registration token.
#    response = messaging.send_multicast(message)
    # Response is a message ID string.
#    print('Successfully sent message:', response)

# tokens = ["fhonTw7MRra58G7_IXb9R0:APA91bH4xTrJYdWwEUnx9i3zSj9sBxgBSPZXc7c554BhBnzTQWTU9uQJuEPcP-tzJHsEuMZbPygy0yorByzwEAGr-mdZpZ-ILWqBfxucMaOfms4J4NveRWLeo-0k783KNaJSPl_lh-pj"]

# sendPush("success", "cenit notification", tokens)
