import facebook

image_url='https://18f9-218-255-162-116.ap.ngrok.io/photo/facebook/IMG_2324.JPG'
message='New Arrval Guerlain Chanel Dior Parfum Perfume'
link=''
msg=message + "\n"
token='EAAK5QsATIs4BAH9hjA5pdZCimGRTNBWKv8og7NxRXSmw4OrKbJlqkmFYyVyZAPsEk7kAGrXYXDVbw4PF7VXwZCZA3L4SCLklCtHYZBCfW8gc8JZAVA1e6Fy1rqJNWgLc9tGSQex1WHRP27CLvUJG7RBL3Oz79QyFnXrSzE7Gi2iMDlSuZBVfqSesEGXzTKzJL3nZBKGLPZCVu57qqhDZCdfMaOGIHbFvzpKKoTkBcKTuapHhNJwhxqVpHfCRT2WlmalpcZD'
graph=facebook.GraphAPI(access_token=token)

id='jadorelesparfum'
x=graph.put_object(id,'photos',message=msg,url=image_url)
print(x)
print("Success")