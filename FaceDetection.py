import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
from PIL import Image
from Backend import Database



class Detection():
    def __init__(self):
        self.I=Database()
        self.list = self.I.fetchcode()
        self.ID=self.I.fetchID()+1


    def photo(self):
        cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
        while True:
            success, img = cap.read()
            imgs = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgs = cv2.cvtColor(imgs, cv2.COLOR_BGR2RGB)

            faceLoc = face_recognition.face_locations(imgs)

            #if len(faceLoc)==0:
                #cv2.imshow('Webcam', img)
                #cv2.waitKey(1)
                #continue
            encode = face_recognition.face_encodings(imgs, faceLoc,num_jitters=2)

            for encodeface, faceloca in zip(encode, faceLoc):  # 拿到脸的编码和摄像头中的脸
                #matchs = face_recognition.compare_faces(encodeListKnowen, encodeface)
                #faceDis = face_recognition.face_distance(encodeListKnowen, encodeface)
                if self.confirm(encodeface)==False:
                    self.list.append(encodeface)
                    Bytes=encodeface.dumps()

                    for face in faceLoc:
                        top, right, bottom, left = face

                        face_image = img[4*top:4*bottom, 4*left:4*right]
                        face_image = cv2.cvtColor(face_image, cv2.COLOR_BGR2RGB)
                        pil_image = Image.fromarray(face_image)
                        pil_image.save(f'Faces/{self.ID}.jpg')
                        blob_value = open(f'Faces/{self.ID}.jpg', 'rb').read()
                        self.ID+=1
                        self.I.insert(blob_value,Bytes)
                        self.matchname='Unknown'
                        #self.rectangleandmark(img, faceloca)
                #else:
                    #self.FindName(encodeface)

            for encodeface, faceloca in zip(encode, faceLoc):
                self.FindName(encodeface)
                self.rectangleandmark(img, faceloca)




            cv2.imshow('Webcam', img)
            key=cv2.waitKey(1)
            if key == ord('n') or key ==ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()


    def confirm(self,CAMFacecode):

        #if len(list)==0:
            #return False
        #else:
            #result = face_recognition.compare_faces(list, CAMFacecode)
            #print(result)
            #if True in result:
                #return True

        result = face_recognition.compare_faces(self.list, CAMFacecode,tolerance=0.5)

        if True in result:
            return True
        for i in range(3):
            result = face_recognition.compare_faces(self.list, CAMFacecode,tolerance=0.5)
            if True in result:
                return True
        return False


    def rectangleandmark(self,img,faceloca):
        cv2.rectangle(img, (4 * faceloca[3], 4 * faceloca[0]), (4 * faceloca[1], 4 * faceloca[2]), (0, 255, 0), 2)
        #cv2.rectangle(img, (4 * faceloca[3], 4 * faceloca[2]-35), (4 * faceloca[1],4*faceloca[2]), (0, 255, 0), cv2.FILLED)  # 画正方形在原图下方，填充颜色
        cv2.putText(img,self.matchname, (4 * faceloca[3], 4 * faceloca[0]-20), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)


    def FindName(self,x):
        faceDistance = face_recognition.face_distance(self.list, x)
        matchindex = np.argmin(faceDistance)
        self.matchname = self.I.FindName(self.list[matchindex].dumps())
        if self.matchname == None:
            self.matchname="Unknown"




p=Detection()
p.photo()
