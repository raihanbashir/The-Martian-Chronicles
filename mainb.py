from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QWidget, QComboBox, QLineEdit
from PySide6.QtGui import QPixmap
import requests

class widg():
    def __init__(self):
        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignLeft)
        self.dropdown = QComboBox()
        self.dropdown.addItem("curiosity")
        self.dropdown.addItem("opportunity")
        self.dropdown.addItem("spirit")
        self.dropdown.move(20, 20)
        self.rover = self.dropdown
        self.rover.currentTextChanged.connect(self.rovercheck)

        self.x = QPushButton('Fetch')  # fetch button
        self.x.setFixedHeight(25)
        self.camText = QPushButton('cam')
        self.camText.setFixedHeight(25)
        self.cam = QComboBox()
        for i in ['FHAZ','RHAZ','MAST','CHEMCAM','MAHLI','MARDI','NAVCAM','PANCAM','MINITES']:self.cam.addItem(i)
        self.earthdateText = QPushButton('earth date')
        self.earthdateText.setFixedHeight(25)
        self.earthdate = QLineEdit('yyyy-mm-dd')
        self.roverText = QPushButton('rover')
        self.roverText.setFixedHeight(25)

        self.params = [self.earthdateText, self.earthdate, self.roverText, self.rover, self.camText, self.cam, self.x]
        self.exclude = [self.earthdateText, self.roverText, self.camText, self.x,self.earthdate]

        self.layout = QVBoxLayout()
        self.layout.setAlignment(Qt.AlignBottom)
        self.x.setFixedHeight(35)
        for i in self.params:
            if i != self.earthdate:
                i.setFixedWidth(300)
            if i != self.x:
                i.setStyleSheet("border-radius: 5px;")
            if i not in self.exclude:
                i.setStyleSheet("border-radius: 5px;background-color: grey;")
                i.setFixedHeight(30)
            if i == self.earthdate:
                i.setStyleSheet("border-radius: 5px;background-color: grey;")
            self.layout.addWidget(i)
    
    def rovercheck(self,text):
        if text == 'curiosity' :
            self.rovername = "curiosity"
        elif text == 'opportunity':
            self.rovername = "opportunity"
        elif text == 'spirit':
            self.rovername = "spirit"


class ImageViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.image_index = 0
        self.images = ["images/image.jpg"]

        self.label = QLabel()
        pixmap = QPixmap(self.images[self.image_index])
        pixmap = pixmap.scaledToHeight(500, Qt.SmoothTransformation)
        self.label.setPixmap(pixmap)


        self.previous_button = QPushButton("Previous")
        self.previous_button.clicked.connect(self.show_previous_image)

        self.next_button = QPushButton("Next")
        self.next_button.clicked.connect(self.show_next_image)

        self.mail_butt = QPushButton("mail")

        button_layout = QHBoxLayout()
        master = QHBoxLayout()
        button_layout.addWidget(self.previous_button)
        button_layout.addWidget(self.next_button)

        button_layout1 = QVBoxLayout()
        button_layout1.setAlignment(Qt.AlignHCenter)
        button_layout1.addWidget(self.mail_butt)
        self.widg = widg()
        self.widg=self.widg.layout
        button_layout.addLayout(self.widg)

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addLayout(button_layout)

        master.addLayout(layout)
        master.addLayout(button_layout1)

        self.setLayout(master)

    def show_previous_image(self):
        self.image_index = (self.image_index - 1) % len(self.images)
        self.label.setPixmap(QPixmap(self.images[self.image_index]))

    def show_next_image(self):
        self.image_index = (self.image_index + 1) % len(self.images)
        self.label.setPixmap(QPixmap(self.images[self.image_index]))

app = QApplication()
viewer = ImageViewer()
viewer.show()
app.exec_()

# if __name__ == '__main__':
#     #tried using os.getenv() but it wasnt working
#     yourkey = '3VDfk7Zt0VMDk1rpXg4gyR5eRb3aSvY1ogdV3g0O'
#     def getpic(rover = 'curiosity',photos = 'photos',date = '2015-06-03',camera = ''):

#         date,photos = latestpic()
#         print(date , photos)
#         rover = rovercheck()
#         camera = checkcamera()

#         #Calling the api and recieving the JSON file
#         apicall = requests.get(f'https://api.nasa.gov/mars-photos/api/v1/rovers/{rover}/{photos}?earth_date={date}{camera}&api_key={yourkey}')
#         apicall = apicall.json()    #Converting the JSON file to a dictionary
#         pictures = []
#         l = apicall[photos]
#         for i in l:
#             pictures.append(i['img_src'])    #Adding the images to a list
#         print(pictures)
#         return pictures

#     def checkcamera():
#         camera = ''
#         chc = input('Enter Camera (FHAZ/RHAZ/NAVCAM): ')
#         if chc == 'FHAZ':
#             camera = '&camera=fhaz'
#         elif chc == 'RHAZ':
#             camera = '&camera=rhaz'
#         elif chc == 'NAVCAM':
#             camera = '&camera=navcam'



#     def rovercheck(): 

#     #Checking to see wwhich rover to choose
#         rover = ''
#         chr = input('Enter rover(Curiosity/Opportunity/Spirit) : ')
#         if chr in ['opportunity','Opportunity','OPPORTUNITY']:
#             rover = 'opportunity'
#         elif chr in ['spirit','Spirit','SPIRIT']:
#             rover = 'spirit'
#         elif chr in ['curiosity','Curiosity','CURIOSITY']:
#             rover = 'curiosity'

#         return rover


#     def latestpic() :

#     #checking to see if the latest pictures are requiredd
#         date = '2015-06-03'
#         photos = 'photos'
#         chp = input('Do you want latest photos (Y/N) : ')
#         if chp == 'Y' or chp == 'y':
#             photos = 'latest_photos'
#         else:
#             date = input('Enter date(YYYY/MM/DD) : ') 

#         return date,photos
        
#     def fetch(url = 'http://www.nasa.gov/sites/default/files/thumbnails/image/web_first_images_release.png'):
#         image = QImage
#         image = QPixmap(requests.get(url).content)
#         return image
